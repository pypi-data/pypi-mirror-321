from typing import Optional
from pydantic import BaseModel
import yaml

# There is a duplicate of this file in brain/lib/models.py.
# ANY CHANGES MUST ALSO BE MADE THERE.


class DeeptestTest(BaseModel):
    name: str
    steps: list[str]


class DeeptestConfig(BaseModel):
    base_url: str
    timeout: float = 300  # seconds


class DeeptestYaml(BaseModel):
    name: str
    description: Optional[str] = None
    config: DeeptestConfig
    tests: list[DeeptestTest]


def parse_yaml_file(file_path: str) -> DeeptestYaml:
    with open(file_path, "r") as file:
        yaml_content = yaml.safe_load(file)
        # Validate YAML structure using Pydantic
        validated_yaml = DeeptestYaml(**yaml_content)
        return validated_yaml
