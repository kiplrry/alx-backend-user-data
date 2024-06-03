#!/usr/bin/env python3
"""Authorization module
"""
from flask import Request
from typing import List, TypeVar


class Auth:
    """ Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth"""
        if path is None or not excluded_paths:
            return True

        path_slashed = path if path.endswith('/') \
            else path + '/'
        path = path_slashed.removesuffix('/')

        print(path, path_slashed)
        if path_slashed in excluded_paths \
                or path in excluded_paths:
            return False

        return True

    def authorization_header(self, request: Request = None) -> str:
        """auth header"""
        if request is None or \
                request.authorization is None:
            return None
        return request.authorization

    def current_user(self, request: Request = None) -> TypeVar('User'):
        """return Current user"""
        return None
