#!/usr/bin/env python3
"""Regex-ing Module"""

import re
import logging


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields


    def format(self, record: logging.LogRecord) -> str:
        """Format the record"""
        mes = super().format(record)
        return filter_datum(self.fields, RedactingFormatter.REDACTION, 
                            mes, RedactingFormatter.SEPARATOR )


def filter_datum(fields: list[str, str], redaction: str, message: str,
                 separator: str) -> str:
    """returns the log message obfuscated:"""
    pattern = f"({'|'.join(map(re.escape, fields))})=[^{separator}]*"
    return re.sub(pattern, lambda m: f" {m.group(1)}={redaction}", message)



def get_logger() -> logging.Logger:
    logger = logging.getLogger("user_data")
    logger.setLevel = logging.INFO
    stream = logging.StreamHandler(format=RedactingFormatter)
    logger.addHandler(stream)
    logger.propagate = False
    return logger
