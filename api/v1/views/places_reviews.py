#!/usr/bin/python3
"""
This module creates the view for all review objects
and handles all default api actions
"""

from api.v1.views import app_views
from flask import Flask, abort, jsonify, make_response, request
from models import storage
from models.review import Review
from models.place import Place


@app_views.route('/places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def get_reviews(place_id):
    """
    This method retrieves a list of all reviews for a place
    Args: place - contains a place object
    Return: a list of dictionaries containing reviews
    """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    reviews = place.reviews
    reviews_list = []
    for review in reviews:
        reviews_list.append(review.to_dict())
    return jsonify(reviews_list)
