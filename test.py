from time import sleep
from core import Player
from manager.utils import next_angle, move_to_target
from manager import AutoControls
from loguru import logger
import pydirectinput

# TODO: remover esse aquivo

controls = AutoControls()

if __name__ == "__main__":
    while True:
        player = Player()
        n = move_to_target(
            pos_x_current=player.position.x,
            pos_y_current=player.position.y,
            rotation_current=player.position.rx,
            rotation_target=0.31,
            pos_x_destination=250.1875,
            pos_y_destination=440.375,
        )
        logger.debug(f"target: {n}")
        if n == 1:
            pydirectinput.keyDown("left")
            pydirectinput.keyUp("left")
            continue
        if n == 2:
            pydirectinput.keyDown("right")
            pydirectinput.keyUp("right")
            continue
        pydirectinput.keyDown("up")
        pydirectinput.keyUp("up")
        sleep(.7)

