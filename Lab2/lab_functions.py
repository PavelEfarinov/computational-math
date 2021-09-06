from math import log, sin


def function_1(x):
    return x * x - abs(x + 1) / (x + 1) - 1


def function_2(x):
    return 1 / x


def function_3(x):
    return log(x)


def function_4(x):
    return sin(x) / x


def calcLeft(left, right):
    return left


def calcRight(left, right):
    return right


def calcMiddle(left, right):
    return (right + left) / 2
