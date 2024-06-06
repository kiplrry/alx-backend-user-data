#!/usr/bin/env python3
"""
Session auth implementation
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """Session Authntication class

    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates session

        :param user_id: user id, defaults to None
        :type user_id: str, optional
        :return: session
        :rtype: str
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ that returns a User ID based on a Session ID

        :param session_id: Session id, defaults to None
        :type session_id: str, optional
        :return: user
        :rtype: str
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id, None)
