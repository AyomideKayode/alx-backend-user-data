#!/usr/bin/env python3

""" SessionAuth module for API authentication
"""

from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """ Session authentication class.
    """
    # initialize dictionary to store user_id by session_id
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a session ID for a user_id
        Args:
            user_id: The user_id to create a session for
        Returns:
            The session ID created
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id
