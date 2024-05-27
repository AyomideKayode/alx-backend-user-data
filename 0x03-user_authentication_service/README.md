# Project: 0x03. User authentication service

![User Authentication Service](./user_auth_service.jpg)

## Resources

### Read or watch:-

- [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
- [Requests module](https://requests.kennethreitz.org/en/latest/user/quickstart/)
- [HTTP status codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)

### Learning Objectives:-

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

### Setup

Install `bcrypt`

```bash
ayomide@Kazzywiz:~/alx-backend-user-data/0x03-user_authentication_service$ pip3 install bcrypt
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: bcrypt in /home/ayomide/.local/lib/python3.8/site-packages (3.1.7)
Requirement already satisfied: cffi>=1.1 in /home/ayomide/.local/lib/python3.8/site-packages (from bcrypt) (1.16.0)
Requirement already satisfied: six>=1.4.1 in /usr/lib/python3/dist-packages (from bcrypt) (1.14.0)
Requirement already satisfied: pycparser in /home/ayomide/.local/lib/python3.8/site-packages (from cffi>=1.1->bcrypt) (2.21)
ayomide@Kazzywiz:~/alx-backend-user-data/0x03-user_authentication_service$ 
```

## Tasks

### 0. [User model](./user.py) :-

In this task you will create a SQLAlchemy model named `User` for a database table named `users` (by using the [mapping declaration](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#declare-a-mapping) of SQLAlchemy).

The model will have the following attributes:

- `id`, the integer primary key
- `email`, a non-nullable string
- `hashed_password`, a non-nullable string
- `session_id`, a nullable string
- `reset_token`, a nullable string

```bash
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from user import User

print(User.__tablename__)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))

bob@dylan:~$ python3 main.py
users
users.id: INTEGER
users.email: VARCHAR(250)
users.hashed_password: VARCHAR(250)
users.session_id: VARCHAR(250)
users.reset_token: VARCHAR(250)
bob@dylan:~$ 
```

### 1. [create user](./db.py) :-

In this task, you will complete the `DB` class provided below to implement the `add_user` method.

```bash
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
```

Note that `DB._session` is a private property and hence should NEVER be used from outside the `DB` class.

Implement the `add_user` method, which has two required string arguments: `email` and `hashed_password`, and returns a `User` object. The method should save the user to the database. No validations are required at this stage.

```bash
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

from db import DB
from user import User

my_db = DB()

user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
print(user_1.id)

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
print(user_2.id)

bob@dylan:~$ python3 main.py
1
2
bob@dylan:~$
```

### 2. [Find user](./db.py) :-

In this task you will implement the `DB.find_user_by` method. This method takes in arbitrary keyword arguments and returns the first row found in the `users` table as filtered by the method’s input arguments. No validation of input arguments required at this point.

Make sure that SQLAlchemy’s `NoResultFound` and `InvalidRequestError` are raised when no results are found, or when wrong query arguments are passed, respectively.

Warning:

- `NoResultFound` has been moved from `sqlalchemy.orm.exc` to `sqlalchemy.exc` between the version 1.3.x and 1.4.x of SQLAchemy - please make sure you are importing it from `sqlalchemy.orm.exc`

```bash
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


my_db = DB()

user = my_db.add_user("test@test.com", "PwdHashed")
print(user.id)

find_user = my_db.find_user_by(email="test@test.com")
print(find_user.id)

try:
    find_user = my_db.find_user_by(email="test2@test.com")
    print(find_user.id)
except NoResultFound:
    print("Not found")

try:
    find_user = my_db.find_user_by(no_email="test@test.com")
    print(find_user.id)
except InvalidRequestError:
    print("Invalid")        

bob@dylan:~$ python3 main.py
1
1
Not found
Invalid
bob@dylan:~$ 
```

| Task | File |
| ---- | ---- |
| 3. update user | [db.py](./db.py) |
| 4. Hash password | [auth.py](./auth.py) |
| 5. Register user | [auth.py](./auth.py) |
| 6. Basic Flask app | [app.py](./app.py) |
| 7. Register user | [app.py](./app.py) |
| 8. Credentials validation | [auth.py](./auth.py) |
| 9. Generate UUIDs | [auth.py](./auth.py) |
| 10. Get session ID | [auth.py](./auth.py) |
| 11. Log in | [app.py](./app.py) |
| 12. Find user by session ID | [auth.py](./auth.py) |
| 13. Destroy session | [auth.py](./auth.py) |
| 14. Log out | [app.py](./app.py) |
| 15. User profile | [app.py](./app.py) |
| 16. Generate reset password token | [auth.py](./auth.py) |
| 17. Get reset password token | [app.py](./app.py) |
| 18. Update password | [auth.py](./auth.py) |
| 19. Update password end-point | [app.py](./app.py) |
