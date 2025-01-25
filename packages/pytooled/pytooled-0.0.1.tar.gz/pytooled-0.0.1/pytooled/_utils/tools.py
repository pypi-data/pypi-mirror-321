from typing import overload, Any

from ..tools import boundary
from ..typealias import Number

def boundary_color(c: Number) -> int:
    return boundary(int(c), 255, 0)

def boundary_percent(n: Number) -> float:
    return boundary(n / 100 if isinstance(n, int) else float(n), 1, 0)

def boundary_hue_based_color_models(i: int, c: Number) -> Number:
    if i == 0:
        return boundary(c, 360, 0)
    else:
        return boundary_percent(c)

@overload
def get_key_by_value(dictionary: dict, value: Any) -> Any: ...
@overload
def get_key_by_value(dictionary: dict, value: Any, default: Any) -> Any: ...
def get_key_by_value(*args) -> Any:
    dictionary = args[0]
    value = args[1]
    for key, v in dictionary.items():
        if v == value:
            return key
    if len(args) == 3:
        return args[2]
    raise KeyError(value)