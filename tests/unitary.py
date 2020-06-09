import unittest

from api.controllers.simulation import SimulationController
from api.server import rest


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
        active_load, reactive_load = self.controller.run_simulation()
        self.assertEqual(active_load, 0.1)
        self.assertEqual(reactive_load, 0.05)

    def test_get_active_load(self):
        self.controller.run_simulation()
        self.assertEqual(self.controller.active_load, 0.1)

    def test_get_reactive_load(self):
        self.controller.run_simulation()
        self.assertEqual(self.controller.reactive_load, 0.05)


class RestAPIv1Test(unittest.TestCase):

    def setUp(self):
        rest.config['TESTING'] = True
        self.app = rest.test_client()

    def test_get_active_load(self):
        self.app.post('/api/v1/run')
        simulation_res = self.app.get('/api/v1/simulation/0/load/active')
        self.assertEqual(simulation_res.status_code, 200)
        self.assertEqual(simulation_res.json, {'value': 0.1})

    def test_get_reactive_load(self):
        self.app.post('/api/v1/run')
        simulation_res = self.app.get('/api/v1/simulation/0/load/reactive')
        self.assertEqual(simulation_res.status_code, 200)
        self.assertEqual(simulation_res.json, {'value': 0.05})

    def test_get_simulation_by_id(self):
        simulation_res = self.app.get('/api/v1/simulation/0')
        self.assertEqual(simulation_res.status_code, 200)
        self.assertEqual(simulation_res.json, {'id': 0, 'results': {'load': {'active': 0.1, 'reactive': 0.05}}})

    def test_get_simulations_list(self):
        simulation_res = self.app.get('/api/v1/simulations')
        self.assertEqual(simulation_res.status_code, 200)
        self.assertEqual(simulation_res.json, {'0': {'id': 0, 'results': {'load': {'active': 0.1, 'reactive': 0.05}}}})

    def test_run_simulation(self):
        simulation_res = self.app.post('/api/v1/simulations')
        self.assertEqual(simulation_res.status_code, 201)
        self.assertEqual(simulation_res.json, {'id': '10', 'results': {'load': {'active': 0.1, 'reactive': 0.05}}})

    def test_run_simulation_raises(self):
        simulation_res = self.app.post('/api/v1/simulations', data=dict(active=0.9, reactive=0.8))
        self.assertEqual(simulation_res.status_code, 417)

    def test_put_simulation_replace(self):
        self.app.put('/api/v1/simulation/9', data=dict(active=0.4, reactive=0.01))
        simulation_res = self.app.put('/api/v1/simulation/9', data=dict(active=0.2, reactive=0.02))
        self.assertEqual(simulation_res.status_code, 201)
        self.assertEqual(simulation_res.json, {'id': '9', 'results': {'load': {'active': 0.2, 'reactive': 0.02}}})

    def test_put_simulation_new(self):
        simulation_res = self.app.put('/api/v1/simulation/8', data=dict(active=0.2, reactive=0.02))
        self.assertEqual(simulation_res.status_code, 201)

    def test_put_simulation_raises(self):
        simulation_res = self.app.put('/api/v1/simulation/1', data=dict(active=0.9, reactive=0.8))
        self.assertEqual(simulation_res.status_code, 417)

    def test_delete_simulation(self):
        self.app.put('/api/v1/simulation/5', data=dict(active=0.2, reactive=0.02))
        simulation_res = self.app.delete('/api/v1/simulation/5')
        self.assertEqual(simulation_res.status_code, 204)
