#!/usr/bin/env python3
"""
Simple demostration of async
"""
import asyncio
import time
from typing import List


wait_n = __import__('1-concurrent_coroutines.py').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''
    Function that returns total execution time for
    '''
    start_time = time.perf.counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time
    avg_time = total_time / n
    return avg_time
