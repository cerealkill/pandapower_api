"""
TODO:  Unfortunately flask-restful-swagger is outdatedand this code does not work. will create a PR later to fix it.
https://github.com/rantav/flask-restful-swagger/issues/123
"""
from flask_restful_swagger import swagger


@swagger.model
class SimulationIndex:
    """
    Power grid simulation results.
    """

    def __init__(self, sim_id: str, active_load: float, reactive_load: float):
        self.sim_id = sim_id
        self.results = SimulationResults(active_load, reactive_load)


@swagger.model
class SimulationResults:
    """
    Power grid simulation results.
    """

    def __init__(self, active_load: float, reactive_load: float):
        self.load = Load(active_load, reactive_load)


@swagger.model
class Load:
    """
    Power grid load.
    """

    def __init__(self, active_load: float, reactive_load: float):
        self.active = active_load
        self.reactive = reactive_load
