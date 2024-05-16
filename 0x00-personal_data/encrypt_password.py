#!/usr/bin/env python3

""" Hash Password Module.
This module provides a hash_password function that takes in a password string.
The function returns a salted, hashed password, which is a byte string.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ Hashes a password using the bcrypt algorithm.
    Arguments:
      password(str) -- a string to be hashed
    Returns:
      A byte string.
    """
    hashed_pwd = password.encode()  # Convert the password to bytes
    # Generate a salt and hash the password
    salted_hash = bcrypt.hashpw(hashed_pwd, bcrypt.gensalt())
    return salted_hash
