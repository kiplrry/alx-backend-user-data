#!/usr/bin/env python3
"""Regex-ing Module"""

import re


def filter_datum(fields: list[str, str], redaction: str, message: str,
                 separator: str) -> str:
    """returns the log message obfuscated:"""
    pattern = f"({'|'.join(map(re.escape, fields))})=[^{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
