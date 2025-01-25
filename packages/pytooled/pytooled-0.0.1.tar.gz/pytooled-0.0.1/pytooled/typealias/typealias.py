from typing import TYPE_CHECKING, Sequence, Union, Literal

if TYPE_CHECKING:
    from ..color.color import Color
    from ..color.base import BaseColor

Number = int | float

LiteralComparision = Literal['eq', 'ne', 'lt', 'le', 'gt', 'ge']
LiteralReverseComparision = Literal['req', 'rne', 'rlt', 'rle', 'rgt', 'rge']
LiteralComparisions = Literal[LiteralComparision, LiteralReverseComparision]

ColorSequence = Sequence[int]
ColorHex = str | int
ColorAnsi = str | int
ColorName = str
ColorLike = Union['Color', 'BaseColor', str, int, ColorSequence]