#!/usr/bin/env python3

""" Basic Flask App setup.
"""

from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def welcome():
    """ Welcome message for the API
    GET '/' route that returns a JSON payload response
    Returns:
        (str): JSON payload response
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """ POST '/users' route that registers a new user.
    Returns:
        Response: JSON response indicating success if user was fully registered
                    or error if user already exists.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return jsonify({"message": "email and password required"}), 400

    try:
        new_user = AUTH.register_user(email, password)
        return jsonify({"email": new_user.email,
                        "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
