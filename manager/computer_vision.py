from os import PathLike
import pyautogui
from loguru import logger

pyautogui.useImageNotFoundException()


class ComputerVision:
    @staticmethod
    def locateOnScreen(image_path: PathLike | str, confidence: float = 0.95) -> tuple[int, int, int, int] | None:
        """
        Locate Image On Screen
        :param image_path:
        :param confidence:
        :return: left, top, width, height
        """
        try:
            box = pyautogui.locateOnScreen(image_path, confidence=confidence)
            return box.left, box.top, box.width, box.height
        except pyautogui.ImageNotFoundException:
            pass

    def locateCenter(self, image_path: PathLike | str, confidence: float = 0.95) -> tuple[int, int] | None:
        """
        Locate center object On Screen
        :return: x, y
        """
        box = self.locateOnScreen(image_path, confidence=confidence)
        if box is None:
            logger.error(
                "Unable to locate object in scene."
            )
            return
        coords = pyautogui.center(box)
        return coords.x, coords.y


if __name__ == "__main__":
    cv = ComputerVision()
    print(
        cv.locateCenter(
            image_path='images/btn_close.png'
        )
    )
