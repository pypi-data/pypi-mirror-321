from typing import Any, Optional

def asserter(

    condition: bool,
    exception: Optional[BaseException | str] = None,
    traceback: Optional[BaseException] = None

    ) -> None:

    if not condition:

        if exception is None:
            assert_error = AssertionError
        elif isinstance(exception, str):
            assert_error = AssertionError(exception)
        else:
            assert_error = None

        if traceback is not None:
            if assert_error:
                raise assert_error from traceback
            raise exception from traceback

        if assert_error:
            raise assert_error
        raise exception

def boundary(value: Any, nmax: Any, nmin: Any) -> Any:
    return min(nmax, max(nmin, value))

def bounds(value: Any, nmax: Any, nmin: Any) -> bool:
    return nmin <= value <= nmax

def name(obj: Any, abs: bool = False) -> str:
    module, name = obj.__class__.__module__, obj.__class__.__name__
    if module != '__main__' and abs:
        return f'{module}.{name}'
    return name