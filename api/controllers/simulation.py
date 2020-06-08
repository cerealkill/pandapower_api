"""
1. POST request that launches the simulation using the aforementioned Python module. The response should include the active and reactive power of the load in JSON format
2. GET request that reads the active power of the previously executed simulation
3. GET request that reads the reactive power of the previously executed simulation
"""

import pandapower as pp


class SimulationController:

    def __init__(self):
        self._active_load, self._reactive_load = None, None

    def run_simulation(self, active_load=0.1, reactive_load=0.05) -> (float, float):
        """
        Runs the Pandaspower simulation with 3 buses, a 0.4 MVA 20/0.4 kV transformer, and an external grid connection.
        :param active_load: Grid active load in megawatts. Default is 0.1.
        :param reactive_load: Grid reactive load in megawatts. Default is 0.05.
        :return: Resulting active and reactive grid load.
        """
        # fallback parameters
        if not active_load:
            active_load = 0.1
        if not reactive_load:
            reactive_load = 0.05

        # create empty net
        net = pp.create_empty_network()

        # create buses
        b1 = pp.create_bus(net, vn_kv=20., name="Bus 1")
        b2 = pp.create_bus(net, vn_kv=0.4, name="Bus 2")
        b3 = pp.create_bus(net, vn_kv=0.4, name="Bus 3")

        # create bus elements
        pp.create_ext_grid(net, bus=b1, vm_pu=1.02, name="Grid Connection")
        pp.create_load(net, bus=b3, p_mw=active_load, q_mvar=reactive_load, name="Load")

        # create branch elements
        pp.create_transformer(net, hv_bus=b1, lv_bus=b2, std_type="0.4 MVA 20/0.4 kV", name="Trafo")
        pp.create_line(net, from_bus=b2, to_bus=b3, length_km=0.1, name="Line", std_type="NAYY 4x50 SE")
        pp.runpp(net)
        self._active_load, self._reactive_load = net.res_load.p_mw[0], net.res_load.q_mvar[0]
        return self._active_load, self._reactive_load

    @property
    def active_load(self) -> float:
        if not self._active_load:
            raise Exception('Please run simulation first.')
        return self._active_load

    @property
    def reactive_load(self) -> float:
        if not self._reactive_load:
            raise Exception('Please run simulation first.')
        return self._reactive_load


controller = SimulationController()
