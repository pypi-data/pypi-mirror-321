from typing import Type, List, Dict, Any
from pydantic import BaseModel, ValidationError
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
from rich.table import Table
from rich.text import Text
from rich import box
from itertools import groupby
from operator import itemgetter


def print_validation_errors(
    model_cls: Type[BaseModel],
    validation_error: ValidationError,
    field_infos: Dict[str, Any],
) -> None:
    """
    Pretty print Pydantic validation errors with field context.

    Args:
        model_cls: The Pydantic model class
        validation_error: The ValidationError exception
        field_infos: Dictionary of field information from get_field_info()
    """
    console = Console()
    errors = validation_error.errors()

    # Group errors by type
    errors_by_type = {
        k: list(g)
        for k, g in groupby(
            sorted(errors, key=itemgetter("type")), key=itemgetter("type")
        )
    }

    main_tree = Tree(f"[bold red]Validation Errors for {model_cls.__name__}")

    def format_type(annotation: Any) -> str:
        """Format type annotation into a readable string."""
        if get_origin(annotation) is not None:
            origin = get_origin(annotation)
            args = get_args(annotation)

            # Handle special cases
            if origin is Union:
                return " | ".join(
                    arg.__name__ if hasattr(arg, "__name__") else str(arg)
                    for arg in args
                )

            # Format generic types
            origin_name = (
                origin.__name__ if hasattr(origin, "__name__") else str(origin)
            )
            args_str = ", ".join(
                arg.__name__ if hasattr(arg, "__name__") else str(arg) for arg in args
            )
            return f"{origin_name}[{args_str}]"

        return (
            annotation.__name__ if hasattr(annotation, "__name__") else str(annotation)
        )

    def get_field_context(loc: tuple) -> tuple[str, str]:
        """Get field type and context information."""
        field_path = ".".join(str(x) for x in loc)
        field_info = field_infos.get(field_path)
        if not field_info:
            return "", ""

        # Get type information
        field_type = format_type(field_info.annotation)

        # Get context information
        context = []
        if field_info.description:
            context.append(f"Description: {field_info.description}")

        # Add validation rules
        rules = []
        for rule in [
            "gt",
            "ge",
            "lt",
            "le",
            "min_length",
            "max_length",
            "regex",
            "pattern",
            "multiple_of",
        ]:
            value = getattr(field_info, rule, None)
            if value is not None:
                rules.append(f"{rule}: {value}")

        if rules:
            context.append("Validation rules: " + ", ".join(rules))

        return field_type, "\n".join(context)

    # Handle missing fields
    if "missing" in errors_by_type:
        missing_node = main_tree.add("[yellow]Missing Required Fields")
        error_table = Table(box=box.ROUNDED, show_header=True)
        error_table.add_column("Field", style="bold yellow")
        error_table.add_column("Type", style="blue")
        error_table.add_column("Error Type", style="bold red")
        error_table.add_column("Message", style="italic")
        error_table.add_column("Context", style="dim")

        for error in errors_by_type["missing"]:
            field_path = ".".join(str(x) for x in error["loc"])
            field_type, context = get_field_context(error["loc"])
            error_table.add_row(
                field_path, field_type, "missing", "Field required", context
            )

        missing_node.add(error_table)

    # Handle type errors
    if "type_error" in errors_by_type:
        type_node = main_tree.add("[red]Type Errors")
        error_table = Table(box=box.ROUNDED, show_header=True)
        error_table.add_column("Field", style="bold red")
        error_table.add_column("Error Type", style="bold blue")
        error_table.add_column("Message", style="italic")
        error_table.add_column("Context", style="dim")

        for error in errors_by_type["type_error"]:
            field_path = ".".join(str(x) for x in error["loc"])
            field_type, context = get_field_context(error["loc"])
            error_table.add_row(
                field_path, field_type, "type_error", error["msg"], context
            )

        type_node.add(error_table)

    # Handle value errors
    if "value_error" in errors_by_type:
        value_node = main_tree.add("[magenta]Value Errors")
        error_table = Table(box=box.ROUNDED, show_header=True)
        error_table.add_column("Field", style="bold magenta")
        error_table.add_column("Error Type", style="bold blue")
        error_table.add_column("Message", style="italic")
        error_table.add_column("Context", style="dim")

        for error in errors_by_type["value_error"]:
            field_path = ".".join(str(x) for x in error["loc"])
            field_type, context = get_field_context(error["loc"])
            error_table.add_row(
                field_path, field_type, "value_error", error["msg"], context
            )

        value_node.add(error_table)

    # Handle other types of errors
    other_errors = {
        k: v
        for k, v in errors_by_type.items()
        if k not in ["missing", "type_error", "value_error"]
    }
    if other_errors:
        other_node = main_tree.add("[blue]Other Validation Errors")
        error_table = Table(box=box.ROUNDED, show_header=True)
        error_table.add_column("Field", style="bold")
        error_table.add_column("Error Type", style="bold blue")
        error_table.add_column("Message", style="italic")
        error_table.add_column("Context", style="dim")

        for error_type, errors in other_errors.items():
            for error in errors:
                field_path = ".".join(str(x) for x in error["loc"])
                context = get_field_context(error["loc"])
                error_table.add_row(field_path, error_type, error["msg"], context)

        other_node.add(other_table)

    # Print the error tree
    console.print(Panel(main_tree, title="Validation Errors", border_style="red"))


# Example usage
if __name__ == "__main__":
    from datetime import datetime
    from pydantic import Field, EmailStr
    from typing import Optional, List

    class Address(BaseModel):
        street: str = Field(..., min_length=5, description="Street address")
        city: str = Field(..., pattern="^[A-Za-z ]+$", description="City name")
        postal_code: str = Field(
            ..., pattern=r"^\d{5}$", description="5-digit postal code"
        )

    class User(BaseModel):
        name: str = Field(..., min_length=2, description="User's full name")
        age: int = Field(..., ge=0, le=150, description="User's age in years")
        email: EmailStr = Field(..., description="Valid email address")
        address: Address = Field(..., description="User's primary address")
        tags: Optional[List[str]] = Field(
            None, min_length=1, description="Optional user tags"
        )

    # Test with invalid data
    try:
        user = User.model_validate(
            {
                "name": "A",  # too short
                "age": -1,  # negative age
                "email": "not_an_email",  # invalid email
                "address": {
                    "street": "123",  # too short
                    "city": "New York123",  # contains numbers
                    "postal_code": "1234",  # not 5 digits
                },
                "tags": [],  # empty list
            }
        )
    except ValidationError as e:
        # Get field info using the previously defined get_field_info function
        from expedantic.utils import get_field_info

        field_infos = get_field_info(User)

        # Print validation errors with context
        print_validation_errors(User, e, field_infos)
