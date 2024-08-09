from loguru import logger
from core.bot import Bot
from gui import GUI
from manager import (
    ComputerVision,
    AutoControls,
    Win32,
)
from core import Player
from controller import settings

computer_vision = ComputerVision()
auto_controls = AutoControls()
GFWindow = Win32(
    "Grand Fantasia Violet"
)
player = Player()


def _call_bot():
    logger.info(
        "Bot starting..."
    )
    GFWindow.centralize_window()
    try:
        bot = Bot(
            settings.config,
            stage="open_quest"
        )
        bot.start()
    except Exception as err:
        logger.error(err)


if __name__ == "__main__":
    panel = GUI(title="GF Violet Bot")
    panel.add_label(str(player))
    panel.add_button("start", _call_bot)
    panel.window.mainloop()
