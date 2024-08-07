import os

from loguru import logger

path = './dataset'

files = [
    f for f in os.listdir(
        path
    ) if os.path.isfile(
        os.path.join(
            path, f
        )
    )
]


for f in files:
    name, ext = os.path.splitext(f)
    if ext == '.jpg' and f"{name}.txt" not in files:
        logger.debug(
            f"Deleting {name}..."
        )
        os.remove(os.path.join(path, f))
