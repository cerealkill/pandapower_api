from flask_restful import reqparse, abort, Resource
from flask_restful_swagger import swagger
from pandapower import ppException

from api.controllers.simulation import SimulationController

parser = reqparse.RequestParser()
parser.add_argument('active', type=float, help='Active load must be a float.')
parser.add_argument('reactive', type=float, help='Active load must be a float.')

# Static variable storing the state in memory
simulations = {
    '0': {'results': {'load': {'active': 0.1, 'reactive': 0.05}}, 'id': 0},
    # '1': SimulationIndex('1', 0.4, 0.6)
}


def abort_if_doesnt_exist(sim_id):
    if sim_id not in simulations:
        abort(404, message="Simulation of id {}  doesn't exist".format(sim_id))


def simulate_and_store(active_load, reactive_load, sim_id):
    pp_sim = SimulationController()
    results = pp_sim.run_simulation(active_load, reactive_load)
    simulations[sim_id] = {'results': {'load': {'active': results[0], 'reactive': results[1]}}, 'id': sim_id}


class Simulation(Resource):

    @swagger.operation(
        notes='Gets simulation by id provided in the url.',
        responseMessages=[
            {
                "code": 404,
                "message": "Simulation with provided ID was not found."
            }
        ]
    )
    def get(self, sim_id):
        abort_if_doesnt_exist(sim_id)
        return simulations[sim_id]

    @swagger.operation(
        notes='Deletes simulation by id provided in the url.',
        responseMessages=[
            {
                "code": 204,
                "message": "Simulation successfully Deleted."
            },
            {
                "code": 404,
                "message": "Simulation with provided ID was not found."
            }
        ]
    )
    def delete(self, sim_id):
        abort_if_doesnt_exist(sim_id)
        del simulations[sim_id]
        return '', 204

    @swagger.operation(
        notes='Creates or replaces a simulation of specific id, with grid load specified in the active and reactive '
              'body parameters in the multipart/form-data format. Defaults are 0.1 active and 0.05 reactive grid load.',
        responseMessages=[
            {
                "code": 201,
                "message": "Created."
            },
            {
                "code": 404,
                "message": "Simulation with provided ID was not found."
            },
            {
                "code": 417,
                "message": "Simulation failed. See error message in response body."
            },
        ]
    )
    def put(self, sim_id):
        args = parser.parse_args()
        active_load, reactive_load = args['active'], args['reactive']
        try:
            simulate_and_store(active_load, reactive_load, sim_id)
            return simulations[sim_id], 201
        except ppException as e:
            return {'error': str(e)}, 417


class SimulationList(Resource):

    @swagger.operation(
        notes='Gets a list of all existing simulations.',
    )
    def get(self):
        return simulations

    @swagger.operation(
        notes='Creates a simulation with grid load specified in the active and reactive body parameters in '
              'the multipart/form-data format. Defaults are 0.1 active and 0.05 reactive grid load.'
              'Simulation id is in the response body in json format.',
        responseMessages=[
            {
                "code": 400,
                "message": "Malformed body. Active and Reactive load must be floating points."
            },
            {
                "code": 417,
                "message": "Simulation failed. See error message in response body."
            },
            {
                "code": 201,
                "message": "Created. Simulation ID is in the message body."
            }
        ]
    )
    def post(self):
        args = parser.parse_args()
        active_load, reactive_load = args['active'], args['reactive']
        try:
            sim_id = str(int(max(simulations.keys())) + 1) if len(simulations) > 0 else '0'
            simulate_and_store(active_load, reactive_load, sim_id)
            # TODO: Add response resource location header
            return simulations[sim_id], 201
        except ppException as e:
            return {'error': str(e)}, 417


class Load(Resource):

    @swagger.operation(
        notes='Gets specific load by simulation id and load type provided in the url.',
        responseMessages=[
            {
                "code": 404,
                "message": "Simulation with provided ID was not found."
            }
        ]
    )
    def get(self, **kwargs):
        load_type, sim_id = kwargs['load_type'], kwargs['sim_id']
        abort_if_doesnt_exist(sim_id)
        return {'value': simulations[sim_id]['results']['load'][load_type]}
