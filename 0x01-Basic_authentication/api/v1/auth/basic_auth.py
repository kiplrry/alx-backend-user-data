#!/usr/bin/env python3
"""
Basic auth implementation
"""
from api.v1.auth.auth import Auth
import base64

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
                                           base64_authorization_header: str) -> str:
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
        except:
            return None
