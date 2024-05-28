#!/usr/bin/env python3

""" User authentication service module
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


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


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register a new user by hashing the password and adding the user
        to the database.
        Args:
            email (str): The email of the new user.
            password (str): The password of the new user
        Returns:
            User: The newly created User object.
        Raises:
            ValueError: If a user with the given email already exists.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # user doesn't exist, we proceed to create new user
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)

            return new_user