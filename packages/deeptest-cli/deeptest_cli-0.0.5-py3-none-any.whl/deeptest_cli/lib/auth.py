import os
import json
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich import box
import typer

console = Console()
CONFIG_DIR = os.path.expanduser("~/.deeptest")
CREDENTIALS_FILE = os.path.join(CONFIG_DIR, "credentials.json")


class Auth:
    @staticmethod
    def get_api_key() -> Optional[str]:
        """Get API key from credentials file."""
        try:
            with open(CREDENTIALS_FILE) as f:
                credentials = json.load(f)
                return credentials.get("api_key")
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    @staticmethod
    def save_api_key(api_key: str) -> None:
        """Save API key to credentials file."""
        os.makedirs(CONFIG_DIR, exist_ok=True)
        with open(CREDENTIALS_FILE, "w") as f:
            json.dump({"api_key": api_key}, f)
        # Set file permissions to user read/write only
        os.chmod(CREDENTIALS_FILE, 0o600)

    @staticmethod
    def clear_api_key() -> None:
        """Remove API key from credentials file."""
        try:
            os.remove(CREDENTIALS_FILE)
        except FileNotFoundError:
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
