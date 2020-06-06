import pandapower as pp


def run_simulation():
    # create empty net
    net = pp.create_empty_network()

    # create buses
    b1 = pp.create_bus(net, vn_kv=20., name="Bus 1")
    b2 = pp.create_bus(net, vn_kv=0.4, name="Bus 2")
    b3 = pp.create_bus(net, vn_kv=0.4, name="Bus 3")

    # create bus elements
    pp.create_ext_grid(net, bus=b1, vm_pu=1.02, name="Grid Connection")
    pp.create_load(net, bus=b3, p_mw=0.1, q_mvar=0.05, name="Load")

    # create branch elements
    tid = pp.create_transformer(net, hv_bus=b1, lv_bus=b2, std_type="0.4 MVA 20/0.4 kV", name="Trafo")
    pp.create_line(net, from_bus=b2, to_bus=b3, length_km=0.1, name="Line",std_type="NAYY 4x50 SE")
    pp.runpp(net)
    return net.res_load.p_mw[0], net.res_load.q_mvar[0]


if __name__ == '__main__':
    message = "\n\t -=Simulation Results =- " \
              "\nNetwork Load Power: {} megawatts" \
              "\nNetwork Load Reactive Power: {} megawatts"
    print(message.format(*run_simulation()))
