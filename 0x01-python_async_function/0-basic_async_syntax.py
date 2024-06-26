#!/usr/bin/env python3
""" wait random """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ wait random """
    wait_delay = random.uniform(0, max_delay)
    await asyncio.sleep(wait_delay)
    return wait_delay
