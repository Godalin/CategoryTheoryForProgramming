def memorize(f):
    dic = {}

    def inner(x):
        nonlocal dic
        if x in dic:
            return dic[x]
        else:
            fx = f(x)
            dic[x] = fx
            return fx
    return inner


def same_(x: bool) -> bool: return x
def diff_(x: bool) -> bool: return not x
def true_(_: bool) -> bool: return True
def fals_(_: bool) -> bool: return False
