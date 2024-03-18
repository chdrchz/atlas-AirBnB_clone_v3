#!/usr/bin/python3
"""
This module creates the view for all city objects
as well as handles all default api functions
"""

from api.v1.views import app_views
from flask import Flask, abort, jsonify, request
from models import storage
from models.state import State

# @app_views.route("/states/<state_id>/cities")
# def get_all_cities_from_state_id():
