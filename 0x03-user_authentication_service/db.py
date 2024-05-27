#!/usr/bin/env python3

"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        # Create an engine to connect to the SQLite database file "a.db"
        # can set echo to False to hide the SQL queries
        self._engine = create_engine("sqlite:///a.db", echo=True)
        # Drop all existing tables defined in the Base metadata from the database
        Base.metadata.drop_all(self._engine)
        # Create all tables defined in the Base metadata in the database
        Base.metadata.create_all(self._engine)
        # Initialize the session as None
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        # Check if session is already created
        if self.__session is None:
            # Create a session using sessionmaker and bind it to the engine
            DBSession = sessionmaker(bind=self._engine)
            # Assign the created session to the private variable __session
            self.__session = DBSession()
        # Return the session object
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add the user to the database
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()

        return new_user
