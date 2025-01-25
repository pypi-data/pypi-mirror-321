from typing import *

from overloadable import overloadable

__all__ = ["assertfunction"]


@overloadable
def assertfunction(*args: Any) -> int:
    "This function works as dispatcher."
    if len(args) < 1:
        raise TypeError(
            "An assertion requires at least 1 positional argument (0 given)."
        )
    if len(args) > 2:
        raise TypeError(
            "An assertion takes at most 2 positional arguments (%s given)." % len(args)
        )
    return len(args)


@assertfunction.overload(1)
def assertfunction(check: Any, /) -> None:
    "This function implements assert check."
    assert check


@assertfunction.overload(2)
def assertfunction(check: Any, message: Any, /) -> None:
    "This function implements assert check, message."
    assert check, message
