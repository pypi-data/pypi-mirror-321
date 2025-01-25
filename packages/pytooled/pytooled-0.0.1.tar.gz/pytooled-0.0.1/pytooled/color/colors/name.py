from .hex import Hex

from ..base import BaseColor

from ..._utils.constants import NAMED_COLORS
from ..._utils.tools import get_key_by_value

from ...typealias import ColorLike, ColorSequence, ColorName

def isname(string: ColorName) -> bool:
    return isinstance(string, str) and string.strip().lower() in NAMED_COLORS

class Name(BaseColor):

    _DEFAULT_COLOR = 'black'

    @property
    def color(self) -> ColorName:
        return self._color

    @color.setter
    def color(self, color: ColorLike) -> None:
        if isinstance(color, BaseColor):
            r, g, b, a = color.rgba

            hex_color = f'#{r:02x}{g:02x}{b:02x}'
            self._color = get_key_by_value(NAMED_COLORS, hex_color)

        else:
            assert isname(color)

            self._color = color.strip().lower()

    @property
    def rgba(self) -> ColorSequence:
        return Hex(NAMED_COLORS[self._color]).rgba