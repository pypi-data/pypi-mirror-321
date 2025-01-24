from rich.console import Console
from rich.panel import Panel
from rich import box
import requests
import typer
from rich.prompt import Prompt
from deeptest.lib.auth import Auth
from rich.markdown import Markdown


console = Console()

app = typer.Typer()


@app.command()
def login():
    """Save your DeepTest API key."""

    instructions = """
# Getting Your API Key 🔑

1. Go to https://app.deeptest.sh
2. Navigate to Settings > Workspace settings > Generate API key
3. Copy your API key from the API Key section

Your API key starts with 'dt_' and looks something like: dt_1234...
    """

    console.print(
        Panel(
            Markdown(instructions),
            title="Welcome to DeepTest!",
            style="blue",
            box=box.ROUNDED,
        )
    )

    api_key = Prompt.ask("Enter your API key")

    try:
        # Verify the API key works
        # response = requests.get(
        #     f"{Config.BASE_URL}/v1/workspaces/verify-api-key",
        #     headers={
        #         "X_API_KEY": api_key,

        #     },
        # )
        # response.raise_for_status()

        Auth.save_api_key(api_key)
        console.print(
            Panel(
                "API key saved successfully!",
                style="bold green",
                box=box.ROUNDED,
            )
        )
    except requests.RequestException as e:
        console.print(
            Panel(
                f"Invalid API key: {str(e)}",
                style="bold red",
                box=box.ROUNDED,
            )
        )
        raise typer.Exit(1)


@app.command()
def logout():
    """Remove saved API key."""
    Auth.clear_api_key()
    console.print(
        Panel(
            "API key removed successfully!",
            style="bold green",
            box=box.ROUNDED,
        )
    )
