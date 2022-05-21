#!/usr/bin/python3
''' It’s time to start your API! '''

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def status():
    return jsonify({'status': 'OK'})
