#!/usr/bin/env python3
"""Auth implementation"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


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
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email}  already exists')
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str):
        """validates a login"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                valid = bcrypt.checkpw(password.encode(), user.hashed_password)
                return valid
        except Exception:
            return False
