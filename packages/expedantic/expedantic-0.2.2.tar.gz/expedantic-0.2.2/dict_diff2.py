from rich.console import Console
from rich.tree import Tree
from rich.text import Text
from rich.panel import Panel
from rich.columns import Columns
from typing import Dict, Any, Union


def create_diff_tree(
    d1: Dict[str, Any], d2: Dict[str, Any], parent: Tree | None = None
) -> Tree:
    """
    Recursively create a tree representation showing the differences between two dictionaries.
    """

    def format_value(v: Any) -> str:
        if isinstance(v, (dict, list)):
            return ""
        return f": {repr(v)}"

    def add_dict_to_tree(
        d: Dict[str, Any], tree: Tree, other_dict: Dict[str, Any] | None = None
    ) -> None:
        for key, value in sorted(d.items()):
            if other_dict is None or key not in other_dict:
                # Key only exists in this dict
                label = Text(f"{key}{format_value(value)}", style="dim")
                node = tree.add(label)
                if isinstance(value, dict):
                    add_dict_to_tree(value, node)
                elif isinstance(value, list):
                    add_list_to_tree(value, node)

    def add_list_to_tree(lst: list, tree: Tree) -> None:
        for i, value in enumerate(lst):
            if isinstance(value, dict):
                node = tree.add(f"[{i}]")
                add_dict_to_tree(value, node)
            else:
                tree.add(f"[{i}] {repr(value)}")

    def compare_values(key: str, v1: Any, v2: Any, tree: Tree) -> None:
        if isinstance(v1, dict) and isinstance(v2, dict):
            node = tree.add(Text(key, style="bold"))
            create_diff_tree(v1, v2, node)
        elif isinstance(v1, list) and isinstance(v2, list):
            node = tree.add(Text(key, style="bold"))
            if v1 == v2:
                for i, v in enumerate(v1):
                    node.add(Text(f"[{i}] {repr(v)}", style="green"))
            else:
                node_1 = node.add(Text("Previous:", style="red"))
                for i, v in enumerate(v1):
                    node_1.add(Text(f"[{i}] {repr(v)}", style="red"))
                node_2 = node.add(Text("Current:", style="blue"))
                for i, v in enumerate(v2):
                    node_2.add(Text(f"[{i}] {repr(v)}", style="blue"))
        else:
            if v1 == v2:
                tree.add(Text(f"{key}{format_value(v1)}", style="green"))
            else:
                node = tree.add(Text(key, style="yellow bold"))
                node.add(Text(f"Previous: {repr(v1)}", style="red"))
                node.add(Text(f"Current: {repr(v2)}", style="blue"))

    # Start with a new tree if none is provided
    if parent is None:
        parent = Tree("📦 Dictionary Comparison")

    # All keys in both dictionaries
    all_keys = sorted(set(d1.keys()) | set(d2.keys()))

    for key in all_keys:
        if key in d1 and key in d2:
            # Key exists in both dictionaries
            compare_values(key, d1[key], d2[key], parent)
        elif key in d1:
            # Key only in first dictionary
            node = parent.add(Text(f"❌ {key} (removed)", style="red"))
            value = d1[key]
            if isinstance(value, dict):
                add_dict_to_tree(value, node)
            elif isinstance(value, list):
                add_list_to_tree(value, node)
            else:
                node.add(Text(repr(value), style="red"))
        else:
            # Key only in second dictionary
            node = parent.add(Text(f"✨ {key} (added)", style="blue"))
            value = d2[key]
            if isinstance(value, dict):
                add_dict_to_tree(value, node)
            elif isinstance(value, list):
                add_list_to_tree(value, node)
            else:
                node.add(Text(repr(value), style="blue"))

    return parent


def visualize_tree_diff(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> None:
    """
    Create a tree-style visualization of the differences between two dictionaries.

    Args:
        dict1: First dictionary (previous state)
        dict2: Second dictionary (current state)
    """
    console = Console()

    # Create the tree
    diff_tree = create_diff_tree(dict1, dict2)

    # Create a legend panel
    legend = Panel(
        Text.assemble(
            ("Legend\n\n", "bold"),
            ("✨ ", "blue"),
            ("Added in current\n", "default"),
            ("❌ ", "red"),
            ("Removed from previous\n", "default"),
            ("Green", "green"),
            (" Unchanged values\n", "default"),
            ("Yellow", "yellow"),
            (" Modified keys\n", "default"),
            ("Red", "red"),
            (" Previous values\n", "default"),
            ("Blue", "blue"),
            (" Current values", "default"),
        ),
        title="Guide",
        border_style="bright_blue",
    )

    # Print everything
    console.print("\n")
    console.print(Columns([diff_tree, legend]))
    console.print("\n")


# Example usage
if __name__ == "__main__":
    # Example with nested structures
    dict1 = {
        "user": {
            "name": "Alice",
            "age": 30,
            "contact": {"email": "alice@email.com", "phone": "123-456-7890"},
        },
        "settings": {"theme": "dark", "notifications": True},
        "permissions": ["read", "write"],
        "stats": {"login_count": 10, "last_login": "2024-01-15"},
    }

    dict2 = {
        "user": {
            "name": "Alice",
            "age": 31,
            "contact": {
                "email": "alice.new@email.com",
                "phone": "123-456-7890",
                "address": "123 Main St",
            },
        },
        "settings": {"theme": "light", "notifications": True, "language": "en"},
        "permissions": ["read", "write", "admin"],
        "activity": {"last_action": "profile_update"},
    }

    visualize_tree_diff(dict1, dict2)
