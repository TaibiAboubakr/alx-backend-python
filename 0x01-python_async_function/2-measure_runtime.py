#!/usr/bin/env python3
import asyncio
import time

"""  Measure the runtime  """
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """  Measure the runtime """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return ((time.time() - start_time) / n)
