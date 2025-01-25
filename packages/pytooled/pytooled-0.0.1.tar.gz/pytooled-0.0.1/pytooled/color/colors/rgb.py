from typing import Sequence

from ..base import BaseColor

from ..._utils.tools import boundary_color

from ...typealias import ColorLike, ColorSequence

class RGB(BaseColor):

    _DEFAULT_COLOR = (0, 0, 0)

    @property
    def color(self) -> ColorSequence:
        return self._color

    @color.setter
    def color(self, color: ColorLike) -> None:
        if isinstance(color, BaseColor):
            self._color = color.rgba

        else:
            assert isinstance(color, Sequence)
            assert len(color) in (3, 4)

            color = tuple(map(boundary_color, color))

            self._color = color

    @property
    def rgba(self) -> ColorSequence:
        if len(self._color) == 3:
            return self._color + (255,)
        return self._color