#!/usr/bin/env python3
"""Auth implementation"""
import bcrypt
from db import DB
from typing import TypeVar
from sqlalchemy.exc import NoResultFound
User = TypeVar('User')


def _hash_password(password: str) -> bytes:
    """hashes a password"""
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a user"""
        if email is None or not isinstance(email, str) or\
                password is None or not isinstance(password, str):
            return
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            hashed = _hash_password(password)
        user = self._db.add_user(email, hashed)
        return user
