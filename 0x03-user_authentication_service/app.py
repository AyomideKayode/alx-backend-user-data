#!/usr/bin/env python3

""" Basic Flask App setup.
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def welcome():
    """ Welcome message for the API
    GET '/' route that returns a JSON payload response
    Returns:
        (str): JSON payload response
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
