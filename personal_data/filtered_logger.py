#!/usr/bin/env python3
"""This module filters, redacts and logs personal data from a database."""
import logging
import os
import re
from typing import List

import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Return the log message with the values of the given fields redacted."""
    pattern = r'({})=.*?{}'.format('|'.join(fields), re.escape(separator))
    return re.sub(pattern, r'\1={}{}'.format(redaction, separator), message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class that hides PII fields in log records."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        """Initialize the formatter with the list of fields to redact."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record and redact the configured PII fields."""
        message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION, message,
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Return the user_data logger that redacts the PII fields."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Return a connection to the database using environment variables."""
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")
    return mysql.connector.connection.MySQLConnection(
        user=username, password=password, host=host, database=db_name)


def main() -> None:
    """Read every row of the users table and log it with PII redacted."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    columns = [column[0] for column in cursor.description]
    logger = get_logger()
    for row in cursor:
        message = "; ".join("{}={}".format(col, value)
                            for col, value in zip(columns, row)) + ";"
        logger.info(message)
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
