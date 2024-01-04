#!/usr/bin/env python3
'''
Simple module for strongly
typed python
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function that takes a float multiplier
    as argument and returns a function that
    multiplies a float by multiplier
    """

    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
