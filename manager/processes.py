from typing import Any
from loguru import logger
from ReadWriteMemory import ReadWriteMemory, Process

BASE_ADDRESS = 0x00400000


class Memory:
    def __init__(self, process_name: str):
        self._rwm = ReadWriteMemory()
        self._process = self._rwm.get_process_by_name(process_name)
        self._process.open()

    def get_process(self) -> Process:
        return self._process

    def read(self, addr: hex, offsets: list[hex]) -> Any:
        process = self.get_process()
        pointer = process.get_pointer(
            BASE_ADDRESS + addr,
            offsets
        )
        buffer = process.read(pointer)
        return buffer


if __name__ == "__main__":
    p = Memory('GrandFantasia.exe')
    logger.info(
        p.read(
            0x009E1C2C,
            [
                0xDC,
                0x8,
                0x10,
                0x8,
                0x8,
            ]
        )
    )

