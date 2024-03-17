#!/usr/bin/python3
"""Adding documentation here?? -- Sav"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """returns the status of the api"""
    return jsonify({"status": "OK"})
