# import typer

# app = typer.Typer()

# @app.command()
# def greet(name: str):
#     """Greet the user with their name"""
#     typer.echo(f"Hello, {name}!")

# if __name__ == "__main__":
#     app()
import typer

app = typer.Typer()

@app.command()
def greet(name: str = typer.Argument(..., help="The name of the person to greet")):
    """Greet the user with their name"""
    typer.echo(f"Hello, {name}!")

if __name__ == "__main__":
    app()
