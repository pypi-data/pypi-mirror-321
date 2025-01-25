#!/usr/bin/env python

import os
import unittest
from atooms.trajectory import TrajectoryXYZ
from atooms.simulation import Simulation
from atooms.core.utils import rmd, rmf
import atooms.backends.lammps
from atooms.backends.lammps import LAMMPS, Interaction

atooms.backends.lammps.lammps_command = 'lmp'
SKIP = not atooms.backends.lammps.installed()

class Test(unittest.TestCase):

    def setUp(self):
        if SKIP:
            self.skipTest('missing LAMMPS')
        self.input_file = os.path.join(os.path.dirname(__file__),
                                       '../data/lj_N1000_rho1.0.xyz')

    def test_single(self):
        cmd = """
        pair_style      lj/cut 2.5
        pair_coeff      1 1 1.0 1.0 2.5
        neighbor        0.3 bin
        neigh_modify    every 20 delay 0 check no
        fix             1 all nve
        """
        bck = LAMMPS(self.input_file, cmd)
        sim = Simulation(bck)
        x = sim.system.particle[0].position[0]
        self.assertAlmostEqual(x, 3.62635, places=5)
        sim.run(10)
        x = sim.system.particle[0].position[0]
        self.assertAlmostEqual(x, 3.64526, places=5)
        sim.run(10)
        x = sim.system.particle[0].position[0]
        self.assertAlmostEqual(x, 3.675987, places=5)

    def test_nvt(self):
        import random
        cmd = """
        pair_style      lj/cut 2.5
        pair_coeff      1 1 1.0 1.0 2.5
        neighbor        0.3 bin
        neigh_modify    every 20 delay 0 check no
        fix             1 all nvt temp 2.0 2.0 0.2
        timestep        0.002
        """

        def store(sim, T, U):
            T.append(sim.system.temperature)
            U.append(sim.system.potential_energy(per_particle=True))

        with TrajectoryXYZ(self.input_file) as th:
            system = th[-1]

        for inp in [self.input_file, TrajectoryXYZ(self.input_file),
                    system]:
            T, U = [], []
            random.seed(1)
            bck = LAMMPS(inp, cmd)
            sim = Simulation(bck)
            sim.system.temperature = 1.5
            sim.add(store, 500, T, U)
            sim.run(2000)
            ave = sum(T[3:]) / len(T[3:])
            self.assertAlmostEqual(ave, 2.0, places=1)
            if isinstance(inp, TrajectoryXYZ):
                inp.close()

    def test_nvt_nofix(self):
        import random
        from atooms.system import Thermostat
        cmd = """
        pair_style      lj/cut 2.5
        pair_coeff      1 1 1.0 1.0 2.5
        neighbor        0.3 bin
        neigh_modify    every 20 delay 0 check no
        timestep        0.002
        """
        random.seed(1)
        T = []

        def store(sim, T):
            T.append(sim.system.temperature)
        bck = LAMMPS(self.input_file, cmd)
        sim = Simulation(bck)
        sim.system.temperature = 1.4
        sim.system.thermostat = Thermostat(2.0)
        sim.add(store, 500, T)
        sim.run(4000)
        ave = sum(T[3:]) / len(T[3:])
        self.assertAlmostEqual(ave, 2.0, places=1)

    def test_energy(self):
        cmd = """
        pair_style      lj/cut 2.5
        pair_coeff      1 1 1.0 1.0 2.5
        """
        bck = LAMMPS(self.input_file, cmd)
        bck.system.interaction.compute("energy", bck.system.particle, bck.system.cell)
        self.assertEqual(bck.system.interaction.energy / len(bck.system.particle), -4.2446836)  # crosschecked

        # Relaxed FCC
        bck = LAMMPS(os.path.join(os.path.dirname(__file__),
                                  '../data/lj_fcc_N108.xyz'), cmd)
        bck.system.interaction.compute("forces", bck.system.particle, bck.system.cell)
        # Test norm of force per particle
        U = bck.system.potential_energy(per_particle=True)
        W = bck.system.force_norm(per_particle=True)
        P = bck.system.pressure
        self.assertAlmostEqual(U, -7.7615881, places=7)
        self.assertAlmostEqual(W, 4.2e-11, places=2)
        self.assertAlmostEqual(P, -3.3935748, places=7)

    def test_roundoff(self):
        cmd = """
        pair_style      lj/cut 2.5
        pair_coeff      1 1 1.0 1.0 2.5
        neighbor        0.3 bin
        neigh_modify    every 20 delay 0 check no
        fix             1 all nve
        """
        import numpy
        numpy.set_printoptions(precision=15)
        bck = LAMMPS(self.input_file, cmd)
        bck.run(10)
        x1 = bck.system.particle[3].position[0]
        bck.run(0)
        x2 = bck.system.particle[3].position[0]
        # The difference should be of order of machine precision
        # Unfortunately, without packing/unpacking data in binary
        # format, we cannot maintain coehrence at machine precision
        self.assertAlmostEqual(abs(x2-x1), 0.0, places=12)

    def tearDown(self):
        rmd('/tmp/test_lammps.d')
        rmf('/tmp/test_lammps*')


if __name__ == '__main__':
    unittest.main()
