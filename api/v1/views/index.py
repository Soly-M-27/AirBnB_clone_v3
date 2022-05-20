#!/usr/bin/python3
''' It’s time to start your API! '''

from api.v1.views import app_views
from flask import make_response, jsonify
from models import storage

@app_views.route('/status')
def status():
    ''' return json dic of status '''
    return jsonify({'status': 'OK'})

@app.route('/api/v1/stats')
def stats():
    ''' Return dictionary on json format 
    with all classes and their values '''
    return storage(jsonify({'{}'.format(storage.get()): '{}'.format(storage.count())}))

@app.errorhandler(404)
''' Send 404 error '''
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

''' Check host and port through get env '''
host = getenv("HBNB_API_HOST")
port = getenv("HBNB_API_PORT")

if not host:
    host = "0.0.0.0"
if not port:
    port = "5000"

if __name__ == "__main__":
    app.run(host=host, port=port, threaded = True)
