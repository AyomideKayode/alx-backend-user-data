#!/usr/bin/env python3

""" User authentication service module
"""

from db import DB
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Takes in a password string arguments and returns a salted hash.
    Args:
        password (str): The password string to hash.
    Returns:
        bytes: The hashed password.
    """
    # generate a salted hash for the password
    salt = bcrypt.gensalt()
    # hash the password with the generated salt
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password
