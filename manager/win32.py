from os import PathLike

import pyautogui
import win32gui  # noqa
import win32con  # noqa
import win32api  # noqa
from PIL import ImageGrab
from loguru import logger

RELATIVE_X = 0.5
RELATIVE_Y = 0.5


class Win32:
    def __init__(self, window_name: str):
        self._window_name = window_name
        self._hwnd = win32gui.FindWindow(None, window_name)
        if not self._hwnd:
            raise Exception(
                "Unable to locate window"
            )

    def get_region(self) -> tuple[int, int, int, int]:
        """
        with, height, left, top
        :return:
        """
        rect = self.get_window_rect()
        titlebar_pixels = 26
        w = rect[0]
        h = rect[1] + titlebar_pixels
        return w, h, rect[2] - w, rect[3] - h - titlebar_pixels

    def get_window_size(self) -> tuple[int, int]:
        """
        :return: width, height
        """
        rect = win32gui.GetWindowRect(self._hwnd)
        width = rect[2] - rect[0]
        height = rect[3] - rect[1]
        return width, height

    def get_window_position(self) -> tuple[int, int]:
        """
        :return: left, top
        """
        rect = win32gui.GetWindowRect(self._hwnd)
        left = rect[0]
        top = rect[1]
        return left, top

    def get_window_position_center(self) -> tuple[int, int]:
        rect: tuple[int, int, int, int] = self.get_window_rect()
        left, top = rect[0], rect[1]
        width, height = rect[2] - rect[0], rect[3] - rect[1]

        x, y = (left + int(width / 2), top + int(height / 2))
        return x, y

    def get_window_rect(self):
        rect = win32gui.GetWindowRect(self._hwnd)
        return rect

    def capture_window(self, save_path: str | PathLike):
        rect = self.get_window_rect()
        screenshot = ImageGrab.grab(bbox=rect)
        screenshot.save(save_path)
        logger.info(f"screenshot saved to {save_path}")

    def activate_window(self):
        win32gui.SetForegroundWindow(self._hwnd)

    @staticmethod
    def get_winfo_screen() -> tuple[int, int]:
        width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)  # noqa
        height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)  # noqa
        return width, height

    def get_center_window(self) -> tuple[int, int, int, int]:
        """
        :return: x, y, width, height
        """
        screen_width, screen_height = self.get_winfo_screen()
        window_width, window_height = self.get_window_size()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        return x, y, window_width, window_height

    def centralize_window(self) -> None:
        x, y, screen_width, screen_height = self.get_center_window()

        win32gui.MoveWindow(
            self._hwnd,
            x,
            y,
            screen_width,
            screen_height,
            True
        )

    @staticmethod
    def get_mouse_position() -> tuple[int, int]:
        """
        :return: x, y
        """
        pos_x, pos_y = pyautogui.position()
        return pos_x, pos_y


if __name__ == "__main__":
    ...
