#!/usr/bin/python3
''' Create a new view for Review objects that handles all
RESTful API actions '''

from flask import request, abort, Response, jsonify
from models import storage
from models.review import Review
from models.user import User
from models.place import Place
from api.v1.views import app_views


@app_views.route('/places/<place_id>/reviews',
                 methods=['GET', 'POST'], strict_slashes=False)
def get_all_review_obj(place_id=None):
    ''' Retrieves the list of all Review objects '''
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    if request.method == "POST":
        HTTP_body = request.get_json()
        if not HTTP_body:
            return Response("Not a JSON", 400)
        if 'user_id' not in HTTP_body:
            return Response("Missing user_id", 400)
        if 'text' not in HTTP_body:
            return Response("Missing text", 400)

        user_check = storage.get(User, HTTP_body.get('user_id'))
        if not user_check:
            abort(404)

        review = Review(place_id=place.id, user_id=user.id,
                        text=HTTP_body.get('text'))
        review.save()
        return (jsonify(review.to_dict()), 201)

    All_Reviews = place.reviews
    Existing_Reviews = []

    for r in All_Reviews:
        Existing_Reviews.append(r.to_dict())
    return (jsonify(Existing_Reviews), 200)


@app_views.route('/reviews/<review_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def get_a_review(review_id=None):
    ''' Retrives, Deleted or Updates a specified Place '''
    a_review = storage.get(Review, review_id)
    if a_review is None:
        abort(404)

    if request.method == "DELETE":
        storage.delete(a_review)
        storage.save()
        return (jsonify({}), 200)

    if request.method == "PUT":
        HTTP_body = request.get_json()
        if not HTTP_body:
            return Response("Not a JSON", 400)
        HTTP_body['id'] = a_review.id
        HTTP_body['user_id'] = a_review.user_id
        HTTP_body['place_id'] = a_review.place_id
        HTTP_body['created_at'] = a_review.created_at
        a_review.__init__(**HTTP_body)
        a_review.save()
        return (jsonify(a_review.to_dict()), 200)
    return (jsonify(a_review.to_dict()), 200)
