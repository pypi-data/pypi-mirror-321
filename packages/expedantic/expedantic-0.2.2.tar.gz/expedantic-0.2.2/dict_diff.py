from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.layout import Layout
from rich.columns import Columns
from typing import Dict, Any


def visualize_dict_diff(
    dict1: Dict[str, Any],
    dict2: Dict[str, Any],
    title1: str = "Dict 1",
    title2: str = "Dict 2",
) -> None:
    """
    Creates a beautiful visualization of the differences between two dictionaries.

    Args:
        dict1: First dictionary to compare
        dict2: Second dictionary to compare
        title1: Title for the first dictionary
        title2: Title for the second dictionary
    """
    console = Console()

    # Create a layout for side-by-side comparison
    layout = Layout()
    layout.split_column(Layout(name="top"), Layout(name="bottom"))

    # Create the comparison table
    table = Table(
        title="Dictionary Comparison", show_header=True, header_style="bold magenta"
    )
    table.add_column("Key", style="cyan")
    table.add_column(f"{title1} Value", style="green")
    table.add_column(f"{title2} Value", style="blue")
    table.add_column("Status", style="yellow")

    # Get all unique keys
    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))

    # Compare dictionaries
    for key in all_keys:
        val1 = dict1.get(key, "—")
        val2 = dict2.get(key, "—")

        if key not in dict1:
            status = "[red]Added in Dict 2[/red]"
        elif key not in dict2:
            status = "[red]Removed in Dict 2[/red]"
        elif val1 != val2:
            status = "[yellow]Modified[/yellow]"
        else:
            status = "[green]Unchanged[/green]"

        table.add_row(str(key), str(val1), str(val2), status)

    # Create summary panel
    summary = Panel(
        Text.assemble(
            ("Summary Statistics\n\n", "bold magenta"),
            (f"Total keys: {len(all_keys)}\n", "white"),
            (f"Keys only in {title1}: {len(dict1.keys() - dict2.keys())}\n", "green"),
            (f"Keys only in {title2}: {len(dict2.keys() - dict1.keys())}\n", "blue"),
            (
                f"Modified keys: {sum(1 for k in all_keys if k in dict1 and k in dict2 and dict1[k] != dict2[k])}\n",
                "yellow",
            ),
            (
                f"Unchanged keys: {sum(1 for k in all_keys if k in dict1 and k in dict2 and dict1[k] == dict2[k])}",
                "white",
            ),
        ),
        title="Summary",
        border_style="bright_blue",
    )

    # Print everything
    console.print("\n")
    console.print(table)
    console.print("\n")
    console.print(summary)
    console.print("\n")


# Example usage
if __name__ == "__main__":
    dict1 = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "occupation": "Engineer",
        "hobbies": ["reading", "painting"],
    }

    dict2 = {
        "name": "Alice",
        "age": 31,
        "city": "Boston",
        "skills": ["Python", "JavaScript"],
        "hobbies": ["reading", "painting", "photography"],
    }

    visualize_dict_diff(dict1, dict2, "Original", "Updated")
