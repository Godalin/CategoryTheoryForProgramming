from typing import *


Vector = List[float | int]


class Eq:
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, t: type):
        self.type = t


def dependent_type(x: str) -> List[float]:
    ...


def scale(x: float, v: Vector) -> Vector:
    return [x * i for i in v]


def dt(x: int | float) -> type:
    if x % 2 == 0:
        return int
    else:
        return float


T = TypeVar('T')


def some_function(x: int | float) -> dt(x):
    return dt(x)
