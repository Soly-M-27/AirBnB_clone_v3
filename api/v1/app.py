#!/usr/bin/python3
''' Your first endpoint (route) will be to return the status of your API '''

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from models import storage


app = Flask(__name__)
app.resgister_blueprint(app_views)


@app.teardown_appcontext
def close(self):
    storage.close()


if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST", "0.0.0.0"),
            port=int(getenv("HBNB_API_PORT", "5000")), threaded=True)
