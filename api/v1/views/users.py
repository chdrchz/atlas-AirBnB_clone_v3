#!/usr/bin/python3
"""
This module creates the view for all state objects
and handles all default api actions
"""

from api.v1.views import app_views, index
from flask import Flask, abort, jsonify, request
from models import storage
from models.user import User


@app_views.route("/users", methods=['GET'], strict_slashes=False)
def get_all_users():
    """
    This method retrieves a list of all state objects
    Args: users - list of all users, keys excluded
          users_json - all users converted to a list of dictionaries
    Return: a json dictionary containing all user objects
    """
    users = storage.all(User).values()
    users_json = [user.to_dict() for user in users]
    return jsonify(users_json)


@app_views.route("/users/<user_id>", methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """
    This method retrieves one user object
    Args: user - retrieves one user object, based on its user id
          user_json - user object converted to a dictionary
    Return: a json dictionary containing one user object
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404) #Bad request
    user_json = user.to_dict()
    return jsonify(user_json)


@app_views.route(
        "/users/<user_id>", methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """
    This method deletes one user object
    Args: user - retrieves one user object, based on its user id
    Return: an empty json dictionary
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404) #Bad request
    storage.delete(user)
    print(f"type of user: {type(user)}")
    storage.save()
    return jsonify({}), 200 #OK


@app_views.route("/users", methods=['POST'], strict_slashes=False)
def create_user():
    """
    This method creates a user object
    Args: user - gets an HTTP body request to a user object
          json_data - holds the json data request
    Return: a json dictionary containing one state object
    """
    json_data = request.get_json(silent=True)
    if not json_data:
        abort(400, 'Not a JSON') #Bad request
    if 'name' not in json_data:
        abort(400, 'Missing name') #Bad request
    user = User(**json_data)
    user.save()
    user_json = user.to_dict()
    return jsonify(user_json), 201 #OK


@app_views.route(
        "/users/<user_id>", methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """
    This method updates a user object
    Args: user - retrieves one user object, based on its user id
          json_data - json request data for readability
          new_user - exists to store the unpacked request
          user_json - user object converted to a dictionary
    Return: a json dictionary
    """
    user = storage.get(User, user_id)
    json_data = request.get_json()
    if json_data is None:
            abort(400, description="Not a JSON")
    if 'email' not in json_data:
        abort(400, description="Missing email")
    if 'password' not in json_data:
        abort(400, description="Missing password")
    for key, value in json_data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(user, key, value)
    new_user = User(**json_data)
    new_user.save()
    user_json = new_user.to_dict()
    return jsonify(user_json)
