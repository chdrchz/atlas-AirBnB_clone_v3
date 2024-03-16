#!/usr/bin/python3
"""This module defines a flask web app"""
from api.v1.views import app_views
from flask import Flask
from models import storage
import os

app = Flask(__name__)
app.register_blueprint(app_views)

# Hey Savs, I'm kind of confused about this decorator?
# @app.teardown_appcontext('/', strict_slashes=False)
# temp comment to see what the hecky becky is up
#   Ok so looks like that may have been part of the issue.
#   Now to figure out where everything else is sitting
#   And I'm not really sure what's happening
#   But at least it's running?
#   -Ace
@app.teardown_appcontext
def teardown():
    storage.close()

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)