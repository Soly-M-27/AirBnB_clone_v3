#!/usr/bin/python3
''' It’s time to start your API! '''

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def status():
    ''' route status test that return a JSON query '''
    return jsonify({'status': 'OK'})
