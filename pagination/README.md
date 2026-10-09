# Pagination

This project explores different ways to paginate a large dataset in Python 3:
simple page/page-size pagination, hypermedia pagination that returns
navigation metadata, and deletion-resilient hypermedia pagination that keeps
working when rows are removed between requests. The data comes from the
`Popular_Baby_Names.csv` file, which must be placed in the working directory
(it is not included in this repository).

## Learning Objectives

- How to paginate a dataset with simple `page` and `page_size` parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Requirements

- Python 3.7 on Ubuntu 18.04 LTS
- Every file starts with `#!/usr/bin/env python3` and ends with a new line
- Code follows `pycodestyle` style (version 2.5)
- All files are executable
- Every module, class, function and method has a documentation string
- All functions and methods are type-annotated

## Tasks

| File | Description |
| ---- | ----------- |
| `0-simple_helper_function.py` | `index_range(page, page_size)` returns a tuple with the start and end indexes of a 1-indexed page |
| `1-simple_pagination.py` | `Server.get_page(page, page_size)` validates its arguments and returns the matching page of the dataset (an empty list when out of range) |
| `2-hypermedia_pagination.py` | `Server.get_hyper(page, page_size)` returns a page plus `page_size`, `page`, `next_page`, `prev_page` and `total_pages` |
| `3-hypermedia_del_pagination.py` | `Server.get_hyper_index(index, page_size)` returns a page starting at `index` that skips deleted rows, plus the `next_index` to query |
