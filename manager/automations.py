from enum import Enum

import pydirectinput


class BUTTON(Enum):
    LEFT: str = "left"
    MIDDLE: str = "middle"
    RIGHT: str = "right"
    PRIMARY: str = "primary"
    SECONDARY: str = "secondary"


class PyAutoGUI:
    @staticmethod
    def mouseRelease(coords: tuple[int, int], button: BUTTON = BUTTON.LEFT, delay: float = 60.0):
        ...

    @staticmethod
    def mouseClick(coords: tuple[int, int], clicks: int = 1, interval: float = 0.0, button: BUTTON = BUTTON.LEFT):
        x, y = coords
        pydirectinput.click()

    @staticmethod
    def press(keys: list[str]):
        pydirectinput.keyDown(
            key=keys[0]
        )


if __name__ == "__main__":
    auto = PyAutoGUI()
    auto.mouseClick(
        (10, 20),
    )
    auto.mouseClick(
        (10, 20),
    )
    auto.mouseClick(
        (10, 20),
    )
