# 0x01-python_async_function

This directory contains Python scripts demonstrating asynchronous programming concepts using asyncio in Python.

## Files:
0-basic_async_syntax.py: This script introduces the basic syntax and concepts of asynchronous programming in Python using asyncio. It includes an asynchronous coroutine wait_random that waits for a random delay and returns it.
1-concurrent_coroutines.py: This script demonstrates the execution of multiple coroutines concurrently using asyncio. It includes an asynchronous coroutine wait_n that spawns multiple instances of the wait_random coroutine with the specified maximum delay and returns the sorted list of delays.
2-measure_runtime.py: This script measures the runtime of the wait_n coroutine and calculates the average time taken for each call. It includes an asynchronous coroutine measure_time that measures the runtime of the wait_n coroutine and returns the average time taken per call.