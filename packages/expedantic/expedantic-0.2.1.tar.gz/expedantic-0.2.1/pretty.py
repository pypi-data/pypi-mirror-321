from typing import Dict, Any, get_origin, get_args, Union
from pydantic import BaseModel, Field
from pydantic.fields import FieldInfo
from rich.console import Console
from rich.tree import Tree
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich import box


def format_type(type_annotation: Any) -> str:
    """Format type annotation into a readable string."""
    if get_origin(type_annotation) is not None:
        origin = get_origin(type_annotation)
        args = get_args(type_annotation)

        # Handle special cases
        if origin is Union:
            return " | ".join(
                arg.__name__ if hasattr(arg, "__name__") else str(arg) for arg in args
            )

        # Format generic types like List[str], Dict[str, Any]
        origin_name = origin.__name__ if hasattr(origin, "__name__") else str(origin)
        args_str = ", ".join(
            arg.__name__ if hasattr(arg, "__name__") else str(arg) for arg in args
        )
        return f"{origin_name}[{args_str}]"

    return (
        type_annotation.__name__
        if hasattr(type_annotation, "__name__")
        else str(type_annotation)
    )


def create_validation_table(field: FieldInfo) -> Table:
    """Create a table showing field validation rules."""
    table = Table(box=box.ROUNDED, show_header=False, padding=(0, 1))
    table.add_column("Rule", style="bold cyan")
    table.add_column("Value", style="yellow")

    # Common validation attributes
    validation_attrs = {
        "gt": "Greater than",
        "ge": "Greater than or equal to",
        "lt": "Less than",
        "le": "Less than or equal to",
        "min_length": "Minimum length",
        "max_length": "Maximum length",
        "regex": "Regex pattern",
        "pattern": "Pattern",
        "multiple_of": "Multiple of",
        "max_digits": "Maximum digits",
        "decimal_places": "Decimal places",
    }

    for attr, label in validation_attrs.items():
        value = getattr(field, attr, None)
        if value is not None:
            table.add_row(label, str(value))

    # Add enum values if present
    if hasattr(field, "annotation") and get_origin(field.annotation) is None:
        try:
            if hasattr(field.annotation, "__members__"):  # Enum check
                enum_values = ", ".join(field.annotation.__members__.keys())
                table.add_row("Allowed values", enum_values)
        except (AttributeError, TypeError):
            pass

    return table


def print_field_info(fields_dict: Dict[str, FieldInfo], title: str = "Model Fields"):
    """
    Pretty print Pydantic FieldInfo using Rich.

    Args:
        fields_dict: Dictionary mapping field paths to their FieldInfo objects
        title: Title for the main panel
    """
    console = Console()

    # Create main tree
    main_tree = Tree(title)

    # Group fields by their parent path
    grouped_fields = {}
    for path, field in fields_dict.items():
        parts = path.split(".")
        if len(parts) > 1:
            parent = ".".join(parts[:-1])
            if parent not in grouped_fields:
                grouped_fields[parent] = []
            grouped_fields[parent].append((parts[-1], field))
        else:
            if "" not in grouped_fields:
                grouped_fields[""] = []
            grouped_fields[""].append((path, field))

    def add_fields_to_tree(tree: Tree, fields: list, indent_level: int = 0):
        for name, field in sorted(fields):
            # Create field node
            field_text = Text()
            field_text.append(f"{name}: ", style="bold green")
            field_text.append(format_type(field.annotation), style="blue")

            if field.description:
                field_text.append(f"\n{'  ' * (indent_level + 1)}└─ ", style="dim")
                field_text.append(field.description, style="italic")

            field_node = tree.add(field_text)

            # Add validation rules if any exist
            validation_table = create_validation_table(field)
            if validation_table.row_count > 0:
                field_node.add(
                    Panel(
                        validation_table,
                        title="Validation Rules",
                        title_align="left",
                        border_style="dim",
                    )
                )

            # Add nested fields if they exist
            if name in grouped_fields:
                add_fields_to_tree(field_node, grouped_fields[name], indent_level + 1)

    # Add root level fields
    if "" in grouped_fields:
        add_fields_to_tree(main_tree, grouped_fields[""])

    # Print the tree in a panel
    console.print(Panel(main_tree, title=title, border_style="blue"))


# Example usage
if __name__ == "__main__":
    from enum import Enum
    from datetime import datetime
    from typing import Optional, List

    class UserType(str, Enum):
        ADMIN = "admin"
        USER = "user"
        GUEST = "guest"

    class Location(BaseModel):
        latitude: float = Field(description="Latitude coordinate", ge=-90, le=90)
        longitude: float = Field(description="Longitude coordinate", ge=-180, le=180)

    class Address(BaseModel):
        street: str = Field(description="Street address", min_length=5, max_length=100)
        city: str = Field(description="City name", pattern="^[A-Za-z ]+$")
        location: Optional[Location] = Field(
            description="Geographic coordinates", default=None
        )

    class User(BaseModel):
        id: int = Field(description="User ID", gt=0)
        name: str = Field(description="User's full name", min_length=2, max_length=50)
        email: str = Field(
            description="Email address",
            pattern=r"[^@]+@[^@]+\.[^@]+",
        )
        type: UserType = Field(
            description="User type/role in the system", default=UserType.USER
        )
        address: Address = Field(description="User's primary address")
        tags: List[str] = Field(description="User tags", min_length=1, max_length=10)
        created_at: datetime = Field(
            description="Account creation timestamp", default_factory=datetime.now
        )
        settings: Dict[str, Any] = Field(
            description="User settings", default_factory=dict
        )

    # Get and print field info
    from expedantic.utils import (
        get_field_info,
    )  # assuming get_field_info is in previous_code.py

    fields = get_field_info(User)
    print_field_info(fields, "User Model Schema")
