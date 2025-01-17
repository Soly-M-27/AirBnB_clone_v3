#!/usr/bin/python3
''' Create a new view for City objects that handles all
RESTful API actions '''

from flask import request, abort, Response, jsonify
from models import storage
from models.state import State
from models.city import City
from api.v1.views import app_views


@app_views.route('/states/<state_id>/cities',
                 methods=['GET', 'POST'], strict_slashes=False)
def get_all_city_obj(state_id=None):
    ''' Retrieves the list of all State objects '''
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if request.method == "POST":
        HTTP_body = request.get_json()
        if not HTTP_body:
            return Response("Not a JSON", 400)
        if 'name' not in HTTP_body:
            return Response("Missing name", 400)
        new_city = City(name=HTTP_body.get('name'), state_id=state.id)
        new_city.save()
        return (jsonify(new_city.to_dict()), 201)

    All_Cities = storage.all('City')
    Existing_Cities = []

    for city in All_Cities.values():
        if city.state_id == state.id:
            Existing_Cities.append(city.to_dict())
    return jsonify(Existing_Cities)


@app_views.route('/cities/<city_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def get_a_city(city_id=None):
    ''' Retrives, Deleted or Updates a specified State '''
    a_city = storage.get(City, city_id)
    if a_city is None:
        abort(404)

    if request.method == "DELETE":
        storage.delete(a_city)
        storage.save()
        return (jsonify({}), 200)

    if request.method == "PUT":
        HTTP_body = request.get_json()
        if not HTTP_body:
            return Response("Not a JSON", 400)
        HTTP_body['id'] = a_city.id
        HTTP_body['created_at'] = a_city.created_at
        HTTP_body['state_id'] = a_city.state_id
        a_city.__init__(**HTTP_body)
        a_city.save()
        return (jsonify(a_city.to_dict()), 200)
    return jsonify(a_city.to_dict())
