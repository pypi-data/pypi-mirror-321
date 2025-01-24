import keyring
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich import box
import typer

console = Console()
SERVICE_NAME = "deeptest-cli"
ACCOUNT_NAME = "default"


class Auth:
    @staticmethod
    def get_api_key() -> Optional[str]:
        """Get API key from keyring."""
        return keyring.get_password(SERVICE_NAME, ACCOUNT_NAME)

    @staticmethod
    def save_api_key(api_key: str) -> None:
        """Save API key to keyring."""
        keyring.set_password(SERVICE_NAME, ACCOUNT_NAME, api_key)

    @staticmethod
    def clear_api_key() -> None:
        """Remove API key from keyring."""
        try:
            keyring.delete_password(SERVICE_NAME, ACCOUNT_NAME)
        except keyring.errors.PasswordDeleteError:
            pass

    @staticmethod
    def is_logged_in() -> bool:
        """Check if API key exists."""
        return Auth.get_api_key() is not None

    @staticmethod
    def get_headers():
        """Get headers with API key."""
        api_key = Auth.get_api_key()
        if not api_key:
            console.print(
                Panel(
                    "No API key found. Please run 'deeptest login' first.",
                    style="bold red",
                    box=box.ROUNDED,
                )
            )
            raise typer.Exit(1)

        return {"X_API_KEY": api_key}
