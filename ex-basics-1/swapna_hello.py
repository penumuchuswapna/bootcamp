import sys

def main(name: str = "world") -> None:
    """Print a greeting."""
    print(f"Hello, {name}!")

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args[0] if args else "world")
