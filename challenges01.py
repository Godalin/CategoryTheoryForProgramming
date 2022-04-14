from typing import TypeVar, Callable

A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')


def id(x: A) -> A:
    return x


def compose(
    g: Callable[[B], C],
    f: Callable[[A], B]
) -> Callable[[A], C]:
    return lambda x: g(f(x))
