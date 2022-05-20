#!/usr/bin/python3

from api.v1.views import app_views
from flask import make_response
from models import storage

@app.route('/status')
def status():
    return app_views(jsonify({'status': 'OK'}))

@app.route('/api/v1/stats')
def stats():
    return storage(jsonify({'{}'.format(storage.get()): '{}'.format(storage.count())}))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(HBNB_API_HOST = "0.0.0.0", HBNB_API_PORT = 5000, threaded = True)
