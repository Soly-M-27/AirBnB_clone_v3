#!/usr/bin/python3

from api.v1.views import app_views

@app.route('/status')
def status():
    return app_views(jsonify({'status': 'OK'}))
