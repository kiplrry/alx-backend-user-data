#!/usr/bin/env python3
"""
Basic auth implementation
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """BasicAuth

    :param Auth: An implementatin of Basic Authentication
    :type Auth: Auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extrac Basic auth

        :param authorization_header: Auth header
        :type authorization_header: str
        :return: the header or None
        :rtype: str
        """
        if authorization_header is None or\
                not isinstance(authorization_header, str):
            return None
        arrs = authorization_header.split(' ')
        if len(arrs) != 2:
            return None

        if arrs[0] != 'Basic':
            return None

        return arrs[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Decode basic auth

        :param base64_authorization_header: base64 str
        :type base64_authorization_header: str
        :return: None or decoded str
        :rtype: str
        """
        ba = base64_authorization_header
        if ba is None or not isinstance(ba, str):
            return None
        try:
            decode = base64.decodebytes(ba.encode())
            return decode.decode()
        except BaseException:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """get credentials

        :param self: decoded auth
        :type self: str
        :param str: returns email and password
        :type str: tuple
        """
        da = decoded_base64_authorization_header
        if da is None or not isinstance(da, str):
            return None, None
        arrs = da.split(':')
        if len(arrs) != 2:
            return None, None
        return tuple(arrs)

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """get user from the credentials provided

        :param user_email: users email
        :type self: str
        :param user_pwd: users pass
        :type self: str
        :returns: User
        """
        if user_email is None or user_pwd is None\
            or not isinstance(user_pwd, str)\
                or not isinstance(user_email, str):
            return None

        users = None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """retrieves the User instance for a request"""
        auth_header = self.authorization_header(request)
        encoded = self.extract_base64_authorization_header(auth_header)
        decoded = self.decode_base64_authorization_header(encoded)
        email, password = self.extract_user_credentials(decoded)
        user = self.user_object_from_credentials(email, password)
        return user
