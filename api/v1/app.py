#!/usr/bin/python3
''' Your first endpoint (route) will be to return the status of your API '''

from api.v1.views import app_views
from flask import Flask
from os import getenv
from models import storage

app = Flask(__name__)
app.resgister_blueprint(app_views)

@app.teardown_appcontext
''' storage.close() '''
def close():
    storage.close()

''' Check host and port with getenv '''
host = getenv("HBNB_API_HOST")
port = getenv("HBNB_API_PORT")

if not host:
    host = "0.0.0.0"
if not port:
    port = "5000"

if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
