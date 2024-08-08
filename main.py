import keyboard
from loguru import logger

from core.bot import Bot
from detect import Detect
from manager import (
    ComputerVision,
    AutoControls,
    Win32,
)
from time import sleep
from controller import settings

computer_vision = ComputerVision()
auto_controls = AutoControls()
GFWindow = Win32(
    "Grand Fantasia Violet"
)


def _call_bot():
    logger.info(
        "Bot starting..."
    )
    GFWindow.centralize_window()
    try:
        bot = Bot(
            settings.config,
            stage="start"
        )
        bot.start()
    except Exception as err:
        logger.error(err)


def _call_center_window():
    GFWindow.centralize_window()


def _call_mouse_position():
    while True:
        pos_x, pos_y = GFWindow.get_mouse_position()
        logger.debug("Mouse Position: %i, %i" % (pos_x, pos_y))
        sleep(.6)


def _call_show_display():
    try:
        region = GFWindow.get_region()
        cv = Detect(region)
        cv.display()
    except Exception as err:
        logger.error(err)


keyboard.add_hotkey(
    "F1",
    _call_bot,
)
keyboard.add_hotkey(
    "F2",
    _call_center_window,
)
keyboard.add_hotkey(
    "F3",
    _call_show_display,
)
keyboard.add_hotkey(
    "F4",
    _call_mouse_position,
)

logger.success(
    "Setup started... Waiting commands:\n\n"
    "F1: Start bot\n"
    "F2: Center screen\n"
    "F3: Display bot vision\n"
    "F4: Mouse position"
)
keyboard.wait('esc')
