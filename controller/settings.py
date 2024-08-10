from pathlib import Path

from pydantic import BaseModel
import yaml


with open(f"{Path(__file__).parent.parent}/flow.yaml") as f:
    cfg = yaml.safe_load(f)


class Settings(BaseModel):
    config: dict = cfg


s = Settings()
