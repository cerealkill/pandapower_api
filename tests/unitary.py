import json
import unittest

from api.controllers.controller import SimulationController
from api.server import api_v1


class SimulationControllerTest(unittest.TestCase):

    def setUp(self):
        self.controller = SimulationController()

    def test_get_active_load_fails(self):
        with self.assertRaises(Exception):
            self.controller.active_load

    def test_get_reactive_load_fails(self):
        with self.assertRaises(Exception):
            self.controller.reactive_load

    def test_run_simulation(self):
        active_load, reactive_load = self.controller.simulate_and_store()
        self.assertEqual(active_load, 0.1)
        self.assertEqual(reactive_load, 0.05)

    def test_get_active_load(self):
        self.controller.simulate_and_store()
        self.assertEqual(self.controller.active_load, 0.1)

    def test_get_reactive_load(self):
        self.controller.simulate_and_store()
        self.assertEqual(self.controller.reactive_load, 0.05)


class RestAPIv1Test(unittest.TestCase):

    def setUp(self):
        api_v1.config['TESTING'] = True
        self.app = api_v1.test_client()

    def test_hello_world(self):
        helloworld = self.app.get('/')
        self.assertEqual(helloworld.status_code, 200)
        self.assertEqual(helloworld.json, {"Hello": "World!"})

    def test_echo(self):
        helloworld = self.app.post('/echo', data=json.dumps({'Hello': 'Again!'}))
        self.assertEqual(helloworld.status_code, 200)
        self.assertEqual(helloworld.json, {"Hello": "Again!"})

    def test_run_simulation(self):
        simulation_res = self.app.post('/api/v1/run')
        self.assertEqual(simulation_res.status_code, 200)
        self.assertEqual(simulation_res.json, {'results': {'active_load': 0.1, 'reactive_load': 0.05}})

    def test_get_active_load(self):
        self.app.post('/api/v1/run')
        simulation_res = self.app.get('/api/v1/load/active')
        self.assertEqual(simulation_res.status_code, 200)
        self.assertEqual(simulation_res.json, {'results': {'active_load': 0.1}})

    def test_get_reactive_load(self):
        self.app.post('/api/v1/run')
        simulation_res = self.app.get('/api/v1/load/reactive')
        self.assertEqual(simulation_res.status_code, 200)
        self.assertEqual(simulation_res.json, {'results': {'reactive_load': 0.05}})
