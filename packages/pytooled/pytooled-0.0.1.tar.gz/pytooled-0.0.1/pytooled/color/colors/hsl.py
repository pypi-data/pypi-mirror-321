from typing import Sequence

from ..base import BaseColor

from ..._utils.tools import boundary_hue_based_color_models

from ...typealias import ColorLike, ColorSequence

class HSL(BaseColor):

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

            cmax = max(r, g, b)
            cmin = min(r, g, b)
            delta = cmax - cmin

            if delta == 0:
                h = 0
            elif cmax == r:
                h = (60 * ((g - b) / delta) + 360) % 360
            elif cmax == g:
                h = (60 * ((b - r) / delta) + 120) % 360
            elif cmax == b:
                h = (60 * ((r - g) / delta) + 240) % 360

            l = (cmax + cmin) / 2

            if delta == 0:
                s = 0
            else:
                s = delta / (1 - abs(2 * l - 1)) if l != 0 and l != 1 else delta / (cmax + cmin)

            self._color = (h, s, l, a)

        else:
            assert isinstance(color, Sequence)
            assert len(color) in (3, 4)

            color = tuple(map(boundary_hue_based_color_models, range(4), color))

            self._color = color

    @property
    def rgba(self) -> ColorSequence:
        h, s, l, *a = self._color

        a = a[0] if a else 1

        h = h / 60
        c = (1 - abs(2 * l - 1)) * s
        x = c * (1 - abs((h % 2) - 1))
        m = l - c / 2

        if 0 <= h < 1:
            r, g, b = c, x, 0
        elif 1 <= h < 2:
            r, g, b = x, c, 0
        elif 2 <= h < 3:
            r, g, b = 0, c, x
        elif 3 <= h < 4:
            r, g, b = 0, x, c
        elif 4 <= h < 5:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x

        return (
            int((r + m) * 255),
            int((g + m) * 255),
            int((b + m) * 255),
            int(a * 255)
        )