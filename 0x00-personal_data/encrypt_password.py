#!/usr/bin/env python3
"""Encrypting passwords """

from typing import ByteString
import bcrypt


def hash_password(password: str) -> bytes:
    """
    expects one string argument name password
    and returns a salted, hashed password, which is a byte string.
    """
    passw = password.encode()
    hashpwd = bcrypt.hashpw(passw, bcrypt.gensalt())
    return hashpwd


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
        Validates whether the provided password matches the hashed password.

        Args:
                hashed_password (bytes): A byte string representing
                the salted, hashed password.
                password (str): A string containing the plain text
                password to be validated.

        Returns:
                bool: True if the provided password matches the hashed
                password, False otherwise.
    """
    passw = password.encode()
    if bcrypt.checkpw(passw, hashed_password):
        return True
    return False
