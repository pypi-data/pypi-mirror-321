from typing import Sequence

from ..base import BaseColor

from ..._utils.tools import boundary, boundary_hue_based_color_models

from ...typealias import ColorLike, ColorSequence

class HWB(BaseColor):

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

            self._color = (h, cmin, 1 - cmax, a)

        else:
            assert isinstance(color, Sequence)
            assert len(color) in (3, 4)

            color = tuple(map(boundary_hue_based_color_models, range(4), color))

            self._color = color

    @property
    def rgba(self) -> ColorSequence:
        h, w, b, *a = self._color

        a = a[0] if a else 1

        h = h % 360
        w = boundary(w, 1, 0)
        b = boundary(b, 1, 0)

        if w + b > 1:
            raise ValueError('whiteness + blackness must be <= 1')

        c = 1 - w - b
        x = c * (1 - abs((h / 60) % 2 - 1))

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
            int((r + w) * (1 - b) * 255),
            int((g + w) * (1 - b) * 255),
            int((b + w) * (1 - b) * 255),
            int(a * 255)
        )