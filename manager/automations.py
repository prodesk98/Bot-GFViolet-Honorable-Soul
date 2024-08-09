from time import sleep

import gf_auto
import pydirectinput


class AutoControls:
    @staticmethod
    def mouseClick_Left(coords: tuple[int, int], time: int = 120) -> None:
        x, y = coords
        gf_auto.mouse_click(x, y, "left", time) # noqa

    @staticmethod
    def mouseClick_Right(coords: tuple[int, int], time: int = 120) -> None:
        x, y = coords
        gf_auto.mouse_click(x, y, "right", time) # noqa

    @staticmethod
    def mouseMove(coords: tuple[int, int]) -> None:
        x, y = coords
        gf_auto.mouse_move(x, y)  # noqa

    @staticmethod
    def keyPress(key: str, time: float = .6):
        pydirectinput.keyDown(key)
        sleep(time)
        pydirectinput.keyUp(key)


if __name__ == "__main__":
    ...
