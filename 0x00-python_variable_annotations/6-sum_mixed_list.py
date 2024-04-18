#!/usr/bin/env python3
""" takes a list mxd_lst of integers and floats
returns their sum as a float """
from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """  takes a list mxd_lst of integers and floats
    returns their sum as a float """
    n = sum(mxd_lst)
    return n
