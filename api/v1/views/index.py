#!/usr/bin/python3
''' It’s time to start your API! '''

from flask import make_response, jsonify
from api.v1.views import app_views
from models import storage
from os import getenv


@app_views.route('/status')
def status():
    return jsonify({'status': 'OK'})


@app.route('/api/v1/stats')
def stats():
    return storage(jsonify({'{}'.
                   format(storage.get()): '{}'.format(storage.count())}))


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST", "0.0.0.0"),
            port=int(getenv("HBNB_API_PORT", "5000")), threaded=True)
