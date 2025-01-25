from typing import overload, Optional
from abc import abstractmethod, ABC
from copy import deepcopy

from ..typealias import ColorLike, ColorSequence

class BaseColor(ABC):

    _DEFAULT_COLOR: ColorLike

    @overload
    def __init__(self, color: Optional[ColorLike] = None) -> None: ...
    @overload
    def __init__(self, *args) -> None: ...
    def __init__(self, *args):
        len_args = len(args)
        if len_args == 0:
            self._color = self._DEFAULT_COLOR
        elif len_args == 1:
            self.color = args[0]
        else:
            self.color = args

    def copy(self) -> 'BaseColor':
        return deepcopy(self)

    @property
    @abstractmethod
    def color(self) -> ColorLike:
        pass

    @property
    @abstractmethod
    def rgba(self) -> ColorSequence:
        pass

    @property
    def rgb(self) -> ColorSequence:
        return self.rgba[0:3]