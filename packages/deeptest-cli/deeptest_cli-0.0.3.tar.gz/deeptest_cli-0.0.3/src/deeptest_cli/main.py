import typer
from deeptest_cli.commands import login, runner, validate

app = typer.Typer(
    help="A well-structured CLI application",
    no_args_is_help=True,
)

# Add sub-commands
app.add_typer(login.app, name="", help="Login")
app.add_typer(runner.app, name="", help="Run tests")
app.add_typer(
    validate.app, name="validate", help="Validate YAML files in .deeptest directory"
)

# @app.callback()
# def callback(
#     version: Optional[bool] = typer.Option(
#         None,
#         "--version",
#         "-v",
#         help="Show the application version and exit.",
#         is_eager=True,
#     )
# ) -> None:
#     """A well-structured CLI application."""
#     if version:
#         print(f"My CLI Version: {__version__}")
#         raise typer.Exit()

if __name__ == "__main__":
    app()
