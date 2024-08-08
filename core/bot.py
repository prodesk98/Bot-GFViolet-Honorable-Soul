from time import sleep

from loguru import logger
from manager import (
    AutoControls
)

controls = AutoControls()


class Bot:
    def __init__(self, config: dict, stage: str):
        self.config = config
        self.stages: list[dict] = [s for s in config['stages']]
        self.current_stage: list[dict] = []
        self.set_stage(stage)

    def set_stage(self, stage: str) -> None:
        self.current_stage = next(iter(d.get(stage) for d in self.stages if d.get(stage)))

    def get_current_stage(self) -> list[dict] | None:
        return self.current_stage

    @staticmethod
    def _mouse_click(**kwargs):
        button = kwargs.get('button')
        x, y = kwargs.get('x', 0), kwargs.get('y', 0)
        delay = kwargs.get('delay', 0.0)
        if button == 'right':
            sleep(delay)
            return controls.mouseClick_Right(
                (x, y)
            )
        if button == 'left':
            sleep(delay)
            return controls.mouseClick_Left(
                (x, y)
            )

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


if __name__ == "__main__":
    from controller import settings

    bot = Bot(
        settings.config,
        stage="start"
    )
    bot.start()
