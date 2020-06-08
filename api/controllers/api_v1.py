from flask_restful import reqparse, abort, Resource
from api.controllers.simulation import SimulationController

# parses
parser = reqparse.RequestParser()
parser.add_argument('active', type=float, help='Active load must be a float.')
parser.add_argument('reactive', type=float, help='Active load must be a float.')

# Static variable storing the state in memory
simulations = {
    '0': {'results': {'load': {'active': 0.1, 'reactive': 0.05}}, 'id': 0},
}


def abort_if_doesnt_exist(sim_id):
    if sim_id not in simulations:
        abort(404, message="Simulation of id {}  doesn't exist".format(sim_id))


class Simulation(Resource):

    def get(self, sim_id):
        abort_if_doesnt_exist(sim_id)
        return simulations[sim_id]

    def delete(self, sim_id):
        abort_if_doesnt_exist(sim_id)
        del simulations[sim_id]
        return '', 204

    def put(self, sim_id):
        args = parser.parse_args()
        active_load, reactive_load = args['active'], args['reactive']
        pp_sim = SimulationController()
        results = pp_sim.run_simulation(active_load, reactive_load)
        simulations[sim_id] = {'results': {'load': {'active': results[0], 'reactive': results[1]}}, 'id': sim_id}
        return simulations[sim_id], 201


class SimulationList(Resource):

    def get(self):
        return simulations

    def post(self):
        args = parser.parse_args()
        active_load, reactive_load = args['active'], args['reactive']
        pp_sim = SimulationController()
        results = pp_sim.run_simulation(active_load, reactive_load)
        sim_id = str(int(max(simulations.keys())) + 1) if len(simulations) > 0 else '0'
        simulations[sim_id] = {'results': {'load': {'active': results[0], 'reactive': results[1]}}, 'id': sim_id}
        return simulations[sim_id], 201


class Load(Resource):

    def get(self, **kwargs):
        load_type, sim_id = kwargs['load_type'], kwargs['sim_id']
        abort_if_doesnt_exist(sim_id)
        return {'value': simulations[sim_id]['results']['load'][load_type]}
