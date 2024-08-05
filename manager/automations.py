from enum import Enum

import pyautogui


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
        pyautogui.click(
            x=x,
            y=y,
            clicks=clicks,
            interval=interval,
            button=button.value,
        )

    @staticmethod
    def press(keys: list[str]):
        pyautogui.keyDown(
            key=keys[0]
        )


if __name__ == "__main__":
    auto = PyAutoGUI()
    auto.mouseClick(
        (200, 200),
        button=BUTTON.RIGHT,
        interval=2.0,
        clicks=5,
    )
    auto.press(
        [
            'enter',
            'w',
        ] * 45
    )
