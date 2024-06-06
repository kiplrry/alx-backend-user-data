#!/usr/bin/env python3
"""
Authorization module implementation
"""
from flask import request
from typing import List, TypeVar
User = TypeVar('User')


class Auth:
    """Authorization Module
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth

        :param path: str
        :type path: str
        :param excluded_paths: excluded paths
        :type excluded_paths: List[str]
        :return: bool
        :rtype: bool
        """
        if not isinstance(path, str) or\
                not isinstance(excluded_paths, list):
            return True

        if path is None or not len(excluded_paths)\
                or excluded_paths is None:
            return True

        if path in excluded_paths:
            return False

        if not path.endswith('/'):
            path = path + '/'
            if path in excluded_paths:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header check

        :param request: request , defaults to None
        :type request: Request, optional
        :return: authorization header or none
        :rtype: str
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """return current user

        :return: current user
        :rtype: _type_
        """
        return getattr(request, 'current_user', None)
