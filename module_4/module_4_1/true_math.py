from math import inf


def divide(first, second):
    if second == 0:
        return inf.__float__()
    else:
        return first / second
