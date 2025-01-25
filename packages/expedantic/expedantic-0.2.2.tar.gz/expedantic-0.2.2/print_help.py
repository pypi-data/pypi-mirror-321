import inspect
from pathlib import Path
from typing import Type, Any, get_origin, get_args
from pydantic import BaseModel
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box


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


def print_model_help(
    model_class: Type[BaseModel], program_name: str = "program"
) -> None:
    """
    Print help information for a Pydantic model as if it were an argparse program.

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

    # Print usage header
    console.print(f"\n[bold]Usage:[/bold] {program_name} [OPTIONS]")

    # Create options table
    table = Table(show_header=True, header_style="bold", box=box.SQUARE)
    table.add_column("Option", style="cyan")
    table.add_column("Type", style="green")
    table.add_column("Default", style="yellow")
    table.add_column("Help", style="white")

    # Get model schema and field info
    schema = model_class.model_json_schema()

    required_fields = schema.get("required", [])
    properties = schema.get("properties", {})

    for field_name, field_info in properties.items():
        field = model_class.model_fields[field_name]

        # Format option name
        option_name = Text()
        if field_name in required_fields:
            option_name.append("--" + field_name, style="bold cyan")
        else:
            option_name.append("--" + field_name, style="cyan")

        # Get field type
        field_type = get_type_string(field.annotation)

        # Get default value
        default = field.default
        if default is None and not field.is_required():
            default_str = "None"
        elif default == ...:
            default_str = "Required"
        else:
            default_str = str(default)

        # Get help text
        help_text = field_info.get("description", "")

        table.add_row(option_name, field_type, default_str, help_text)

    # console.print(table)
    console.print(Panel(table))


# Example usage
if __name__ == "__main__":
    from pydantic import Field

    class ExampleConfig(BaseModel):
        """Example configuration model."""

        name: str = Field(..., description="Name of the user")
        age: int = Field(None, description="Age of the user")
        scores: list[float] = Field(
            default_factory=list, description="List of test scores"
        )
        is_active: bool = Field(True, description="Whether the user is active")
        metadata: dict[str, Any] = Field(
            default_factory=dict, description="Additional metadata"
        )

    print_model_help(ExampleConfig, "config_tool")
