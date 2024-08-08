from pathlib import Path

from pydantic import BaseModel
from loguru import logger
import yaml


with open(f"{Path(__file__).parent.parent}/config.yaml") as f:
    cfg = yaml.safe_load(f)

logger.info(cfg)


class Settings(BaseModel):
    config: dict = cfg


s = Settings()
