#!/usr/bin/python3
''' Create a new view for Amenity objects that handles all
RESTful API actions '''

from flask import request, abort, Response, jsonify
from models import storage
from models.amenity import Amenity
from api.v1.views import app_views


@app_views.route('/amenities', methods=['GET', 'POST'], strict_slashes=False)
def get_all_amenities_obj():
    ''' Retrieves the list of all Amenities objects '''
    if request.method == "POST":
        HTTP_body = request.get_json()
        if not HTTP_body:
            return Response("Not a JSON", 400)
        if 'name' not in HTTP_body:
            return Response("Missing name", 400)
        new_amenity = Amenity(name=HTTP_body.get('name'))
        new_amenity.save()
        return (jsonify(new_amenity.to_dict()), 201)

    All_Amenities = storage.all('Amenity')
    Existing_Amenities = []

    for ame in All_Amenities.values():
        Existing_Amenities.append(ame.to_dict())
    return jsonify(Existing_Amenities)


@app_views.route('/amenities/<amenity_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def get_a_amenity(amenity_id=None):
    ''' Retrives, Deleted or Updates a specified Amenity '''
    a_amenity = storage.get(Amenity, amenity_id)
    if a_amenity is None:
        abort(404)

    if request.method == "DELETE":
        storage.delete(a_amenity)
        storage.save()
        return (jsonify({}), 200)

    if request.method == "PUT":
        HTTP_body = request.get_json()
        if not HTTP_body:
            return Response("Not a JSON", 400)
        HTTP_body['id'] = a_amenity.id
        HTTP_body['created_at'] = a_amenity.created_at
        a_amenity.__init__(**HTTP_body)
        a_amenity.save()
        return (jsonify(a_amenity.to_dict()), 200)
    return jsonify(a_amenity.to_dict())
