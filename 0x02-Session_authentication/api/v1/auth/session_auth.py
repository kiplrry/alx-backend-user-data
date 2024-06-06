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
        """ returns a User ID based on a Session ID

        :param session_id: Session id, defaults to None
        :type session_id: str, optional
        :return: user
        :rtype: str
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None):
        """returns a User instance based on a cookie value

        :param request: Request , defaults to None
        :type request: Request, optional
        """
        if request is None:
            return None
        session_id = self.session_cookie(request=request)
        if session_id is None:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)

    def destroy_session(self, request=None):
        """Destroys the user session

        :param request: request object, defaults to None
        :type request: _type_, optional
        """
        if request is None:
            return False
        sess_cookie = self.session_cookie(request)
        if sess_cookie is None:
            return False
        user = self.user_id_for_session_id(sess_cookie)
        if user is None:
            return False
        self.user_id_by_session_id.pop(sess_cookie)
        return True
