from typing import *

from overloadable import overloadable

__all__ = ["assertfunction"]


@overloadable
def assertfunction(*args) -> int:
    "This function works as dispatcher."
    return len(args)


@assertfunction.overload(1)
def assertfunction(check: Any, /) -> None:
    "This function implements assert check."
    assert check


@assertfunction.overload(2)
def assertfunction(check: Any, message: Any, /) -> None:
    "This function implements assert check, message."
    assert check, message
