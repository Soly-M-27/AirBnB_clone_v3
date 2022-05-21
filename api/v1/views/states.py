#!/usr/bin/python3
''' Create a new view for State onnjects that handles all
RESTful API actions '''


from flask import jsonify, abort, request, Response
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states', methods=['GET', 'POST'], strict_slashes=False)
def get_all_state_obj():
    ''' Retrieves the list of all State objects '''
    if request.method == "POST":
        HTTP_body = request.get_json()
        if not HTTP_body:
            return Response("Not a JSON", 400)
        if 'name' not in HTTP_body:
            return Response("Missing name", 400)
        state = State(name=HTTP_body.get('name'))
        state.save()
        return (jsonify(state.to_dict()), 201)

    All_States = storage.all('State')
    Existing_States = []

    for state in All_States.values():
        Existing_States.append(state.to_dict())
        return jsonify(Existing_States)


@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def get_a_state(state_id=None):
    ''' Retrives, Deleted or Updates a specified State '''
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    if request.method == "DELETE":
        storage.delete(state)
        storage.save()
        return (jsonify({}), 200)

    if request.method == "PUT":
        HTTP_body = request.get_json()
        if not HTTP_body:
            return Response("Not a JSON", 400)
        HTTP_body['id'] = state.id
        HTTP_body['created_at'] = state.created_at
        state.__init__(**HTTP_body)
        state.save()
        return (jsonify(state.to_dict()), 200)
    return jsonify(state.to_dict())
