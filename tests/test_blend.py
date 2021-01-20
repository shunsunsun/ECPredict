import unittest
from ecpredict import *

smiles = ['CCC', 'CCCC', 'CCCCC']
known_vals = [40.0, 50, 55.0]
mix = ['CCC', 50, 'CCCC']


class TestBlends(unittest.TestCase):

    def test_cn_blend(self):

        cetane_number_blend(smiles, (0.4, 0.25, 0.35))
        result = cetane_number_blend(known_vals, (0.4, 0.25, 0.35))
        self.assertEqual(result[0], 47.75)
        self.assertEqual(result[1], 0)
        cetane_number_blend(mix, (0.4, 0.25, 0.35))

    def test_cp_blend(self):

        cloud_point_blend(smiles, (0.4, 0.25, 0.35))
        cloud_point_blend(known_vals, (0.4, 0.25, 0.35))
        cloud_point_blend(mix, (0.4, 0.25, 0.35))

    def test_lhv_blend(self):

        lower_heating_value_blend(smiles, (0.4, 0.25, 0.35))
        lower_heating_value_blend(known_vals, (0.4, 0.25, 0.35))
        lower_heating_value_blend(mix, (0.4, 0.25, 0.35))

    def test_kv_blend(self):

        kinematic_viscosity_blend(smiles, (0.4, 0.25, 0.35))
        kinematic_viscosity_blend(known_vals, (0.4, 0.25, 0.35))
        kinematic_viscosity_blend(mix, (0.4, 0.25, 0.35))

    def test_ysi_blend(self):

        yield_sooting_index_blend(smiles, (0.4, 0.25, 0.35))
        result = yield_sooting_index_blend(known_vals, (0.4, 0.25, 0.35))
        self.assertEqual(result[0], 47.75)
        self.assertEqual(result[1], 0)
        yield_sooting_index_blend(mix, (0.4, 0.25, 0.35))


if __name__ == '__main__':

    unittest.main()
