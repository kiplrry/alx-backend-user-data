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
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header check

        :param request: request , defaults to None
        :type request: Request, optional
        :return: authorization header or none
        :rtype: str
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """return current user

        :return: current user
        :rtype: _type_
        """
        return None
