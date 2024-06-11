#!/usr/bin/env python3
"""Auth implementation"""
import bcrypt
from db import DB
from typing import TypeVar
from sqlalchemy.orm.exc import NoResultFound
User = TypeVar('User')


def _hash_password(password: str) -> bytes:
    """hashes a password"""
    if password is None or not isinstance(password, str):
        return
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a user"""
        # if email is None or not isinstance(email, str) or\
        #         password is None or not isinstance(password, str):
        #     return
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
