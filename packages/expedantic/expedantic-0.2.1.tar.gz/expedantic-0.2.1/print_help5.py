from typing import Type, Any, get_origin, get_args
import inspect
from pathlib import Path
from dataclasses import dataclass
from pydantic import BaseModel, Field
from rich.console import Console, Group
from rich.tree import Tree
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from rich.columns import Columns
from rich.style import Style


@dataclass
class FieldInfo:
    """Store information about a model field."""

    name: str
    full_path: str
    type_str: str
    default: str
    description: str
    is_required: bool
    nesting_level: int


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
        elif (
            isinstance(field_type, type)
            and not get_origin(field_type)
            and issubclass(field_type, BaseModel)
        ):
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
    model_class: Type[BaseModel], prefix: str = "", level: int = 0
) -> list[FieldInfo]:
    """Recursively collect field information from a model and its nested models."""
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
        if field.is_required():
            default_str = "Required"
        else:
            default_str = str(field.get_default(call_default_factory=True))
        # if default is None and not field.is_required():
        #     default_str = "None"
        # elif default == ...:
        #     default_str = "Required"
        # else:
        #     default_str = str(default)

        # Get help text
        description = field_info.get("description", "")

        # Check if field is required
        is_required = field_name in required_fields

        field_info = FieldInfo(
            name=field_name,
            full_path=full_path,
            type_str=type_str,
            default=default_str,
            description=description,
            is_required=is_required,
            nesting_level=level,
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
                field_type, prefix=full_path, level=level + 1
            )
            fields.extend(nested_fields)

    return fields


def create_aligned_tree_and_table(
    title: str, fields: list[FieldInfo]
) -> tuple[Tree, Table]:
    """Create a tree and table with aligned rows."""
    # Create tree
    root = Tree(title)
    field_map = {}  # Map of paths to tree nodes

    # First pass: create tree structure and track line numbers
    line_to_field = {}  # Track which field appears on which line
    current_line = 0

    for field in fields:
        parts = field.full_path.split(".")
        current = root

        for i, part in enumerate(parts):
            path = ".".join(parts[: i + 1])
            if path not in field_map:
                style = "bold magenta" if field.is_required else "magenta"
                if i == len(parts) - 1:  # Leaf node
                    label = Text(f".{part}", style=style)
                    line_to_field[current_line] = field
                else:
                    label = Text(part, style=style)
                    current_line += 1  # Add empty line for guide lines

                node = current.add(label)
                field_map[path] = node
                current_line += 1
            current = field_map[path]

    # Create table with proper spacing
    table = Table(show_header=True, box=None, padding=(0, 1), collapse_padding=True)
    table.add_column("Field", style="magenta", no_wrap=True)
    table.add_column("Type", style="green", no_wrap=True)
    table.add_column("Status", style="yellow", no_wrap=True)
    table.add_column("Description", style="white")

    # Second pass: add aligned table rows
    for line in range(current_line):
        if line in line_to_field:
            field = line_to_field[line]
            # Style field name based on required status
            name_style = "bold magenta" if field.is_required else "magenta"
            field_name = Text(f"--{field.full_path}", style=name_style)

            # Style type
            type_text = Text(
                field.type_str, style="bold green" if field.is_required else "green"
            )

            # Format status
            if field.is_required:
                status = Text("Required", style="yellow bold")
                if field.default not in ["Required", "None"]:
                    status.append(f" [default: {field.default}]", style="yellow")
            else:
                status = Text(f"[default: {field.default}]", style="yellow")

            # Add row with field information
            table.add_row(field_name, type_text, status, field.description)
        else:
            # Add empty row to maintain alignment
            table.add_row("", "", "", "")

    return Group(Text(title), *root.children), table


def create_field_table(field: FieldInfo) -> Table:
    """Create a table showing detailed field information."""
    table = Table(
        box=None, show_header=False, show_edge=False, pad_edge=False, padding=(0, 1)
    )

    # Add columns for field details
    table.add_column("Property", style="blue")
    table.add_column("Value")

    # Add rows for field details
    table.add_row("Type:", Text(field.type_str, style="green"))

    # Status (Required/Default)
    if field.is_required:
        status = Text("Required", style="yellow bold")
        if field.default not in ["Required", "None"]:
            status.append(f" [default: {field.default}]", style="yellow")
    else:
        status = Text(f"[default: {field.default}]", style="yellow")
    table.add_row("Status:", status)

    if field.description:
        table.add_row("Description:", field.description)

    return table


def print_model_help(
    model_class: Type[BaseModel], program_name: str = "program"
) -> None:
    """Print help information for a Pydantic model with aligned side-by-side view."""
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
    console.print(f"\n[bold]Usage:[/bold] {program_name} [OPTIONS]\n")

    # Get fields
    fields = get_model_fields(model_class)

    # Create aligned tree and table
    tree, table = create_aligned_tree_and_table(model_class.__name__, fields)

    # Create panels
    tree_panel = Panel(tree, title="Structure", border_style="blue", padding=(0, 1))
    table_panel = Panel(table, title="Details", border_style="blue", padding=(0, 1))

    # Create columns with proper ratio

    columns = Columns([tree_panel, table_panel], expand=True)
    console.print(columns)


# Example usage
if __name__ == "__main__":

    class DatabaseConfig(BaseModel):
        """Database connection settings."""

        host: str = Field(..., description="Database host address")
        port: int = Field(5432, description="Port number")
        credentials: dict[str, str] = Field(
            default_factory=dict, description="Credential key-value pairs"
        )

    class DeepConfig(BaseModel):
        """Third level configuration."""

        setting1: str = Field(..., description="Deep setting 1")
        setting2: int = Field(42, description="Deep setting 2")

    class NestedConfig(BaseModel):
        """Second level configuration."""

        name: str = Field(..., description="Nested config name")
        deep: DeepConfig = Field(..., description="Even deeper settings")

    class AppConfig(BaseModel):
        """Application configuration with multiple nesting levels."""

        app_name: str = Field(..., description="Name of the application")
        debug: bool = Field(False, description="Enable debug mode")
        db: DatabaseConfig = Field(..., description="Database settings")
        nested: NestedConfig = Field(..., description="Nested settings")

    print_model_help(AppConfig, "myapp")
