# Python - Async Comprehension

This project explores asynchronous generators and async comprehensions in
Python 3 with the `asyncio` library. Every function and coroutine is fully
type-annotated, checked with `mypy` and styled according to `pycodestyle`
(version 2.5).

## Learning Objectives

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Requirements

- Python 3.7 on Ubuntu 18.04 LTS
- Every file starts with `#!/usr/bin/env python3` and ends with a new line
- Code follows `pycodestyle` style (version 2.5)
- All files are executable
- Every module, function and coroutine has a documentation string
- All functions and coroutines are type-annotated

## Tasks

| File | Description |
| ---- | ----------- |
| `0-async_generator.py` | `async_generator() -> AsyncGenerator[float, None]` loops 10 times, waiting 1 second and then yielding a random float between 0 and 10 each time |
| `1-async_comprehension.py` | `async_comprehension() -> List[float]` collects the 10 random numbers from `async_generator` with an async comprehension |
| `2-measure_runtime.py` | `measure_runtime() -> float` runs `async_comprehension` four times in parallel with `asyncio.gather` and returns the total runtime |

## Why `measure_runtime` takes about 10 seconds

Each `async_comprehension` call takes about 10 seconds (10 waits of 1
second). Because the four calls run concurrently with `asyncio.gather`,
their waits overlap, so the total runtime is about 10 seconds rather
than 40.

## Usage

```bash
$ cat 2-main.py
#!/usr/bin/env python3
import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime

print(asyncio.run(measure_runtime()))
$ ./2-main.py
10.021936893463135
```
