from hashlib import md5
from uuid import uuid4

import keyboard
from loguru import logger
from manager import (
    ComputerVision,
    AutoControls,
    Win32,
)
from time import sleep
from controller import settings

computer_vision = ComputerVision()
auto_controls = AutoControls()
win32 = Win32(
    "Grand Fantasia Violet"
)


def _call_automations():
    logger.info(
        "Automations starting..."
    )
    coords_window = win32.get_window_position_center()
    auto_controls.mouseMove(coords_window)
    auto_controls.mouseClick_Left(coords_window)
    sleep(1.2)
    coords_object = computer_vision.locateCenter(
        "images/btn_ok.png"
    )
    if coords_object is None:
        logger.error(
            "Object not found in scene"
        )
        return
    auto_controls.mouseClick_Left(coords_object)


def _call_screenshot():
    settings.MOD_CAPTURE_WINDOW = not settings.MOD_CAPTURE_WINDOW
    count: int = 0
    while settings.MOD_CAPTURE_WINDOW is True:
        filename = f"screenshot/{count}_{md5(uuid4().bytes).hexdigest()[:8]}.jpg"
        win32.capture_window(filename)
        sleep(0.7)
        count += 1


keyboard.add_hotkey(
    "F1",
    _call_automations,
)
keyboard.add_hotkey(
    "F2",
    _call_screenshot,
)

keyboard.wait('esc')
