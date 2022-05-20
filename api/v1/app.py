#!/usr/bin/python3
''' Your first endpoint (route) will be to return the status of your API '''

from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask("app_views", __name__)

@app.teardown_appcontext
def close():
    storage.close()

if __name__ == "__main__":
    app.run(HBNB_API_HOST = "0.0.0.0", HBNB_API_PORT = 5000, threaded = True)
