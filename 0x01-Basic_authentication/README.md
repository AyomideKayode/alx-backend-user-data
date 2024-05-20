# Project: 0x01. Basic authentication

![Authentication Failed](./authentication_failed.png)

## Resources

### Read or watch:-

- [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY)
- [Base64 in Python](https://docs.python.org/3.7/library/base64.html)
- [HTTP header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
- [Flask](https://palletsprojects.com/p/flask/)
- [Base64 - concept](https://en.wikipedia.org/wiki/Base64)

## Learning Objectives

### General

- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

## Simple API

Simple HTTP API for playing with `User` model.

## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints

## Setup

```bash
pip3 install -r requirements.txt
```

## Run

```bash
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

## Minor Walkthrough for setting up and configuration of the project

- I tried running my flask app when I installed all dependencies inside the `requirement.txt` and I kept getting errors like the `markupsafe` in my current environment not being compatible with the version of `Jinja2` that was installed and other little PoS errors like that.
- So what I did was create a virtual environment for the Basic Auth project and I went on to install the `requirement.txt` file again and I began to downgrade some dependencies versions to make it all comaptible with each other...
- See the following bash session below for details...

```bash
ayomide@Kazzywiz:~/alx-backend-user-data/0x01-Basic_authentication$ source myvenv/bin/activate
(myvenv) ayomide@Kazzywiz:~/alx-backend-user-data/0x01-Basic_authentication$ pip3 install -r requirements.txt 
Collecting Flask==1.1.2
  Using cached Flask-1.1.2-py2.py3-none-any.whl (94 kB)
Collecting Flask-Cors==3.0.8
  Using cached Flask_Cors-3.0.8-py2.py3-none-any.whl (14 kB)
Collecting Jinja2==2.11.2
  Using cached Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
Collecting requests==2.18.4
  Using cached requests-2.18.4-py2.py3-none-any.whl (88 kB)
Collecting pycodestyle==2.6.0
  Using cached pycodestyle-2.6.0-py2.py3-none-any.whl (41 kB)
Collecting Werkzeug>=0.15
  Using cached werkzeug-3.0.3-py3-none-any.whl (227 kB)
Collecting click>=5.1
  Using cached click-8.1.7-py3-none-any.whl (97 kB)
Collecting itsdangerous>=0.24
  Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Collecting Six
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting MarkupSafe>=0.23
  Using cached MarkupSafe-2.1.5-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (26 kB)
Collecting certifi>=2017.4.17
  Using cached certifi-2024.2.2-py3-none-any.whl (163 kB)
Collecting chardet<3.1.0,>=3.0.2
  Using cached chardet-3.0.4-py2.py3-none-any.whl (133 kB)
Collecting idna<2.7,>=2.5
  Using cached idna-2.6-py2.py3-none-any.whl (56 kB)
Collecting urllib3<1.23,>=1.21.1
  Using cached urllib3-1.22-py2.py3-none-any.whl (132 kB)
Installing collected packages: MarkupSafe, Werkzeug, Jinja2, click, itsdangerous, Flask, Six, Flask-Cors, certifi, chardet, idna, urllib3, requests, pycodestyle
Successfully installed Flask-1.1.2 Flask-Cors-3.0.8 Jinja2-2.11.2 MarkupSafe-2.1.5 Six-1.16.0 Werkzeug-3.0.3 certifi-2024.2.2 chardet-3.0.4 click-8.1.7 idna-2.6 itsdangerous-2.2.0 pycodestyle-2.6.0 requests-2.18.4 urllib3-1.22
(myvenv) ayomide@Kazzywiz:~/alx-backend-user-data/0x01-Basic_authentication$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
Traceback (most recent call last):
  File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib/python3.8/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/home/ayomide/alx-backend-user-data/0x01-Basic_authentication/api/v1/app.py", line 6, in <module>
    from api.v1.views import app_views
  File "/home/ayomide/alx-backend-user-data/0x01-Basic_authentication/api/v1/views/__init__.py", line 4, in <module>
    from flask import Blueprint
  File "/home/ayomide/alx-backend-user-data/0x01-Basic_authentication/myvenv/lib/python3.8/site-packages/flask/__init__.py", line 19, in <module>
    from . import json
  File "/home/ayomide/alx-backend-user-data/0x01-Basic_authentication/myvenv/lib/python3.8/site-packages/flask/json/__init__.py", line 15, in <module>
    from itsdangerous import json as _json
ImportError: cannot import name 'json' from 'itsdangerous' (/home/ayomide/alx-backend-user-data/0x01-Basic_authentication/myvenv/lib/python3.8/site-packages/itsdangerous/__init__.py)
```

- Uninstalled `itsdangerous` and reinstalled a compatible version

```bash
(myvenv) ayomide@Kazzywiz:~/alx-backend-user-data/0x01-Basic_authentication$ pip uninstall itsdangerous
Found existing installation: itsdangerous 2.2.0
Uninstalling itsdangerous-2.2.0:
  Would remove:
    /home/ayomide/alx-backend-user-data/0x01-Basic_authentication/myvenv/lib/python3.8/site-packages/itsdangerous-2.2.0.dist-info/*
    /home/ayomide/alx-backend-user-data/0x01-Basic_authentication/myvenv/lib/python3.8/site-packages/itsdangerous/*
Proceed (y/n)? y 
  Successfully uninstalled itsdangerous-2.2.0
(myvenv) ayomide@Kazzywiz:~/alx-backend-user-data/0x01-Basic_authentication$ pip install itsdangerous==1.1.0
Collecting itsdangerous==1.1.0
  Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Installing collected packages: itsdangerous
Successfully installed itsdangerous-1.1.0
(myvenv) ayomide@Kazzywiz:~/alx-backend-user-data/0x01-Basic_authentication$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
Traceback (most recent call last):
  File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib/python3.8/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/home/ayomide/alx-backend-user-data/0x01-Basic_authentication/api/v1/app.py", line 6, in <module>
    from api.v1.views import app_views
  File "/home/ayomide/alx-backend-user-data/0x01-Basic_authentication/api/v1/views/__init__.py", line 4, in <module>
    from flask import Blueprint
  File "/home/ayomide/alx-backend-user-data/0x01-Basic_authentication/myvenv/lib/python3.8/site-packages/flask/__init__.py", line 21, in <module>
    from .app import Flask
  File "/home/ayomide/alx-backend-user-data/0x01-Basic_authentication/myvenv/lib/python3.8/site-packages/flask/app.py", line 32, in <module>
    from werkzeug.wrappers import BaseResponse
ImportError: cannot import name 'BaseResponse' from 'werkzeug.wrappers' (/home/ayomide/alx-backend-user-data/0x01-Basic_authentication/myvenv/lib/python3.8/site-packages/werkzeug/wrappers/__init__.py)
```

- Ran into another error and then repeated the same process with `werkzeug`

```bash
(myvenv) ayomide@Kazzywiz:~/alx-backend-user-data/0x01-Basic_authentication$ pip uninstall werkzeug
Found existing installation: werkzeug 3.0.3
Uninstalling werkzeug-3.0.3:
  Would remove:
    /home/ayomide/alx-backend-user-data/0x01-Basic_authentication/myvenv/lib/python3.8/site-packages/werkzeug-3.0.3.dist-info/*
    /home/ayomide/alx-backend-user-data/0x01-Basic_authentication/myvenv/lib/python3.8/site-packages/werkzeug/*
Proceed (y/n)? y
  Successfully uninstalled werkzeug-3.0.3
(myvenv) ayomide@Kazzywiz:~/alx-backend-user-data/0x01-Basic_authentication$ pip install werkzeug==1.0.1
Collecting werkzeug==1.0.1
  Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
     |█                               | 10 kB 426 kB/s e
     |██▏                             | 20 kB 368 kB/s e
     |███▎                            | 30 kB 546 kB/s e
     |████▍                           | 40 kB 194 kB/s e
     |█████▌                          | 51 kB 179 kB/s e
     |██████▋                         | 61 kB 215 kB/s e
     |███████▊                        | 71 kB 250 kB/s e
     |████████▉                       | 81 kB 286 kB/s e
     |█████████▉                      | 92 kB 321 kB/s e
     |███████████                     | 102 kB 260 kB/s 
     |████████████                    | 112 kB 260 kB/s 
     |█████████████▏                  | 122 kB 260 kB/s 
     |██████████████▎                 | 133 kB 260 kB/s 
     |███████████████▍                | 143 kB 260 kB/s 
     |████████████████▌               | 153 kB 260 kB/s 
     |█████████████████▋              | 163 kB 260 kB/s 
     |██████████████████▋             | 174 kB 260 kB/s 
     |███████████████████▊            | 184 kB 260 kB/s 
     |████████████████████▉           | 194 kB 260 kB/s 
     |██████████████████████          | 204 kB 260 kB/s 
     |███████████████████████         | 215 kB 260 kB/s 
     |████████████████████████▏       | 225 kB 260 kB/s 
     |█████████████████████████▎      | 235 kB 260 kB/s 
     |██████████████████████████▍     | 245 kB 260 kB/s 
     |███████████████████████████▍    | 256 kB 260 kB/s 
     |████████████████████████████▌   | 266 kB 260 kB/s 
     |█████████████████████████████▋  | 276 kB 260 kB/s 
     |██████████████████████████████▊ | 286 kB 260 kB/s 
     |███████████████████████████████▉| 296 kB 260 kB/s 
     |████████████████████████████████| 298 kB 260 kB/s 
Installing collected packages: werkzeug
Successfully installed werkzeug-1.0.1
(myvenv) ayomide@Kazzywiz:~/alx-backend-user-data/0x01-Basic_authentication$ pip list | grep werkzeug
```

- At this point, all seemed to be compatible with each other and then I can proceed

```bash
(myvenv) ayomide@Kazzywiz:~/alx-backend-user-data/0x01-Basic_authentication$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [20/May/2024 21:49:39] "GET / HTTP/1.1" 404 -
127.0.0.1 - - [20/May/2024 21:49:39] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [20/May/2024 21:50:42] "GET /api/v1/status HTTP/1.1" 200 -
```

## Tasks

### 0. [Simple-basic-API](./) :-

Download and start your project from this `[archive.zip](https://intranet.alxswe.com/rltoken/2o4gAozNufil_KjoxKI5bA)`

In this archive, you will find a simple API with one model: `User`. Storage of these users is done via a serialization/deserialization in files.

#### Setup and start server

```bash
bob@dylan:~$ pip3 install -r requirements.txt
...
bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Serving Flask app "app" (lazy loading)
...
bob@dylan:~$
```

#### Use the API (in another tab or in your browser)

```bash
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status" -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/status HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 16
< Access-Control-Allow-Origin: *
< Server: Werkzeug/1.0.1 Python/3.7.5
< Date: Mon, 18 May 2020 20:29:21 GMT
< 
{"status":"OK"}
* Closing connection 0
bob@dylan:~$
```

### 1. [Error handler: Unauthorized](api/v1), [api/v1/app.py](./api/v1/app.py), [api/v1/views/index.py](./api/v1/views/index.py) :-

What the HTTP status code for a request unauthorized? `401` of course!

Edit `api/v1/app.py`:

- Add a new error handler for this status code, the response must be:
  - a JSON: `{"error": "Unauthorized"}`
  - status code `401`
  - you must use `jsonify` from Flask

For testing this new error handler, add a new endpoint in `api/v1/views/index.py`:

- Route: `GET /api/v1/unauthorized`
- This endpoint must raise a 401 error by using `abort` - [Custom Error Pages](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/)

By calling `abort(401)`, the error handler for 401 will be executed.

In the first terminal:

```bash
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In a second terminal:

```bash
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/unauthorized"
{
  "error": "Unauthorized"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/unauthorized" -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/unauthorized HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 401 UNAUTHORIZED
< Content-Type: application/json
< Content-Length: 30
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Sun, 24 Sep 2017 22:50:40 GMT
< 
{
  "error": "Unauthorized"
}
* Closing connection 0
bob@dylan:~$
```

### 2. [Error handler: Forbidden](api/v1), [api/v1/app.py](./api/v1/app.py), [api/v1/views/index.py](./api/v1/views/index.py) :-

### 3. [Auth class](api/v1), [api/v1/auth](./api/v1/auth), [api/v1/auth/__init__.py](./api/v1/auth/__init__.py), [api/v1/auth/auth.py](./api/v1/auth/auth.py) :-

### 4. [Define which routes don't need authentication](api/v1/auth) | [api/v1/auth/auth.py](./api/v1/auth/auth.py) :-

### 5. [Request validation!](api/v1) | [api/v1/app.py](./api/v1/app.py), [api/v1/auth/auth.py](./api/v1/auth/auth.py) :-

### 6. [Basic auth](api/v1) | [api/v1/app.py](./api/v1/app.py), [api/v1/auth/basic_auth.py](./api/v1/auth/basic_auth.py) :-

### 7. [Basic - Base64 part](api/v1) | [api/v1/auth/basic_auth.py](./api/v1/auth/basic_auth.py) :-

### 8. [Basic - Base64 decode](api/v1) | [api/v1/auth/basic_auth.py](./api/v1/auth/basic_auth.py) :-

### 9. [Basic - User credentials](api/v1/auth), [api/v1/auth/basic_auth.py](./api/v1/auth/basic_auth.py) :-

### 10. [Basic - User object](api/v1/auth) | [api/v1/auth/basic_auth.py](./api/v1/auth/basic_auth.py) :-

### 11. [Basic - Overload current_user - and BOOM!](api/v1/auth) | [api/v1/auth/basic_auth.py](./api/v1/auth/basic_auth.py) :-
