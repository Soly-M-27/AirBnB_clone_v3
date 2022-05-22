#!/usr/bin/python3
''' Create a new view for Places objects that handles all
RESTful API actions '''

from flask import request, abort, Response, jsonify
from models import storage
from models.city import City
from models.place import Place
from models.user import User
from api.v1.views import app_views


@app_views.route('/cities/<city_id>/places',
                 methods=['GET', 'POST'], strict_slashes=False)
def get_all_place_obj(city_id=None):
    ''' Retrieves the list of all State objects '''
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    if request.method == "POST":
        HTTP_body = request.get_json()
        if not HTTP_body:
            return Response("Not a JSON", 400)
        if 'user_id' not in HTTP_body:
            return Response("Missing user_id", 400)
        user_check = storage.get(User, HTTP_body.get('user_id'))
        if not user_check:
            abort(404)
        if 'name' not in HTTP_body:
            return Response("Missing name", 400)
        new_place = Place(name=HTTP_body.get('name'), city_id=city.id,
                          user_id=user.id)
        new_place.save()
        return (jsonify(new_place.to_dict()), 201)

    All_Places = city.places
    Existing_Places = []

    for p in All_Places.values():
        Existing_Places.append(p.to_dict())
    return (jsonify(Existing_Places), 200)


@app_views.route('/places/<place_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def get_a_place(place_id=None):
    ''' Retrives, Deleted or Updates a specified State '''
    a_place = storage.get(Place, place_id)
    if a_place is None:
        abort(404)

    if request.method == "DELETE":
        storage.delete(a_place)
        storage.save()
        return (jsonify({}), 200)

    if request.method == "PUT":
        HTTP_body = request.get_json()
        if not HTTP_body:
            return Response("Not a JSON", 400)
        HTTP_body['id'] = a_place.id
        HTTP_body['created_at'] = a_place.created_at
        HTTP_body['user_id'] = a_place.user_id
        HTTP_body['city_id'] = a_place.city_id
        a_place.__init__(**HTTP_body)
        a_place.save()
        return (jsonify(a_place.to_dict()), 200)
    return (jsonify(a_place.to_dict()), 200)
