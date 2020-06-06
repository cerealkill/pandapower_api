import unittest

import pytest

from api.controller import SimulationController


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
