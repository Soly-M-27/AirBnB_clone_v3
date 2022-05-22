#!/usr/bin/python3
''' Create a new view for User objects that handles all
RESTful API actions '''

from flask import request, abort, Response, jsonify
from models import storage
from models.user import User
from api.v1.views import app_views


@app_views.route('/users', methods=['GET', 'POST'], strict_slashes=False)
def get_all_user_obj():
    ''' Retrieves the list of all User objects '''
    if request.method == "POST":
        HTTP_body = request.get_json()
        if not HTTP_body:
            return Response("Not a JSON", 400)
        if 'email' not in HTTP_body:
            return Response("Missing email", 400)
        if 'password' not in HTTP_body:
            return Response("Missing password", 400)
        new_user = User(email=HTTP_body.get('email'),
                        password=HTTP_body.get('password'))
        new_user.save()
        return (jsonify(new_user.to_dict()), 201)

    All_Users = storage.all('User')
    Existing_Users = []

    for u in All_Users.values():
        Existing_Users.append(u.to_dict())
    return jsonify(Existing_Users)


@app_views.route('/users/<user_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def get_a_user(user_id=None):
    ''' Retrives, Deleted or Updates a specified User '''
    a_user = storage.get(User, user_id)
    if a_user is None:
        abort(404)

    if request.method == "DELETE":
        storage.delete(a_user)
        storage.save()
        return (jsonify({}), 200)

    if request.method == "PUT":
        HTTP_body = request.get_json()
        if not HTTP_body:
            return Response("Not a JSON", 400)
        HTTP_body['id'] = a_user.id
        HTTP_body['created_at'] = a_user.created_at
        HTTP_body['email'] = a_user.email
        a_user.__init__(**HTTP_body)
        a_user.save()
        return (jsonify(a_user.to_dict()), 200)
    return jsonify(a_user.to_dict())
