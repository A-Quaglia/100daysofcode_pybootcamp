from functools import reduce
from typing import List, Union

num_array = List[Union[float, int]]
ops_result = Union[float, int]


def apply_ops(func, *args: num_array) -> ops_result:
    return reduce(func, *args)


def add(*args: num_array) -> ops_result:
    return apply_ops(lambda a, b: a + b, *args)


def sub(*args: num_array) -> ops_result:
    return apply_ops(lambda a, b: a - b, *args)


def mul(*args: num_array) -> ops_result:
    return apply_ops(lambda a, b: a * b, *args)


def div(*args: num_array) -> ops_result:
    return apply_ops(lambda a, b: a / b, *args)

