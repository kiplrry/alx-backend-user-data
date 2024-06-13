#!/usr/bin/env python3
"""Auth implementation"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """hashes a password"""
    if password is None or not isinstance(password, str):
        return
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def _generate_uuid() -> str:
    """generates uuids

    :return: uuid
    :rtype: str
    """
    return str(uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """validates a login"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode(), user.hashed_password)

    def create_session(self, email: str) -> str:
        """creates session"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return
        uuid = _generate_uuid()
        self._db.update_user(user.id, session_id=uuid)
        return uuid

    def get_user_from_session_id(self, session_id: str) -> User:
        """gets user using session id"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """destroys user session"""
        try:
            user = self._db.find_user_by(user_id=user_id)
            self._db.update_user(user.id, session_id=None)
            return None
        except NoResultFound:
            pass
