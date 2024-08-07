import os
import random
import shutil

from loguru import logger
from tqdm import tqdm

path_dataset = './dataset'
path_images = './images'
path_labels = './labels'
path_evals = './evals'


def remove_unlabeled():
    files = [
        f for f in os.listdir(path_dataset)
        if os.path.isfile(
            os.path.join(
                path_dataset, f
            )
        )
    ]

    # Remove unlabeled images
    for f in files:
        name, ext = os.path.splitext(f)
        if ext == '.jpg' and f"{name}.txt" not in files:
            logger.debug(
                f"Deleting {name}..."
            )
            os.remove(os.path.join(path_dataset, f))
        logger.info(
            f"{name} labeled..."
        )


def train_test_split(path: str | os.PathLike, test_split: float = 0.2):
    files = list(
        set([name[:-4] for name in os.listdir(path)]))

    logger.info(f"This folder has a total number of {len(files)} images")
    random.seed(42)
    random.shuffle(files)

    test_size = int(len(files) * test_split)
    train_size = len(files) - test_size

    for filex in tqdm(files[:train_size]):
        if filex == 'classes':
            continue
        shutil.copy2(path + filex + '.jpg', f"{path_images}/" + filex + '.jpg')
        shutil.copy2(path + filex + '.txt', f"{path_labels}/" + filex + '.txt')

    logger.info(f"Training data created with {100 - (test_split * 100)}% split {len(files[:train_size])} images")

    for filex in tqdm(files[train_size:]):
        shutil.copy2(path + filex + '.jpg', f"{path_evals}/images/" + filex + '.jpg')
        shutil.copy2(path + filex + '.txt', f"{path_evals}/labels/" + filex + '.txt')

    logger.info(f"Testing data created with a total of {len(files[train_size:])} images")
    logger.success("TASK COMPLETED")


remove_unlabeled()
train_test_split('./dataset/')
