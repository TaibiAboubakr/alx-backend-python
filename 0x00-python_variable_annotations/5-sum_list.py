#!/usr/bin/env python3
""" takes a list input_list of floats as argument
and returns their sum as a float. """
from typing import List


def sum_list(float_list: List[float]) -> float:
    """  takes a list input_list of floats as argument and
returns their sum as a float. """
    n = sum(map(float, float_list))
    return n
