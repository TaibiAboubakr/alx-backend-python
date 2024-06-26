#!/usr/bin/env python3
""" that takes a float multiplier as argument
returns a function that multiplies a float by multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ takes a float multiplier as argument
returns a function that multiplies a float by multiplier """
    def multiplier_func(x: float) -> float:
        """ multiplies a float"""
        return x * multiplier
    return multiplier_func
