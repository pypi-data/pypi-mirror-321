from re import fullmatch

from .hex import Hex

from ..base import BaseColor

from ...typealias import ColorLike, ColorSequence, ColorHex

def extract(obj: ColorHex) -> ColorHex | None:
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, str) and (
        ismatch := fullmatch(
            r'^(0x)?([0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$',
            obj
        )):
        return ismatch.group(2)
    return None

def ishexdec(obj: ColorHex) -> bool:
    return extract(obj) is not None

class HexDec(BaseColor):

    _DEFAULT_COLOR = 0x000

    @property
    def color(self) -> ColorHex:
        if isinstance(self._color, str):
            self._color = int(self._color, 16)
        return self._color

    @color.setter
    def color(self, color: ColorLike) -> None:
        assert ishexdec(color)

        self._color = extract(color)

    @property
    def rgba(self) -> ColorSequence:
        if isinstance(self._color, str):
            return Hex(self._color).rgba
        return Hex(f'{self._color:08x}').rgba