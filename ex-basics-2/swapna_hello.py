import sys
from rich.console import Console

console = Console()

def main(name: str = "world") -> None:
    """Print a greeting using rich."""
    console.print(f"Hello, [bold green]{name}[/bold green]!", style="bold cyan")

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args[0] if args else "world")
