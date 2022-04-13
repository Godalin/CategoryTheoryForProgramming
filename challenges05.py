from enum import Enum
from typing import *


# 4. Implement the Either generic type.


A = TypeVar('A')
B = TypeVar('B')


class Either(Generic[A, B]):
    class Tag(Enum):
        Left = 0
        Right = 1

    def __init__(self, tag: Tag, value: A | B):
        self.tag = tag
        self.value = value

    def __repr__(self):
        return f'Either({self.tag}, {self.value})'


def left(value: A) -> Either[A, B]:
    return Either(Either.Tag.Left, value)


def right(value: B) -> Either[A, B]:
    return Either(Either.Tag.Right, value)


print(left(1))
print(left(4))
print(left(True))
print(left(False))


# 5. Either is better then int with the 2 injections
def i(n: int): return n
def j(b: bool): return 0 if b else 1


def m(e: Either[int, bool]):
    """
    better: with m, we have
    i = m . left
    j = m . right
    """
    if e.tag == Either.Tag.Left:
        return e.value
    elif e.tag == Either.Tag.Right:
        return 0 if e.value else 1

# 7. other injections
def i1(n: int): return n if n < 0 else n + 2
def j1(b: bool): return 0 if b else 1


def m1(e: Either[int, bool]):
    if e.tag == Either.Tag.Left:
        n = e.value
        return n if n < 0 else n + 2
    elif e.tag == Either.Tag.Right:
        return 0 if e.value else 1