#!/usr/bin/env python3
'''
Simple module for strongly
typed python
'''


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function that returns a list of tuples,
    where each tuple contains an element from the input list
    and its corresponding length
    """

    return [(i, len(i)) for i in lst]
