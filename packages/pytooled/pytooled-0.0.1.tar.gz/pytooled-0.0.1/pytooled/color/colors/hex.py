from re import fullmatch

from ..base import BaseColor

from ...typealias import ColorLike, ColorSequence, ColorHex

def extract(obj: ColorHex) -> ColorHex | None:
    if isinstance(obj, str) and (
        ismatch := fullmatch(
            r'^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$',
            obj
        )):
        return ismatch.group(1)

    return None

def ishex(string: ColorHex) -> bool:
    return extract(string) is not None

class Hex(BaseColor):

    _DEFAULT_COLOR = '#000'

    @property
    def color(self) -> ColorHex:
        return f'#{self._color}'

    @color.setter
    def color(self, color: ColorLike) -> None:
        if isinstance(color, BaseColor):
            r, g, b, a = color.rgba
            self._color = f'{r:02x}{g:02x}{b:02x}{a:02x}'

        else:
            assert ishex(color)

            self._color = extract(color)

    @property
    def rgba(self) -> ColorSequence:
        match len(hex := self._color):

            case 3:
                return (
                    int(hex[0]*2, 16),
                    int(hex[1]*2, 16),
                    int(hex[2]*2, 16),
                    255
                )

            case 4:
                return (
                    int(hex[0]*2, 16),
                    int(hex[1]*2, 16),
                    int(hex[2]*2, 16),
                    int(hex[3]*2, 16)
                )

            case 6:
                return (
                    int(hex[0:2], 16),
                    int(hex[2:4], 16),
                    int(hex[4:6], 16),
                    255
                )

            case 8:
                return (
                    int(hex[0:2], 16),
                    int(hex[2:4], 16),
                    int(hex[4:6], 16),
                    int(hex[6:8], 16)
                )