#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, make_response, jsonify
from models import storage
import os
from api.v1.views import app_views
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)

cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}},
            methods=['GET', 'PUT', 'DELETE', 'POST'])


@app.teardown_appcontext
def close(exception=None):
    """close method"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """return a json with 404 error"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    host = None
    port = None
    if os.getenv('HBNB_API_HOST'):
        host = os.getenv('HBNB_API_HOST')
    else:
        host = '0.0.0.0'
    if os.getenv('HBNB_API_PORT'):
        port = int(os.getenv('HBNB_API_PORT'))
    else:
        port = 5000
    app.run(host=host, port=port, threaded=True)
