from pathlib import Path
from typing import List, Optional
from rich.console import Console
from rich.panel import Panel
from rich import box

console = Console()


def load_yaml_files(yaml_file: Optional[str] = None) -> List[Path]:
    """
    Get list of YAML files to process, either a specific file or all files in .deeptest directory.

    Args:
        yaml_file: Optional specific YAML file to load (either full path or relative to .deeptest)

    Returns:
        List[Path]: List of paths to YAML files to process
    """
    deeptest_dir = Path(".deeptest")
    yaml_files = []

    if yaml_file:
        # Try as full path first
        file_path = Path(yaml_file)
        if file_path.is_file():
            yaml_files = [file_path]
        else:
            # Try relative to .deeptest
            potential_path = deeptest_dir / yaml_file
            if potential_path.is_file():
                yaml_files = [potential_path]
            else:
                console.print(
                    Panel(
                        f"Specified YAML file not found: {yaml_file}",
                        style="bold red",
                        box=box.ROUNDED,
                    )
                )
                return []
    else:
        # Get all YAML files in .deeptest directory
        if not deeptest_dir.is_dir():
            console.print(
                Panel(
                    f"Directory not found: {deeptest_dir}",
                    style="bold red",
                    box=box.ROUNDED,
                )
            )
            return []
        yaml_files = [f for f in deeptest_dir.glob("*.yaml")]

    return yaml_files
