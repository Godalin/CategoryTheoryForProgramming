from typing import Any, Callable


class Container(type):
    def __getitem__(self, _):
        ...


class Optional(metaclass=Container):
    """Optional is the Container of either None or a value

    metaclass=Container is used to make Optional class can be looked like a
    container
    """

    def __init__(self, value={}):
        self.__isValid = True
        self.__value = value
        if value is self.__init__.__defaults__[0]:
            self.__isValid = False
            # print("default value")
        else:
            self.__value = value
            # print("setted value", self.value)

    def isValid(self):
        return self.__isValid

    def value(self):
        return self.__value

    def __repr__(self) -> str:
        if self.__isValid:
            return f"Optional({str(self.__value)})"
        else:
            return f"Optional()"


def safe_root(x: float) -> Optional[float]:
    """save version of the sqrt function"""
    return Optional() if x < 0 else Optional(x ** 0.5)


print(safe_root(2))
print(safe_root(-4))


def OptionalCompose(
    m1: Callable[[Any], Optional[Any]],
    m2: Callable[[Any], Optional[Any]]
) -> Callable[[Any], Optional[Any]]:

    def _(x: Any) -> Optional[Any]:
        r1 = m1(x)
        if r1.isValid():
            r2 = m2(r1.value())
            return r2
        else:
            return r1
    return _


def OptionalIdentity(
    v: Any
) -> Optional[Any]:
    return Optional(v)


def safe_reciprocal(x: float) -> Optional[float]:
    """safe version of the reciprocal function"""
    return Optional() if x == 0 else Optional(1 / x)


safe_root_reciprocal = OptionalCompose(safe_root, safe_reciprocal)


print(safe_root_reciprocal(2))
print(safe_root_reciprocal(0))
print(safe_root_reciprocal(-12))
