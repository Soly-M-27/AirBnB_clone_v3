#!/usr/bin/python3
''' It’s time to start your API! '''

from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review


@app_views.route('/status')
def status():
    ''' route status test that return a JSON query '''
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def get_count():
    ''' endpoint that retrieves the number of each
    objects by type '''
    stats = {
         "amenities": storage.count(Amenity),
         "cities": storage.count(City),
         "places": storage.count(Place),
         "reviews": storage.count(Review),
         "states": storage.count(State),
         "usres": storage.count(User)
    }
    return jsonify(stats)
