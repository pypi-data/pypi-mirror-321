from typing import Type, Any, get_origin, get_args
import inspect
from pathlib import Path
from dataclasses import dataclass
from pydantic import BaseModel
from rich.console import Console
from rich.tree import Tree
from rich.text import Text
from rich.panel import Panel
from rich.style import Style


@dataclass
class FieldInfo:
    """Store information about a model field."""

    name: str
    type_str: str
    default: str
    description: str
    is_required: bool
    full_path: str


def get_type_string(field_type: Type[Any]) -> str:
    """Convert Python type hints to command-line argument type strings."""
    origin = get_origin(field_type)
    if origin is None:
        if field_type == bool:
            return "flag"
        elif field_type == int:
            return "integer"
        elif field_type == float:
            return "float"
        elif field_type == str:
            return "string"
        elif isinstance(field_type, type) and issubclass(field_type, BaseModel):
            return "object"
        else:
            return str(field_type.__name__)

    args = get_args(field_type)
    if origin == list:
        inner_type = get_type_string(args[0])
        return f"list[{inner_type}]"
    elif origin == dict:
        key_type = get_type_string(args[0])
        value_type = get_type_string(args[1])
        return f"dict[{key_type}, {value_type}]"
    return str(field_type)


def get_model_fields(
    model_class: Type[BaseModel], prefix: str = "", parent_required: bool = True
) -> list[FieldInfo]:
    """
    Recursively collect field information from a model and its nested models.

    Args:
        model_class: The Pydantic model class to analyze
        prefix: Prefix for nested field names (e.g., "outer.inner")
        parent_required: Whether the parent field is required

    Returns:
        List of FieldInfo objects containing field information
    """
    fields = []
    schema = model_class.model_json_schema()
    required_fields = set(schema.get("required", []))
    properties = schema.get("properties", {})

    for field_name, field_info in properties.items():
        field = model_class.model_fields[field_name]
        full_path = f"{prefix}.{field_name}" if prefix else field_name

        # Get field type
        field_type = field.annotation
        type_str = get_type_string(field_type)

        # Get default value
        default = field.default
        if default is None and not field.is_required():
            default_str = "None"
        elif default == ...:
            default_str = "Required"
        else:
            default_str = str(default)

        # Get help text
        description = field_info.get("description", "")

        # Check if field is required
        is_required = field_name in required_fields and parent_required

        field_info = FieldInfo(
            name=field_name,
            type_str=type_str,
            default=default_str,
            description=description,
            is_required=is_required,
            full_path=full_path,
        )
        fields.append(field_info)

        # Recursively process nested models
        if (
            isinstance(field_type, type)
            and not get_origin(field_type)
            and issubclass(field_type, BaseModel)
            and field_type != model_class
        ):  # Avoid recursive models
            nested_fields = get_model_fields(
                field_type, prefix=full_path, parent_required=is_required
            )
            fields.extend(nested_fields)

    return fields


def create_field_tree(fields: list[FieldInfo]) -> Tree:
    """Create a tree structure from field information."""
    root = Tree("")  # Empty string for root to hide it

    def format_field(field: FieldInfo) -> str:
        """Format field information for display."""
        name_style = "bold magenta" if field.is_required else "magenta"
        type_style = "bold green" if field.is_required else "green"

        # Format the field name
        formatted = f"[{name_style}]--{field.full_path}[/] "

        # Add type with appropriate style
        formatted += f"[{type_style}]{field.type_str}[/] "

        # Add required/default info and/or default value
        if field.is_required:
            formatted += "Required"

        # Always show default value if it exists
        if field.default not in ["Required", "None"]:
            formatted += f" [yellow][default: {field.default}][/]"

        # Add description if present
        if field.description:
            formatted += f" - {field.description}"

        return formatted

    # Group fields by their parent path
    field_groups = {}
    for field in fields:
        parts = field.full_path.split(".")
        if len(parts) == 1:
            # Top-level field
            root.add(format_field(field))
        else:
            # Nested field
            parent_path = ".".join(parts[:-1])
            if parent_path not in field_groups:
                field_groups[parent_path] = []
            field_groups[parent_path].append(field)

    # Add nested fields to the tree
    for parent_path, group_fields in field_groups.items():
        parent_tree = root
        # Create intermediate nodes if they don't exist
        for part in parent_path.split("."):
            found = False
            for node in parent_tree.children:
                if node.label.startswith(f"--{part}"):
                    parent_tree = node
                    found = True
                    break
            if not found:
                parent_tree = parent_tree.add(f"[bold blue]--{part}[/]")

        # Add fields to their parent node
        for field in group_fields:
            parent_tree.add(format_field(field))

    return root


def print_model_help(
    model_class: Type[BaseModel], program_name: str = "program"
) -> None:
    """
    Print help information for a Pydantic model as if it were an argparse program.
    Handles nested models and displays them in a tree structure.

    Args:
        model_class: The Pydantic BaseModel class to generate help for
        program_name: Name of the program to show in usage
    """
    console = Console()

    # Get model location information
    try:
        module = inspect.getmodule(model_class)
        module_path = Path(inspect.getfile(model_class)).resolve()
        line_number = inspect.getsourcelines(model_class)[1]
        location_info = f"[dim]Defined in {module_path}:{line_number}[/dim]"
    except (TypeError, OSError):
        location_info = "[dim]Location information unavailable[/dim]"

    # Print model information
    model_doc = inspect.getdoc(model_class) or "No description available"
    info_panel = Panel.fit(
        f"{model_doc}\n\n{location_info}",
        title=model_class.__name__,
        border_style="blue",
    )
    console.print(info_panel)

    # Print usage
    console.print(f"\n[bold]Usage:[/bold] {program_name} [OPTIONS]")

    # Get and print field tree
    fields = get_model_fields(model_class)
    field_tree = create_field_tree(fields)

    # Print each child of the root tree directly to remove the outer "Fields" label
    for child in field_tree.children:
        console.print(child)
    console.print()


# Example usage
if __name__ == "__main__":
    from pydantic import Field

    class DatabaseConfig(BaseModel):
        """Database connection configuration."""

        host: str = Field(..., description="Database host address")
        port: int = Field(5432, description="Database port")

    class LogConfig(BaseModel):
        """Logging configuration."""

        level: str = Field("INFO", description="Logging level")
        file: str = Field(None, description="Log file path")

    class AppConfig(BaseModel):
        """Example application configuration with nested models."""

        name: str = Field("testapp", description="Application name")
        version: str = Field("1.0.0", description="Application version")
        debug: bool = Field(False, description="Enable debug mode")

        # Nested models
        database: DatabaseConfig = Field(..., description="Database configuration")
        logging: LogConfig = Field(
            default_factory=LogConfig, description="Logging configuration"
        )

        # List and dict fields
        allowed_hosts: list[str] = Field(
            default_factory=list, description="List of allowed hosts"
        )
        metadata: dict[str, Any] = Field(
            default_factory=dict, description="Additional metadata"
        )

    # print_model_help(AppConfig, "myapp")

    from expedantic.printer import print_help

    print_help(AppConfig)
