#!/usr/bin/env python3
""" Module of Session views
"""
from api.v1.views import app_views
from flask import jsonify, request
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Login the user
    """

    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    passw = request.form.get('password')
    if not passw:
        return jsonify({"error": "password missing"}), 400
    users = User.search({'email': email})
    if len(users) < 1:
        return jsonify({"error": "no user found for this email"}), 404
    user: User = None
    for _user in users:
        if _user.is_valid_password(passw):
            user = _user
    if user is None:
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    from os import getenv
    sess_id = auth.create_session(user.id)
    user_dict = user.to_json()
    resp = jsonify(user_dict)
    sess_name = getenv('SESSION_NAME')
    resp.set_cookie(sess_name, sess_id)
    return resp
