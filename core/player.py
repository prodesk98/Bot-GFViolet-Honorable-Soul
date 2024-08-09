from pathlib import Path
from typing import Literal

from manager import MemoryRead
from pydantic import BaseModel
import yaml

mr = MemoryRead(
    "GrandFantasia.exe"
)


class Position(BaseModel):
    x: float
    y: float
    rx: float


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

    def _rot_x(self) -> float:
        memory = self._get_memory_config('rot_x')
        return self._read_memory(memory)

    def get_position(self) -> Position:
        _pos_x = self._pos_x()
        _pos_y = self._pos_y()
        _rot_x = self._rot_x()

        return Position(
            **{
                "x": _pos_x,
                "y": _pos_y,
                "rx": _rot_x,
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
        - rx: {self.position.rx}
    - target: {self.target}"""
