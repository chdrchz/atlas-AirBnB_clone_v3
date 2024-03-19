#!/usr/bin/python3
"""
This module creates the view for all review objects
and handles all default api actions
"""

from api.v1.views import app_views
from flask import Flask, abort, jsonify, make_response, request
from models import storage
from models.review import Review



