#!/usr/bin/python3
''' Your first endpoint (route) will be to return the status of your API '''

from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask("app_views", __name__)

host = getenv("HBNB_API_HOST")
port = getenv("HBNB_API_PORT")

if not host:
    host = "0.0.0.0"
if not port:
    port = "5000"

@app.teardown_appcontext
''' storage.close() '''
def close():
    storage.close()

if __name__ == "__main__":
    app.run(host=host, port=port, threaded = True)
