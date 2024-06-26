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
            raise TypeError
        if path is None or not excluded_paths:
            return True

        path_slashed = path if path.endswith('/') \
            else path + '/'
        path = path_slashed.removesuffix('/')
        if path_slashed in excluded_paths \
                or path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header check

        :param request: request , defaults to None
        :type request: Request, optional
        :return: authorization header or none
        :rtype: str
        """
        if request is None or \
                request.authorization is None:
            return None
        return request.authorization

    def current_user(self, request=None) -> User:
        """return current user

        :return: current user
        :rtype: _type_
        """
        return None
