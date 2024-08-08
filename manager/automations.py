import gf_auto


class AutoControls:
    @staticmethod
    def mouseClick_Left(coords: tuple[int, int]) -> None:
        x, y = coords
        gf_auto.click_left(x, y) # noqa

    @staticmethod
    def mouseClick_Right(coords: tuple[int, int]) -> None:
        x, y = coords
        gf_auto.click_right(x, y) # noqa

    @staticmethod
    def mouseMove(coords: tuple[int, int]) -> None:
        x, y = coords
        gf_auto.move_mouse(x, y)  # noqa


if __name__ == "__main__":
    ...
