from pathlib import Path
from time import sleep

from loguru import logger
from manager import (
    AutoControls,
    ComputerVision
)

controls = AutoControls()
computer_vision = ComputerVision()

UI_CLICK_MAX_ATTEMPTS = 4


class Bot:
    def __init__(self, config: dict, stage: str):
        self.config = config
        self.stages: list[dict] = [s for s in config['stages']]
        self.current_stage: list[dict] = []
        self.set_stage(stage)

    def set_stage(self, stage: str) -> None:
        self.current_stage = next(iter(d.get(stage) for d in self.stages if d.get(stage)))
        logger.debug(f"Stage: {stage}")

    def get_current_stage(self) -> list[dict] | None:
        return self.current_stage

    @staticmethod
    def _ui_click(**kwargs):
        button = kwargs.get('button')
        delay = kwargs.get('delay', .0)
        logger.debug(f"Waiting {delay * 2}seg...")
        sleep(delay * 2)
        coords = None
        attempts = 0
        while coords is None:
            coords = computer_vision.locateCenter(
                f"{Path(__file__).parent.parent}/images/ui/{button}.png"
            )
            if coords is not None:
                break
            attempts += 1
            logger.error(
                f"Retry, {attempts} attempts, Max {UI_CLICK_MAX_ATTEMPTS}"
            )
            if attempts > UI_CLICK_MAX_ATTEMPTS:
                logger.error(
                    f"Not found UI -> {button}"
                )
                return
            sleep(.7)
        x, y = coords
        logger.debug(f"Object UI -> x:{x}, y:{y}")
        wait = delay / 2
        logger.debug(f"Waiting {wait}seg...")
        sleep(wait)
        controls.mouseMove(coords)
        logger.debug(f"move -> x:{x}, y:{y}")
        logger.debug(f"Waiting {wait}seg...")
        sleep(wait)
        controls.mouseClick_Left(coords)
        logger.debug(f"click({button}) -> x:{x}, y:{y}")

    @staticmethod
    def _mouse_move(**kwargs):
        x, y = kwargs.get('x', 0), kwargs.get('y', 0)
        coords = (x, y)
        delay = kwargs.get('delay', .0)
        logger.debug(f"Waiting {delay}seg...")
        sleep(delay)
        controls.mouseMove(coords)
        logger.debug(f"moved -> x:{x}, y:{y}")

    @staticmethod
    def _mouse_click(**kwargs):
        button = kwargs.get('button')
        x, y = kwargs.get('x', 0), kwargs.get('y', 0)
        coords = (x, y)
        delay = kwargs.get('delay', .0)
        repeat = kwargs.get('repeat', 1)
        if button == 'right':
            wait = delay * 2
            logger.debug(f"Waiting {wait}seg...")
            sleep(wait)
            for rep in range(repeat):
                controls.mouseClick_Right(coords)
                sleep(delay / 2)
                logger.debug(
                    f"[{rep + 1}] clicked({button}) -> x:{x}, y:{y}"
                )
            return
        if button == 'left':
            controls.mouseMove(coords)
            wait = delay * 2
            logger.debug(f"Waiting {wait}seg...")
            sleep(wait)
            for rep in range(repeat):
                controls.mouseClick_Left(coords)
                sleep(delay / 2)
                logger.debug(
                    f"[{rep + 1}] clicked({button}) -> x:{x}, y:{y}"
                )
            return

    def start(self):
        interactions: list[dict] = self.current_stage
        for it in interactions:
            act = it['action']
            logger.debug(
                f"Bot action: {act}"
            )
            command = it.copy()
            del command['action']

            if act == 'mouseClick':
                self._mouse_click(**command)

            if act == 'mouseMove':
                self._mouse_move(**command)

            if act == 'uiClick':
                self._ui_click(**command)


if __name__ == "__main__":
    from controller import settings

    bot = Bot(
        settings.config,
        stage="start"
    )
    bot.start()
