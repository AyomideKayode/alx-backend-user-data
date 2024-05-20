#!/usr/bin/env python3
"""Auth module for API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Using this function to check if authentication is required
        for a given path
        Args:
            path (str): The path to check
            excluded_paths (List[str]): A list of paths that do not
            require authentication
        Returns:
            bool: False for now, logic will be implemented later
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Retrieves the authorization header from the request
        Args:
            request (flask.Request): The Flask request object
        Returns:
            str: None for now, logic will be implemented later
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user from the request
        Args:
            request (flask.Request): The Flask request object
        Returns:
            TypeVar('User'): None for now, logic will be implemented later
        """
        return None
