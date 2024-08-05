import win32gui # noqa
import win32con # noqa
import win32api # noqa


class Win32:
    def __init__(self, window_name: str):
        self._window_name = window_name
        self._hwnd = win32gui.FindWindow(None, window_name)
        if not self._hwnd:
            raise Exception(
                "Unable to locate window"
            )

    def get_window_size(self) -> tuple[int, int] | None:
        """
        :return: width, height
        """
        rect = win32gui.GetWindowRect(self._hwnd)
        width = rect[2] - rect[0]
        height = rect[3] - rect[1]
        return width, height

    def centralize_window(self) -> None:
        screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

        window_width, window_height = self.get_window_size()

        new_x = (screen_width - window_width) // 2
        new_y = (screen_height - window_height) // 2

        win32gui.MoveWindow(
            self._hwnd,
            new_x,
            new_y,
            window_width,
            window_height,
            True
        )


if __name__ == "__main__":
    win32 = Win32('Grand Fantasia Violet')
    print(win32.centralize_window())
