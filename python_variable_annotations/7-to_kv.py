#!/usr/bin/env python3
'''
Simple module for strongly
typed python
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple (k, v^2) where v is the square of the int/float
    """
    return k, float(v ** 2)
