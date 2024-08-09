import gf_auto


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
    def keyPress(key: str, time: int = 60):
        gf_auto.key_press(key, time)  # noqa


if __name__ == "__main__":
    ...
