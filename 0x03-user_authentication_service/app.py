#!/usr/bin/env python3
"""basic flask app
"""
from flask import Flask, jsonify, request
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    return jsonify({"message": "Bienvenue"})

@app.post('/users', strict_slashes=False)
def users():
    """implements users route
    """
    email = request.form.get('email')
    password = request.form.get('password')
    user = None
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
