#!/usr/bin/env python3
""" takes list of list and returns a tuple of each list with its len """
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ takes list of list and returns a tuple of each list with its len """
    return [(i, len(i)) for i in lst]
