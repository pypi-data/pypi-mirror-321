from typing import Sequence

from ..base import BaseColor

from ..._utils.tools import boundary_hue_based_color_models

from ...typealias import ColorLike, ColorSequence

class HSB(BaseColor):

    _DEFAULT_COLOR = (0, 0, 0)

    @property
    def color(self) -> ColorSequence:
        return self._color

    @color.setter
    def color(self, color: ColorLike) -> None:
        if isinstance(color, BaseColor):
            r, g, b, a = color.rgba

            r /= 255
            g /= 255
            b /= 255
            a /= 255

            c_max = max(r, g, b)
            c_min = min(r, g, b)
            delta = c_max - c_min

            if delta == 0:
                h = 0
            elif c_max == r:
                h = 60 * (((g - b) / delta) % 6)
            elif c_max == g:
                h = 60 * (((b - r) / delta) + 2)
            else:
                h = 60 * (((r - g) / delta) + 4)

            s = 0 if c_max == 0 else delta / c_max

            self._color = (h, s, c_max, a)

        else:
            assert isinstance(color, Sequence)
            assert len(color) in (3, 4)

            color = tuple(map(boundary_hue_based_color_models, range(4), color))

            self._color = color

    @property
    def rgba(self) -> ColorSequence:
        h, s, b, *a = self._color

        a = a[0] if a else 1

        h = h % 360
        c = b * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = b - c

        if 0 <= h < 60:
            r, g, b = c, x, 0
        elif 60 <= h < 120:
            r, g, b = x, c, 0
        elif 120 <= h < 180:
            r, g, b = 0, c, x
        elif 180 <= h < 240:
            r, g, b = 0, x, c
        elif 240 <= h < 300:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x

        return (
            int((r + m) * 255),
            int((g + m) * 255),
            int((b + m) * 255),
            int(a * 255)
        )