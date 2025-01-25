from typing import Sequence

from ..base import BaseColor

from ..._utils.tools import boundary_percent

from ...typealias import ColorLike, ColorSequence

class CMYK(BaseColor):

    _DEFAULT_COLOR = (0, 0, 0, 0)

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

            k = 1 - max(r, g, b)

            if k == 1:
                self._color = (0, 0, 0, 1)
            else:
                self._color = (
                    ((1 - r - k) / (1 - k)),
                    ((1 - g - k) / (1 - k)),
                    ((1 - b - k) / (1 - k)),
                    k,
                    a
                )

        else:
            assert isinstance(color, Sequence)
            assert len(color) in (4, 5)

            color = tuple(map(boundary_percent, color))

            self._color = color

    @property
    def rgba(self) -> ColorSequence:
        c, m, y, k, *a = self._color

        a = a[0] if a else 1

        return (
            int((1 - c) * (1 - k) * 255),
            int((1 - m) * (1 - k) * 255),
            int((1 - y) * (1 - k) * 255),
            int(a * 255)
        )