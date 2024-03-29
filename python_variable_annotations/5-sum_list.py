#!/usr/bin/env python3
'''
Simple module for strongly
typed python
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of floats in the input list
    """
    return sum(input_list)
