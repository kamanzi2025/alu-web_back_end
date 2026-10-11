# Personal Data

This project covers how to handle Personally Identifiable Information (PII)
safely in a Python back end: redacting sensitive fields from log messages,
connecting to a database with credentials kept in environment variables, and
storing passwords as salted bcrypt hashes instead of plain text.

## Learning Objectives

- Examples of Personally Identifiable Information (PII)
- How to implement a log filter that obfuscates PII fields
- How to encrypt a password and check the validity of an input password
- How to authenticate to a database using environment variables

## Requirements

- Python 3.7 on Ubuntu 18.04 LTS
- Every file starts with `#!/usr/bin/env python3` and ends with a new line
- Code follows `pycodestyle` style (version 2.5)
- All files are executable
- Every module, class, function and method has a documentation string
- All functions and methods are type-annotated
- Dependencies: `mysql-connector-python` and `bcrypt`

## Tasks

| File | Description |
| ---- | ----------- |
| `filtered_logger.py` | `filter_datum` redacts field values in a log message with a single regex |
| `filtered_logger.py` | `RedactingFormatter` is a `logging.Formatter` that redacts the given fields |
| `filtered_logger.py` | `PII_FIELDS` and `get_logger` create the `user_data` logger that redacts PII |
| `filtered_logger.py` | `get_db` connects to MySQL using the `PERSONAL_DATA_DB_*` environment variables |
| `filtered_logger.py` | `main` reads every row of the `users` table and logs it with PII redacted |
| `encrypt_password.py` | `hash_password` returns a salted bcrypt hash of a password |
| `encrypt_password.py` | `is_valid` checks a password against its bcrypt hash |

## Environment variables

| Variable | Default |
| -------- | ------- |
| `PERSONAL_DATA_DB_USERNAME` | `root` |
| `PERSONAL_DATA_DB_PASSWORD` | empty string |
| `PERSONAL_DATA_DB_HOST` | `localhost` |
| `PERSONAL_DATA_DB_NAME` | none |
