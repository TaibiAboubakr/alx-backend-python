#!/usr/bin/env python3
"""  task_wait_n """

import asyncio
from typing import List
task_wait_random  = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List:
    """  task_wait_n """
    delays = []
    for _ in range(n):
        delays.append(task_wait_random(max_delay))
    wait_delays = await asyncio.gather(* delays)
    return sorted(wait_delays)
