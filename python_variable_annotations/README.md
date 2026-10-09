# Python - Variable Annotations

This project introduces type annotations in Python 3. Each file defines a
small, fully annotated function or variable, checked with `mypy` and styled
according to `pycodestyle` (version 2.5).

## Learning Objectives

- Type annotations in Python 3
- How to use type annotations to specify function signatures and variable types
- Duck typing
- How to validate code with `mypy`

## Requirements

- Python 3.7 on Ubuntu 18.04 LTS
- Every file starts with `#!/usr/bin/env python3` and ends with a new line
- Code follows `pycodestyle` style (version 2.5)
- All files are executable
- Every module and function has a documentation string

## Tasks

| File | Description |
| ---- | ----------- |
| `0-add.py` | `add(a: float, b: float) -> float` returns the sum of two floats |
| `1-concat.py` | `concat(str1: str, str2: str) -> str` concatenates two strings |
| `2-floor.py` | `floor(n: float) -> int` returns the floor of a float |
| `3-to_str.py` | `to_str(n: float) -> str` returns the string form of a float |
| `4-define_variables.py` | Defines annotated variables `a`, `pi`, `i_understand_annotations` and `school` |
| `5-sum_list.py` | `sum_list(input_list: List[float]) -> float` sums a list of floats |
| `6-sum_mixed_list.py` | `sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float` sums ints and floats |
| `7-to_kv.py` | `to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]` returns `(k, v ** 2)` |
| `8-make_multiplier.py` | `make_multiplier(multiplier: float) -> Callable[[float], float]` returns a multiplier function |
| `9-element_length.py` | `element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]` pairs each element with its length |
