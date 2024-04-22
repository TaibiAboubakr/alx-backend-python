#!/usr/bin/env python3
import asyncio
import random
""" wait random """


async def wait_random(max_delay : int=10) -> float:
    """ wait random """
    wait_delay = random.uniform(0, max_delay)
    await asyncio.sleep(wait_delay)
    return wait_delay
