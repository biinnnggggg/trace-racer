import unittest
import numpy as np

from src.vec3d import Vec3D

class TestVec3D(unittest.TestCase):

    def test_init(self):
        v = Vec3D(1.0, 2.0, 3.0)
        u = Vec3D(1.0, 2.0, 3.0)
        self.assertEqual(v, u)

    def test_copy(self):
        vec = Vec3D(1.0, 2.0, 3.0)
        copied_vec = Vec3D.copy(vec)
        expected = Vec3D(1.0, 2.0, 3.0)
        self.assertEqual(copied_vec, expected)

        vec = Vec3D(1.0, 2.0, 3.0)
        copied_vec = Vec3D.copy(vec)
        not_expected = Vec3D(2.0, 2.0, 3.0)
        self.assertNotEqual(copied_vec, not_expected)

    def test_of(self):
        vec = np.array([1.0, 2.0, 3.0])
        vec3d = Vec3D.of(vec)
        expected = Vec3D(1.0, 2.0, 3.0)
        self.assertEqual(vec3d, expected)

    def test_zero(self):
        zero_vec = Vec3D.zero()
        expected = Vec3D(0.0, 0.0, 0.0)
        self.assertEqual(zero_vec, expected)

    def test_rand(self):
        rand_vec = Vec3D.rand()
        self.assertTrue(all(0 <= x < 1 for x in rand_vec.vec))

    def test_rand_in(self):
        a, b = 2, 5
        rand_vec = Vec3D.rand_in(a, b)
        self.assertTrue(all(a <= x < b for x in rand_vec.vec))

    def test_rand_in_unit_sphere(self):
        rand_vec = Vec3D.rand_in_unit_sphere()
        self.assertTrue(rand_vec.length() < 1)

    def test_rand_unit_vector(self):
        rand_unit_vec = Vec3D.rand_unit_vector()
        self.assertAlmostEqual(rand_unit_vec.length(), 1)

    def test_rand_on_hemisphere(self):
        normal = Vec3D(0, 0, 1)
        rand_vec = Vec3D.rand_on_hemisphere(normal)
        self.assertGreaterEqual(rand_vec.dot(normal), 0)

    def test_getters(self):
        v = Vec3D(1.0, 2.0, 3.0)
        self.assertEqual(v.get_x(), 1.0)
        self.assertEqual(v.get_y(), 2.0)
        self.assertEqual(v.get_z(), 3.0)

    def test_negation(self):
        v = Vec3D(1.0, 2.0, 3.0)
        result = -v
        expected = Vec3D(-1.0, -2.0, -3.0)
        self.assertEqual(result, expected)

    def test_addition(self):
        v1 = Vec3D(1.0, 2.0, 3.0)
        v2 = Vec3D(4.0, 5.0, 6.0)
        result = v1 + v2
        expected = Vec3D(5.0, 7.0, 9.0)
        self.assertEqual(result, expected)

    def test_subtraction(self):
        v1 = Vec3D(1.0, 2.0, 3.0)
        v2 = Vec3D(4.0, 5.0, 6.0)
        result = v1 - v2
        expected = Vec3D(-3.0, -3.0, -3.0)
        self.assertTrue(result, expected)

    def test_multiplication(self):
        v1 = Vec3D(1.0, 2.0, 3.0)
        c = 2.0
        result = v1 * c
        expected = Vec3D(2.0, 4.0, 6.0)
        self.assertEqual(result, expected)
    
    def test_division(self):
        v1 = Vec3D(1.0, 2.0, 3.0)
        c = 2
        result = v1 / c
        expected = Vec3D(0.5, 1.0, 1.5)
        self.assertEqual(result, expected)

    def test_length(self):
        v1 = Vec3D(0.0, 4.0, 3.0)
        result = v1.length()
        expected = 5.0
        self.assertAlmostEqual(result, expected)

        v2 = Vec3D(0.0, 0.0, 0.0)
        result = v2.length()
        not_expected = -1.0
        self.assertNotAlmostEqual(result, not_expected)
    
    def test_length_squared(self):
        v1 = Vec3D(0.0, 4.0, 3.0)
        result = v1.length_squared()
        expected = 25.0
        self.assertAlmostEqual(result, expected)

    def test_dot(self):
        v1 = Vec3D(1.0, 2.0, 3.0)
        v2 = Vec3D(4.0, 5.0, 6.0)
        result = v1.dot(v2)
        expected = 32.0
        self.assertAlmostEqual(result, expected)
    
    def test_cross(self):
        v1 = Vec3D(1.0, 2.0, 3.0)
        v2 = Vec3D(4.0, 5.0, 6.0)
        result = v1.cross(v2)
        expected = Vec3D(-3.0, 6.0, -3.0)
        self.assertTrue(result, expected)

    def test_string(self):
        v1 = Vec3D(1.0, 2.0, 3.0)
        result = str(v1)
        expected = '1.0 2.0 3.0'
        self.assertTrue(result, expected)

if __name__ == '__main__':
    unittest.main()
