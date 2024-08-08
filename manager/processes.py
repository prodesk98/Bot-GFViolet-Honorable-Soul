from loguru import logger
from pymem import Pymem


class MemoryRead:
    def __init__(self, process_name: str):
        self._process = Pymem(process_name)

    def _find_pointer(self, addr: hex, offsets: list[hex]) -> hex:
        pointer = self._process.read_int(addr)
        for i, offset in enumerate(offsets):
            last = pointer
            if len(offsets) == i + 1:
                break
            pointer = self._process.read_int(pointer + offset)
            logger.debug("[%s + %s] -> %s" % (hex(last), hex(offset), hex(pointer)))
        if len(offsets) > 0:
            return pointer + offsets[-1]
        return pointer

    def read_float(self, addr: hex, offsets: list[hex]) -> float | None:
        pointer = self._find_pointer(addr, offsets)
        buffer = self._process.read_float(pointer)
        return buffer

    def read_int(self, addr: hex, offsets: list[hex]) -> int | None:
        pointer = self._find_pointer(addr, offsets)
        buffer = self._process.read_int(pointer)
        return buffer

    def read_string(self, addr: hex, offsets: list[hex]) -> str | None:
        pointer = self._find_pointer(addr, offsets)
        buffer = self._process.read_string(pointer)
        return buffer


if __name__ == "__main__":
    mr = MemoryRead('GrandFantasia.exe')
    logger.info(
        mr.read_int(
            0x00400000 + 0x009E1C2C,
            [
                0xDC,
                0x8,
                0x10,
                0x8,
                0x1C,
            ]
        )
    )
