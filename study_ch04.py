# python version: 3.9.1

"""ch04 Kleisli Category
"""


"""the Writer Category
"""

# * 这是一些具体的函数，它们都是接受一个参数
# * 并返回一个元组，其中第一个元素是计算结果，第二个元素是日志
# * 这些日志就是携带的额外的信息
# * 这些就是 Writer Category 的 morphisms


def toUpper(s: str) -> tuple[str, str]:
    return (s.upper(), "toUpper\n")


def toWords(s: str) -> tuple[str, str]:
    return (s.split(), "toWords\n")


def is_even(n: int) -> tuple[bool, str]:
    return (n % 2 == 0, "is even\n")


def negate(b: bool) -> tuple[bool, str]:
    return (not b, "negate\n")


def is_odd(n: int) -> tuple[bool, str]:
    r1, s1 = is_even(n)
    r2, s2 = negate(r1)
    return (r2, s1 + s2)


def WriterCompose(m1, m2):
    """the composition operation for Writer Category"""
    def composed(x):
        r1, s1 = m1(x)
        r2, s2 = m2(r1)
        return (r2, s1 + s2)
    return composed


def WriterIdentity(m):
    """the identity morphism for Writer Category"""
    return (m, "")


process = WriterCompose(toUpper, toWords)
print(process("hello world godalin, good morning")[1])
