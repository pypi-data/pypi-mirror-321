from pydantic import ValidationError
import typer
from deeptest.lib.models import parse_yaml_file
from deeptest.lib.yaml import load_yaml_files
from rich.console import Console
from rich.panel import Panel
from rich import box

app = typer.Typer(help="Validate YAML files in .deeptest directory")
console = Console()


def format_validation_error(error: ValidationError) -> str:
    """
    Formats a Pydantic ValidationError into a human-readable message.
    """
    messages = []
    for err in error.errors():
        # Get the field location
        location = ".".join(str(loc) for loc in err["loc"])

        # Convert error type to friendly message
        if err["type"] == "missing":
            msg = f"Required field '{location}' is missing"
        elif err["type"] == "type_error":
            msg = f"Invalid type for '{location}'. {err['msg']}"
        elif err["type"] == "value_error":
            msg = f"Invalid value for '{location}'. {err['msg']}"
        else:
            msg = f"Error in '{location}': {err['msg']}"

        messages.append(msg)

    return "\n".join(messages)


@app.callback(invoke_without_command=True)
def validate() -> None:
    """Validate all YAML files in the .deeptest directory."""
    yaml_files = load_yaml_files()

    if not yaml_files:
        raise typer.Exit(1)

    for yaml_file in yaml_files:
        try:
            parse_yaml_file(yaml_file)
        except ValidationError as e:
            error_message = format_validation_error(e)
            console.print(
                Panel(
                    f"[red]Validation Error[/red]\n\n{error_message}\n\n"
                    "[yellow]Please check your YAML file and ensure all required fields are present.[/yellow]",
                    title="Validation Failed",
                    border_style="red",
                )
            )
            raise typer.Exit(1)
    console.print(
        Panel(
            "All YAML files are valid!",
            style="bold green",
            box=box.ROUNDED,
        )
    )
