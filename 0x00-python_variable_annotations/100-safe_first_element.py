#!/usr/bin/env python3
""" takes a sequance and return first element"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ takes a sequance and return first element"""
    if lst:
        return lst[0]
    else:
        return None
