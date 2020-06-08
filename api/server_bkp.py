import logging

import flask
from flask import jsonify, request
from flask_swagger import swagger
from flask_cors import CORS

from api.controllers.controller import controller

rest = flask.Flask('pandapower_rest_api')

logging.basicConfig(level=logging.INFO)
logging.getLogger('flask_cors').level = logging.INFO
cors = CORS(rest, resources={r"/api/*": {"origins": "*"}})


@rest.route('/', methods=['GET'])
def hello():
    return flask.Response('{"Hello": "World!"}', status=200, mimetype='application/json')


@rest.route("/echo", methods=['POST'])
def echo():
    return jsonify(request.get_json(force=True))


@rest.route("/api/v1/run", methods=['POST'])
def run_simulation():
    active_load, reactive_load = controller.run_simulation()
    payload = {
        'simulation_results': {
            'active_load': active_load,
            'reactive_load': reactive_load
        }
    }
    return jsonify(payload)


@rest.route("/api/v1/load/active", methods=['GET'])
def get_active_load():
    try:
        payload = {
            'simulation_results': {
                'active_load': controller.active_load
            }
        }
        status = 200
    except Exception as e:
        payload = {
            'error': {
                'message': str(e)
            }
        }
        status = 404
    return jsonify(payload), status


@rest.route("/api/v1/load/reactive", methods=['GET'])
def get_reactive_load():
    try:
        payload = {
            'simulation_results': {
                'reactive_load': controller.reactive_load
            }
        }
        status = 200
    except Exception as e:
        payload = {
            'error': {
                'message': str(e)
            }
        }
        status = 404
    return jsonify(payload), status


@rest.route("/spec")
def spec():
    return jsonify(swagger(rest))


@rest.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request. %s', e)
    payload = {
        'error': {
            'status': 500,
            'message': str(e)
        }
    }
    return jsonify(payload), 500


if __name__ == '__main__':
    rest.run('0.0.0.0', 80)
