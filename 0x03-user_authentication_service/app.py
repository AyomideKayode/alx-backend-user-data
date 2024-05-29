#!/usr/bin/env python3

""" Basic Flask App setup.
"""

from flask import Flask, jsonify, request, abort, make_response, redirect
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


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """ POST '/sessions' route that logs in a user.
    Log in users if provided credentials are correct,
    and create a new session for them.
    Returns:
        Response: JSON response indicating success if user was logged in
                    or error if user does not exist.
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        return jsonify({"message": "email and password required"}), 400

    if not AUTH.valid_login(email, password):
        abort(401)  # Abort the request if login credentials are invalid

    session_id = AUTH.create_session(email)
    if not session_id:
        abort(401)  # Abort request if session creation fails

    response = make_response(jsonify({"email": f"{email}",
                                      "message": "logged in"}))
    # Set the session_id as a cookie in the response
    response.set_cookie("session_id", session_id)
    return response


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> str:
    """ DELETE '/sessions' route that logs out a user.
    Log out users by deleting their current session.
    Returns:
        Response: JSON response indicating success if user was logged out
                    or error if user does not exist.
    """
    # Get session_id from request cookies
    session_id = request.cookies.get("session_id")
    # Get the user associated with the session_id
    user = AUTH.get_user_from_session_id(session_id)
    if user is None or session_id is None:
        abort(403)  # Abort the request with a 403 Forbidden status code
    AUTH.destroy_session(user.id)  # Destroy the session for the user
    return redirect("/")  # Redirect the user to the home page


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
