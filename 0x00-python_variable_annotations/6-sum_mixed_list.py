#!/usr/bin/env python3
""" takes a list mxd_lst of integers and floats
returns their sum as a float """
from typing import List
from typing import Union


def sum_mixed_list(int_float_list: List[Union[float, int]]) -> float:
    """  takes a list mxd_lst of integers and floats
    returns their sum as a float """
    n = sum(map(float, int_float_list))
    return n
