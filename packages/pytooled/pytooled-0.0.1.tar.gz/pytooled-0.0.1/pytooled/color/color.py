from os import environ
from typing import overload, Optional, Sequence, Callable

from .base import BaseColor

from .colors.rgb import RGB
from .colors.cmyk import CMYK
from .colors.hex import ishex, Hex
from .colors.ansi import isansi, Ansi
from .colors.name import isname, Name
from .colors.hexdec import ishexdec, HexDec

from .._utils.constants import COLOR_WITH_ALPHA
from .._utils.tools import boundary_color

from ..typealias import ColorLike, ColorSequence, LiteralComparisions, Number
from ..tools import name

def get_rgba(color: ColorLike) -> ColorSequence:
    if isinstance(color, BaseColor):
        return color.rgba
    return Color(color).rgba

def comparison(self: 'Color', op: LiteralComparisions, other: ColorLike, reversed: bool) -> bool:
    if reversed:
        self_rgba, other_rgba = get_rgba(other), self.rgba
    else:
        self_rgba, other_rgba = self.rgba, get_rgba(other)

    if get_alpha():
        return getattr(self_rgba, f'__{op}__')(other_rgba)
    return getattr(self_rgba[0:3], f'__{op}__')(other_rgba[0:3])

def operator(self: 'Color', other: ColorLike | None, with_other: bool, func: Callable) -> 'Color':
    if with_other:
        m = map(
            lambda cs, co: boundary_color(func(cs, co)),
            self.rgba if get_alpha() else self.rgb,
            get_rgba(other)
        )
    else:
        m = map(
            lambda cs: boundary_color(func(cs)),
            self.rgba if get_alpha() else self.rgb
        )

    return Color(m)

def get_alpha() -> bool:
    return environ[COLOR_WITH_ALPHA] == '1'

def set_alpha(boolean: bool) -> None:
    environ[COLOR_WITH_ALPHA] = '1' if boolean else '0'

environ[COLOR_WITH_ALPHA] = '1'

class Color(BaseColor):

    _DEFAULT_COLOR = (0, 0, 0, 0)

    @overload
    def __init__(self, color: Optional[ColorLike] = None) -> None: ...
    @overload
    def __init__(self, color: Optional[ColorLike], default: ColorLike) -> None: ...
    @overload
    def __init__(self, *args) -> None: ...
    @overload
    def __init__(self, *args, default: ColorLike) -> None: ...

    def __init__(self, *args, **kwargs) -> None:
        self.default = kwargs.pop('default', None)

        if kwargs:
            raise TypeError(
                f'{name(self)}.__init__() got an unexpected keyword arguments: '
                ', '.join(f"'{k}'" for k in kwargs.keys())
            )

        len_args = len(args)
        if len_args == 0:
            self.color = None
        elif len_args == 1:
            self.color = args[0]
        else:
            self.color = args

    @property
    def color(self) -> ColorLike | None:
        return self._color

    @color.setter
    def color(self, color: ColorLike | None) -> None:
        error = ValueError(f'invalid color value: {color!r}')

        def set_default():
            if self.default is not None:
                self._rgba = Color(self.default).rgba
            else:
                raise error

        self._color = color

        if isinstance(color, map):
            color = tuple(color)

        if color is None:
            self._rgba = self._DEFAULT_COLOR

        elif isinstance(color, BaseColor):
            try:
                self._rgba = color.rgba
            except:
                set_default()

        elif isinstance(color, int):
            try:
                self._rgba = HexDec(color).rgba
            except:
                set_default()

        elif isinstance(color, str):
            if ishex(color):
                self._rgba = Hex(color).rgba

            elif ishexdec(color):
                self._rgba = HexDec(color).rgba

            elif isname(color):
                self._rgba = Name(color).rgba

            elif isansi(color):
                self._rgba = Ansi(color).rgba

            else:
                set_default()

        elif isinstance(color, Sequence):
            if len(color) == 5:
                self._rgba = CMYK(color).rgba
            else:
                try:
                    self._rgba = RGB(color).rgba
                except:
                    set_default()

        else:
            set_default()

    @property
    def rgba(self) -> ColorSequence:
        return self._rgba

    def __copy__(self) -> 'Color':
        return Color(self._rgba)

    def __deepcopy__(self, memo: dict) -> 'Color':
        return Color(self._rgba)

    def __str__(self):
        return f'Color{self._rgba}'

    def __repr__(self):
        return self.__str__()

    def __bool__(self) -> bool:
        return any(self.rgba) if get_alpha() else any(self.rgb)

    def __len__(self) -> int:
        return 4

    def __list__(self) -> list:
        return list(self.rgba)

    def __tuple__(self) -> tuple:
        return self.rgba

    def __getitem__(self, index: int | slice) -> Number:
        return self.rgba[index]

    def __eq__(self, other: ColorLike):
        return comparison(self, 'eq', other, False)

    def __ne__(self, other: ColorLike):
        return comparison(self, 'ne', other, False)

    def __lt__(self, other: ColorLike):
        return comparison(self, 'lt', other, False)

    def __le__(self, other: ColorLike):
        return comparison(self, 'le', other, False)

    def __gt__(self, other: ColorLike):
        return comparison(self, 'gt', other, False)

    def __ge__(self, other: ColorLike):
        return comparison(self, 'ge', other, False)

    def __req__(self, other: ColorLike):
        return comparison(other, 'eq', self, True)

    def __rne__(self, other: ColorLike):
        return comparison(self, 'ne', other, True)

    def __rlt__(self, other: ColorLike):
        return comparison(self, 'lt', other, True)

    def __rle__(self, other: ColorLike):
        return comparison(self, 'le', other, True)

    def __rgt__(self, other: ColorLike):
        return comparison(self, 'gt', other, True)

    def __rge__(self, other: ColorLike):
        return comparison(self, 'ge', other, True)

    def __add__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a + b)

    def __sub__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a - b)

    def __mul__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a * b)

    def __truediv__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a / b)

    def __floordiv__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a // b)

    def __mod__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a % b)

    def __pow__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a ** b)

    def __and__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a & b)

    def __or__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a | b)

    def __xor__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a ^ b)

    def __lshift__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a << b)

    def __rshift__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a >> b)

    def __radd__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : b + a)

    def __rsub__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : b - a)

    def __rmul__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : b * a)

    def __rtruediv__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : b / a)

    def __rfloordiv__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : b // a)

    def __rmod__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : b % a)

    def __rpow__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : b ** a)

    def __rand__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : b & a)

    def __ror__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : b | a)

    def __rxor__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : b ^ a)

    def __rlshift__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : b << a)

    def __rrshift__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : b >> a)

    def __iadd__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a + b)

    def __isub__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a - b)

    def __imul__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a * b)

    def __itruediv__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a / b)

    def __ifloordiv__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a // b)

    def __imod__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a % b)

    def __ipow__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a ** b)

    def __iand__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a & b)

    def __ior__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a | b)

    def __ixor__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a ^ b)

    def __ilshift__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a << b)

    def __irshift__(self, other: ColorLike):
        return operator(self, other, True, lambda a, b : a >> b)

    def __neg__(self):
        return operator(self, None, False, lambda c : 255 - c)