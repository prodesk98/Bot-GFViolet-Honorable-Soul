import math
from time import sleep
from pathlib import Path
from typing import Literal, Optional

from manager import MemoryRead, AutoControls
from pydantic import BaseModel
import yaml

mr = MemoryRead(
    "GrandFantasia.exe"
)


class Position(BaseModel):
    x: Optional[float] = 0.0
    y: Optional[float] = 0.0
    angle: Optional[float] = 0.0


class MemoryConfig(BaseModel):
    base: int
    addr: int
    offsets: list[int]
    type: Literal['str', 'int', 'float']


with open(f"{Path(__file__).parent.parent}/memory.yaml") as f:
    cfg: dict = yaml.safe_load(f)


class Player:
    def __init__(self):
        self.name: str = self.get_name()
        self.level: int = self.get_level()
        self.hp: int = self.get_hp()
        self.mp: int = self.get_mp()
        self.target: str | None = self.get_target()
        self.position: Position = self.get_position()

    @staticmethod
    def _get_memory_config(name: str) -> MemoryConfig:
        memory_config: dict = cfg.get(name)
        _base = memory_config.get('base')
        _addr = memory_config.get('addr')
        _type = memory_config.get('type')
        _offsets = memory_config.get('offsets')

        return MemoryConfig(
            **{
                "base": _base,
                "addr": _addr,
                "type": _type,
                "offsets": _offsets,
            }
        )

    @staticmethod
    def _read_memory(memory: MemoryConfig) -> str | int | float | None:
        if memory.type == 'str':
            return mr.read_string(
                addr=memory.base + memory.addr,
                offsets=memory.offsets
            )
        if memory.type == 'int':
            return mr.read_int(
                addr=memory.base + memory.addr,
                offsets=memory.offsets
            )
        if memory.type == 'float':
            return mr.read_float(
                addr=memory.base + memory.addr,
                offsets=memory.offsets
            )

    def get_name(self) -> str:
        memory = self._get_memory_config('name')
        self.name = self._read_memory(memory)
        return self.name

    def get_level(self) -> int:
        memory = self._get_memory_config('level')
        self.level = self._read_memory(memory)
        return self.level

    def get_hp(self) -> int:
        memory = self._get_memory_config('hp')
        self.hp = self._read_memory(memory)
        return self.hp

    def get_mp(self) -> int:
        memory = self._get_memory_config('mp')
        self.mp = self._read_memory(memory)
        return self.mp

    def get_target(self) -> str | None:
        memory = self._get_memory_config('target')
        self.target = self._read_memory(memory)
        return self.target

    def set_target(self, target: str | None = None) -> None:
        self.target = target

    def _pos_x(self) -> int:
        memory = self._get_memory_config('pos_x')
        return self._read_memory(memory)

    def _pos_y(self) -> int:
        memory = self._get_memory_config('pos_y')
        return self._read_memory(memory)

    def angle(self) -> float:
        memory = self._get_memory_config('angle')
        return self._read_memory(memory)

    def get_position(self) -> Position:
        _pos_x = self._pos_x()
        _pos_y = self._pos_y()
        _angle = self.angle()

        if (
            _pos_x is None or
            _pos_y is None or
            _angle is None
        ):
            raise Exception("Invalid local player position.")

        return Position(
            **{
                "x": _pos_x,
                "y": _pos_y,
                "angle": _angle,
            }
        )

    def __str__(self):
        return f"""
Player:
    - name: {self.name}
    - level: {self.level}
    - hp: {self.hp}
    - mp: {self.mp}
    - position:
        - x: {self.position.x}
        - y: {self.position.y}
        - angle: {self.position.angle}
    - target: {self.target}"""


class PlayerControl:
    def __init__(self, auto_controls: AutoControls):
        self.control = auto_controls
        self.current_angle = .0

    @staticmethod
    def calculate_rotation(player_x: float, player_y: float, target_x: float, target_y: float) -> float:
        delta_x = target_x - player_x
        delta_y = target_y - player_y

        angle_rad = math.atan2(delta_y, delta_x)
        angle_deg = math.degrees(angle_rad)

        final_angle = (angle_deg + 360) % 360
        return final_angle

    @staticmethod
    def convert_to_normalized_direction(angle: float) -> float:
        if angle <= 180:
            return angle / 180
        else:
            return (angle - 360) / 180

    def rotate_player(self, desired_angle: float):
        while abs(desired_angle - self.current_angle) > .01:
            normalized_direction = self.convert_to_normalized_direction(desired_angle - self.current_angle)

            if normalized_direction < 0:
                self.control.keyPress('a')
            else:
                self.control.keyPress('d')

            self.current_angle = max(-1, min(1, self.current_angle))
            sleep(.01)

    def move_to_point(self, player_x: float, player_y: float, target_x: float, target_y: float, desired_angle: float):
        while math.hypot(target_x - player_x, target_y - player_y) > 5:
            self.control.keyPress('w')
            player_x += math.cos(math.radians(self.current_angle * 180))
            player_y += math.sin(math.radians(self.current_angle * 180))
            sleep(.01)
