# Python - Async

This project introduces asynchronous programming in Python 3 with the
`async` / `await` syntax and the `asyncio` library. Every function and
coroutine is fully type-annotated, checked with `mypy` and styled according
to `pycodestyle` (version 2.5).

## Learning Objectives

- `async` and `await` syntax
- How to execute an async program with `asyncio`
- How to run concurrent coroutines
- How to create `asyncio` tasks
- How to use the `random` module

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
| `0-basic_async_syntax.py` | `wait_random(max_delay: int = 10) -> float` waits a random delay between 0 and `max_delay` seconds and returns it |
| `1-concurrent_coroutines.py` | `wait_n(n: int, max_delay: int) -> List[float]` runs `wait_random` `n` times concurrently and returns the delays in ascending order, without sorting |
| `2-measure_runtime.py` | `measure_time(n: int, max_delay: int) -> float` measures the total runtime of `wait_n` and returns `total_time / n` |
| `3-tasks.py` | `task_wait_random(max_delay: int) -> asyncio.Task` returns an `asyncio.Task` wrapping `wait_random` |
| `4-tasks.py` | `task_wait_n(n: int, max_delay: int) -> List[float]` is like `wait_n` but uses `task_wait_random` |

## Usage

```bash
$ cat 1-main.py
#!/usr/bin/env python3
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
$ ./1-main.py
[0.9693881173832354, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
```
