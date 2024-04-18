#!/usr/bin/env python3
""" takes a sequance and return first element"""
from typing import Sequence, Union, Any, Mapping, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ takes a sequance and return first element"""

    if key in dct:
        return dct[key]
    else:
        return default
