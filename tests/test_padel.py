import unittest
from ecpredict import *

smiles = ['CCC']


class TestProperties(unittest.TestCase):

    def test_cetane_number(self):

        cetane_number(smiles)

    def test_cloud_point(self):

        cloud_point(smiles)

    def test_heat_of_combustion(self):

        heat_of_combustion(smiles)

    def test_kinematic_viscosity(self):

        kinematic_viscosity(smiles)

    def test_motor_octane_number(self):

        motor_octane_number(smiles)

    def test_octane_sensitivity(self):

        octane_sensitivity(smiles)

    def test_pour_point(self):

        pour_point(smiles)

    def test_research_octane_number(self):

        research_octane_number(smiles)

    def test_yield_sooting_index(self):

        yield_sooting_index(smiles)


if __name__ == '__main__':

    unittest.main()
