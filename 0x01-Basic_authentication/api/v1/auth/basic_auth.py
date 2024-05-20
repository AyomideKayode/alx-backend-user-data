#!/usr/bin/env python3
""" BasicAuth module for API authentication
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class that inherits from Auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extracts the base64 part of the Authorization header
        for Basic Authentication
        Arg(s):
          authorization_header (str): The Authorization header
        Returns:
          str: The base64 part of the Authorization header, or None if invalid
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        # we remove the "Basic " prefix to get the base64 part
        base64_str = authorization_header[6:]
        return base64_str
