import logging

from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger

from api.controllers.api_v1 import SimulationList, Simulation, Load

rest = Flask(__name__)
api_v1 = swagger.docs(Api(rest), apiVersion='1.0')

logging.basicConfig(level=logging.INFO)
logging.getLogger('flask_cors').level = logging.INFO

api_v1.add_resource(SimulationList, '/api/v1/simulations')
api_v1.add_resource(Simulation, '/api/v1/simulation/<sim_id>')
api_v1.add_resource(Load, '/api/v1/simulation/<sim_id>/load/<load_type>')


if __name__ == '__main__':
    rest.run('0.0.0.0', 80)
