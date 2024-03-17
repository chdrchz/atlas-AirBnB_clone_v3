#!/usr/bin/python3
"""This module defines a flask web app"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """This method handles the teardown, on itself"""
    storage.close()


@app.errorhandler(404)
def error_404():
    """ return for 404 errors """
    return jsonify({"error": "Not found"})


def start_flask():
    """
    starts flask - sets host and port from getenv
    if 'name == main' runs this method
    """
    app.run(host=getenv('HBNB_API_HOST', default='localhost'),
            port=getenv('HBNB_API_PORT'),
            threaded=True)


if __name__ == "__main__":
    start_flask()
