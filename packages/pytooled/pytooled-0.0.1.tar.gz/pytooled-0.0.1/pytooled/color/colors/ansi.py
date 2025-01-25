from re import fullmatch

from .hex import Hex

from ..base import BaseColor

from ..._utils.constants import ANSI_COLORS
from ..._utils.tools import get_key_by_value, boundary_color

from ...typealias import ColorLike, ColorSequence, ColorAnsi

def extract(obj: ColorAnsi) -> ColorAnsi | None:
    if isinstance(obj, str):

        if ismatch := fullmatch(r'^\033\[(\d+)m', obj):
            return int(ismatch.group(1))

        elif ismatch := fullmatch(r'\u001b\[38;2;(\d{1,3});(\d{1,3});(\d{1,3})m', obj):
            return tuple(map(boundary_color, ismatch.groups()))

    elif isinstance(obj, int):
        return obj

    return None

def isansi(obj: str | int) -> bool:
    return extract(obj) is not None

class Ansi(BaseColor):

    _DEFAULT_COLOR = 0

    @property
    def color(self) -> ColorAnsi:
        r, g, b = self.rgb
        return f'\u001b[38;2;{r};{g};{b}m'

    @color.setter
    def color(self, color: ColorLike) -> None:
        if isinstance(color, BaseColor):
            r, g, b, a = color.rgba

            hex = f'#{r:02x}{g:02x}{b:02x}{a:02x}'
            self._color = get_key_by_value(ANSI_COLORS, hex, hex)

            if self._color not in ANSI_COLORS:
                self._color = (r, g, b, a)

        else:
            assert isansi(color)

            self._color = extract(color)

    @property
    def rgba(self) -> ColorSequence:
        if isinstance(self._color, tuple):
            if len(self._color) == 3:
                return self._color + (255,)
            return self._color

        return Hex(ANSI_COLORS[self._color]).rgba