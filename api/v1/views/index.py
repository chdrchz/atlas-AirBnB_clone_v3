#!/usr/bin/python3
"""The module conatins the index for the api"""
from api.v1.views import app_views
from flask import jsonify

# Task info for Ace's future reference:
#   create a route /status on the object app_views
#   that returns a JSON: "status": "OK" (see example)
# I do not understand what that means
# Where do we make the object????
# Why is the documentation not passing?????
# I am confusion
#
# ACE --- This is Savs, the status:ok is just
# a way for us to see that the status of the
# api works properly, in json format


@app_views.route('/status', strict_slashes=False)
def status():
    """returns the status of the api"""
    return jsonify({"status": "OK"})
