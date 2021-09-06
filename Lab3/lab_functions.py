from math import sin, cos, sqrt, e

from Lab3.FunctionWrapper import FunctionWrapper
from Lab3.UserExceptions import LimitSignException


def get_function_circle():
    fw = FunctionWrapper()
    fw.get_value = lambda x, y: x ** 2 + y ** 2 - 4
    fw.df_dx = lambda x: 2 * x
    fw.df_dy = lambda y: 2 * y
    fw.get_y_from_x = lambda x: ((sqrt(4 - x ** 2), -sqrt(4 - x ** 2)) if abs(x) <= 2 else None)
    return fw


def get_function_e():
    fw = FunctionWrapper()
    fw.get_value = lambda x, y: e ** ((x ** 5) / 3000) - 1 - y
    fw.df_dx = lambda x: e ** ((x ** 5) / 3000) / 600 * x ** 4
    fw.df_dy = lambda y: -1
    fw.get_y_from_x = lambda x: e ** ((x ** 5) / 3000) - 1
    return fw


def get_function_parabolic():
    fw = FunctionWrapper()
    fw.get_value = lambda x, y: (x ** 2) - y - 1
    fw.get_y_from_x = lambda x: x ** 2 - 1
    fw.df_dx = lambda x: 2 * x
    fw.df_dy = lambda y: -1
    return fw


def get_function_sinusoid():
    fw = FunctionWrapper()
    fw.get_value = lambda x, y: 2 * sin(x / 2) - y
    fw.get_y_from_x = lambda x: 2 * sin(x / 2)
    fw.df_dx = lambda x: cos(x / 2)
    fw.df_dy = lambda y: -1
    return fw


def get_function_polynomial():
    fw = FunctionWrapper()
    fw.get_value = lambda x, y: (x / 4) ** 7 - 5 * (x / 4) ** 5 + 5 * (x / 4) ** 3 - y
    fw.get_y_from_x = lambda x: (x / 4) ** 7 - 5 * (x / 4) ** 5 + 5 * (x / 4) ** 3
    fw.df_dx = lambda x: 7 * (x / 4) ** 6 - 25 * (x / 4) ** 4 + 15 * (x / 4) ** 2
    fw.df_dy = lambda y: -1
    return fw


def bisection_method(left: float, right: float, function: FunctionWrapper, epsilon: float,
                     iteration_limit=1e6):
    left, right = set_proper_order(left, right)
    i = 0
    if function.get_y_from_x(left) == 0:
        return left, 0, 0
    if function.get_y_from_x(right) == 0:
        return right, 0, 0
    if sign(function.get_y_from_x(right)) == sign(function.get_y_from_x(left)):
        raise LimitSignException
    dx = (right - left) / 2
    current_x = left + dx
    while right - left > epsilon and i < iteration_limit:
        dx = (right - left) / 2
        current_x = left + dx
        if sign(function.get_y_from_x(current_x)) != sign(function.get_y_from_x(left)):
            right = current_x
        else:
            left = current_x
        i += 1
    return current_x, function.get_y_from_x(current_x), i


def secant_method(left: float, right: float, function: FunctionWrapper, epsilon: float, iteration_limit=1e6):
    i = 0
    if function.get_y_from_x(left) == 0:
        return left, 0, 0
    if function.get_y_from_x(right) == 0:
        return right, 0, 0
    if sign(function.get_y_from_x(left)) == sign(function.get_y_from_x(right)):
        raise LimitSignException

    x0, x1 = left, right
    x2 = x0
    while abs(x0 - x1) >= epsilon and i < iteration_limit and sign(function.get_y_from_x(x2)) != 0:
        # try:
        x2 = x1 - function.get_y_from_x(x1) * (x1 - x0) / float(
            function.get_y_from_x(x1) - function.get_y_from_x(x0))
        if sign(function.get_y_from_x(x0)) == sign(function.get_y_from_x(x2)):
            x0, x1 = x1, x2
        else:
            x0, x1 = x0, x2
        # except Exception:
        #     raise NoRootsException
        i += 1
    return x2, function.get_y_from_x(x2), i


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def set_proper_order(x1: float, x2: float):
    if x1 > x2:
        return x2, x1
    return x1, x2
