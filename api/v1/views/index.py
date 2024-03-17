#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify

"""
Documentation for jsonifying an index?
-Ace
"""

# Task info for Ace's future reference:
#   create a route /status on the object app_views 
#   that returns a JSON: "status": "OK" (see example)
# I do not understand what that means
# Where do we make the object????
# Why is the documentation not passing?????
# I am confusion

@app_views.route('/status', strict_slashes=False)
def status():
    return jsonify({"status": "OK"})