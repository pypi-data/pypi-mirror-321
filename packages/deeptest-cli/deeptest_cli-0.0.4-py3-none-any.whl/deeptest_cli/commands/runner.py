import os
import time
from typing import Optional

from pyfiglet import Figlet
import requests
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.spinner import Spinner
from rich.progress import Progress
from rich.live import Live
from rich.table import Table
from deeptest_cli.lib.auth import Auth
from deeptest_cli.config import Config
from deeptest_cli.lib.models import parse_yaml_file
from deeptest_cli.lib.yaml import load_yaml_files
import typer


# Initialize the controller
console = Console()
app = typer.Typer()


def render_running_tests(test_cases: list, table: Table):
    table.add_row("")
    sorted_tests = sorted(
        test_cases, key=lambda x: x["status"] != "RUNNING", reverse=False
    )
    for test in sorted_tests:
        status_icon = {
            "PENDING": Spinner("dots", style="bright_black"),
            "RUNNING": Spinner("dots", style="blue"),
            "SUCCESS": "✅",
            "FAILED": "❌",
        }.get(test["status"], "")

        status_style = {
            "PENDING": "bright_black",
            "RUNNING": "blue",
            "SUCCESS": "green",
            "FAILED": "red",
        }.get(test["status"], "")

        table.add_row(status_icon, test["name"], style=status_style)
    table.add_row("")
    return table


def raise_for_status(res: requests.Response):
    if res.status_code != 200:
        error_detail = res.json().get("detail", "No error details provided")
        console.print(
            Panel(
                f"Error {res.status_code}: {error_detail}",
                style="bold red",
                box=box.ROUNDED,
            )
        )
        raise typer.Exit(1)


@app.command()
def run(
    yaml_file: Optional[str] = typer.Option(
        None, "-f", "--file", help="Specific YAML file to run tests from"
    ),
):
    yaml_files = load_yaml_files(yaml_file)

    f = Figlet(font="slant")
    console.print(f.renderText("deeptest"), style="bold purple")

    test_suite_id = None
    try:
        for yaml_file in yaml_files:
            console.print(
                Panel(
                    f"Running tests from {os.path.basename(yaml_file)}",
                    style="bold blue",
                    box=box.ROUNDED,
                )
            )
            yaml_content = parse_yaml_file(yaml_file)

            headers = Auth.get_headers()

            res = requests.post(
                f"{Config.BASE_URL}/v1/cli/test_suite",
                headers=headers,
                json={
                    "name": yaml_content.name,
                    "description": yaml_content.description,
                    "config": yaml_content.config.model_dump(),
                    "tests": [test.model_dump() for test in yaml_content.tests],
                },
            )
            raise_for_status(res)
            test_suite_id = res.json()["test_suite"]["id"]

            table = Table(show_footer=False, show_header=False)
            table.box = None

            progress = Progress()
            task = progress.add_task(
                "[blue]Running tests...", total=len(yaml_content.tests)
            )

            with Live(refresh_per_second=4, auto_refresh=True) as live:
                while True:
                    status_res = requests.get(
                        f"{Config.BASE_URL}/v1/cli/test_suite/{test_suite_id}/status",
                        headers=headers,
                    )
                    raise_for_status(status_res)

                    test_cases = status_res.json()["test_cases"]
                    all_complete = all(
                        test["status"] not in ["PENDING", "RUNNING"]
                        for test in test_cases
                    )

                    completed = sum(
                        1
                        for test in test_cases
                        if test["status"] not in ["PENDING", "RUNNING"]
                    )
                    progress.update(
                        task,
                        completed=completed,
                        description="[blue bold]Running tests...",
                    )

                    table = Table(show_footer=False, show_header=False)
                    table.box = None
                    table.title = progress
                    table = render_running_tests(test_cases, table)

                    succeeded = sum(
                        1 for test in test_cases if test["status"] == "SUCCESS"
                    )
                    failed = sum(1 for test in test_cases if test["status"] == "FAILED")
                    if all_complete:
                        complete_color = "green" if failed == 0 else "red"
                        status_table = Table(
                            box=box.ROUNDED,
                            border_style=complete_color,
                            show_footer=False,
                            show_header=False,
                            expand=True,
                            width=console.width,
                        )
                        status_table.add_column()
                        status_table.add_row("Test Summary:", style=complete_color)
                        status_table.add_row(
                            f"✓ {succeeded} succeeded", style=complete_color
                        )
                        status_table.add_row(f"✗ {failed} failed", style=complete_color)
                        status_table.add_row("")
                        status_table.add_row(
                            f"🔗 https://app.deeptest.sh/runs/{test_suite_id}",
                            style=f"{complete_color} bold",
                        )
                        table.caption = status_table
                        live.update(table)
                        break

                    status_table = Table(
                        box=box.ROUNDED,
                        border_style="white",
                        show_footer=False,
                        show_header=False,
                        expand=True,
                        width=console.width,
                    )
                    status_table.add_column()
                    status_table.add_row("Test Summary:", style="white")
                    status_table.add_row(
                        f"✓ {succeeded} succeeded", style="bright_black"
                    )
                    status_table.add_row(f"✗ {failed} failed", style="bright_black")
                    status_table.add_row("")
                    status_table.add_row(
                        f"🔗 https://app.deeptest.sh/runs/{test_suite_id}",
                        style="white bold",
                    )

                    table.caption = status_table

                    live.update(table)
                    time.sleep(2)
    except KeyboardInterrupt:
        console.print(
            Panel(
                "Test execution cancelled by user. Tests still running in the background:\n\n"
                f"🔗 https://app.deeptest.sh/runs/{test_suite_id}",
                style="yellow",
                box=box.ROUNDED,
            )
        )
