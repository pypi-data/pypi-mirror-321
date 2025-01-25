from typing import TYPE_CHECKING, Sequence, Union, SupportsD

if TYPE_CHECKING:
    from ..color.color import Color
    from ..color.base import BaseColor

Number = int | float
ColorLike = Union['Color', 'BaseColor', str, int, Sequence[Number]]
ColorRGBA = tuple[int, int, int, int]
ColorRGB = tuple[int, int, int]