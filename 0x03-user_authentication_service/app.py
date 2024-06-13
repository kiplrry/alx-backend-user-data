#!/usr/bin/env python3
"""basic flask app
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """implements users route
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    '''logs the user in'''
    email = request.form.get('email')
    password = request.form.get('password')
    valid = AUTH.valid_login(email, password)
    if valid is False:
        abort(401)
    sess = AUTH.create_session(email)
    res = jsonify({"email": email, "message": "logged in"})
    res.set_cookie("session_id", sess)
    return res


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """logs user out
    """
    sess = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(sess)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """get profile
    """
    sess = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(sess)
    if user:
        return jsonify({"email": user.email})
    abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """reset password
    """
    email = request.form.get('email')
    try:
        token = AUTH.get_reset_password_token(email=email)
        return jsonify({"email": email, "reset_token": token})
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """updates pass
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    password = request.form.get('password')
    try:
        AUTH.update_password(reset_token, password)
    except Exception:
        abort(403)
    return jsonify({"email": email, "message": "Password updated"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
