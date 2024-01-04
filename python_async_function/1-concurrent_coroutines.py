#!/usr/bin/env python3
"""
Simple demostration of async
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Function that returns the list of
    all delays in ascending order
    '''
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)