import gf_auto
import keyboard

print(gf_auto.__all__)


def click():
    """
    coordinates: (X, Y)
    :return:
    """
    gf_auto.click(
        240,
        240,
    )


keyboard.add_hotkey('F3', click)
keyboard.wait('esc')
