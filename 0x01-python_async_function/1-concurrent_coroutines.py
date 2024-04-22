#!/usr/bin/env python3
import asyncio

"""  execute multiple coroutines at the same time with async """
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """  execute multiple coroutines at the same time with async """
    delays = []
    for _ in range(n):
        delays.append(wait_random(max_delay))
    wait_delays = await asyncio.gather(* delays)
    return sorted(wait_delays)
