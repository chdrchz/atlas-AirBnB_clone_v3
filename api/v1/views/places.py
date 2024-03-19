#!/usr/bin/python3
"""
This module creates the view for all city objects
and handles all default api actions
"""

from api.v1.views import app_views
from flask import Flask, abort, jsonify, make_response, request
from models import storage
from models.place import Place
from models.city import City
from models.user import User


@app_views.route("/cities/<city_id>/places", methods=["GET"],
                 strict_slashes=False)
def get_places(city_id):
    """
    This method retrieves a list of all places in one city
    Args: city - contains a city object
          places - contains all place objects in one city
    Return: a list of dictionaries containing places
    """
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    places = [place.to_dict() for place in city.places]
    return jsonify(places)


@app_views.route("/places/<place_id>", methods=["GET"],
                 strict_slashes=False)
def get_place(place_id):
    """
    This method retrieves one place object
    Args: place - contains one place object, based on its place id
          place_json - city object converted to a dictionary
    Return: a json dictionary containing one place object
    """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)  # Bad request
    place_json = place.to_dict()
    return jsonify(place_json)


@app_views.route("/places/<place_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_place(place_id):
    """
    This method deletes a place object
    Args: place - contains one place object, based on its place id
    Return: an empty dictionary
    """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)  # Bad request
    storage.delete(place)
    storage.save()
    return jsonify({}), 200  # OK


@app_views.route("/cities/<city_id>/places", methods=["POST"],
                 strict_slashes=False)
def create_place(city_id):
    """
    This method creates a city object
    Args: state - contains a state object
          city - contains a city object, based on its city id
          json_data - holds the HTTP json data request
          city_json - holds the dictionary representation of city
          place - holds a dictionary for the corresponding place
    Return: dictionary containing place created
    """
    city = storage.get(City, city_id)
    if city is None:
        return abort(404)
    json_data = request.get_json()
    if not json_data:
        return jsonify([]), 400
    if 'user_id' not in json_data:
        return make_response(jsonify({"error": "Missing user_id"}), 400)
    if 'name' not in json_data:
        return make_response(jsonify({"error": "Missing name"}), 400)
    user = storage.get(User, json_data['user_id'])
    if user is None:
        abort(404)
    json_data['city_id'] = city_id
    place = Place(**json_data)
    place.save()
    place_json = place.to_dict()
    return make_response(jsonify(place_json)), 201


@app_views.route("places/<place_id>", methods=["PUT"], strict_slashes=False)
def update_place(place_id):
    """
    This method updates a city object
    Args: json_data - holds the json data request
          place - contains one place object
          place_json - holds the dictionary representation
    Return: 
    """
    json_data = request.get_json(silent=True)
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    if not json_data:
        abort(400, "Not a JSON")
    if json_data is None:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    for key, value in json_data.items():
        if key not in ["id", "created_at", "updated_at", "city_id", "user_id"]:
            setattr(place, key, value)
    storage.save()
    place_json = place.to_dict()
    return jsonify(place_json)
