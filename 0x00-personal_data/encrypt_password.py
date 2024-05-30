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
