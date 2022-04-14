import math
from CategoryTheoryLib import Optional, Either, left, right
from typing import Any, TypeVar, Tuple


# 1. isomorphism between Maybe and Either
def optional_to_either(
    o: Optional[Any]
) -> Either[None, Any]:
    if o.isValid():
        return right(o.value())
    else:
        return left(None)


def either_to_optional(
    e: Either[None, Any]
) -> Optional[Any]:
    if e.isRight():
        return Optional(e.value())
    else:
        return Optional()


# 2. implement the area function
class Shape:
    ...


class Circle(Shape):
    r: float

    def __init__(self, r: float):
        self.r = r


class Rect(Shape):
    d: float
    w: float

    def __init__(self, d: float, w: float):
        self.d = d
        self.w = w


def area(s: Shape):
    match s:
        case Circle(r=r):
            return r ** 2 * math.pi
        case Rect(d=d, w=w):
            return d * w
        # add square
        case Square(a=a):
            return a ** 2


print(area(Circle(2)))
print(area(Rect(2, 3)))


# 3. add a circ function
def circ(s: Shape):
    match s:
        case Circle(r=r):
            return 2 * r * math.pi
        case Rect(d=d, w=w):
            return 2 * (d + w)
        # add square
        case Square(a=a):
            return 4 * a


print(circ(Circle(2)))
print(circ(Rect(2, 3)))


# 4. add a square class
class Square(Shape):
    a: float

    def __init__(self, a: float):
        self.a = a


print(area(Square(2)))
print(circ(Square(2)))


# 5. show: a + a = 2 * a
A = TypeVar('A')
A_Plus_A = Either[A, A]
A_Times_2 = Tuple[bool, A]


def APA_to_AT2(
    e: A_Plus_A
) -> A_Times_2:
    if e.tag == Either.Tag.Left:
        return (False, e.value())
    else:
        return (True, e.value())


def AT2_to_APA(
    t: A_Times_2
) -> A_Plus_A:
    b, v = t
    if b:
        return right(v)
    else:
        return left(v)
