import unittest
import numpy as np

from src.vec3d import Vec3D

class TestVec3D(unittest.TestCase):

    def test_init(self):
        v = Vec3D()
        self.assertTrue(np.allclose(v.vec, np.array([0.0, 0.0, 0.0])))

        v = Vec3D(np.array([1.0, 2.0, 3.0]))
        self.assertTrue(np.allclose(v.vec, np.array([1.0, 2.0, 3.0])))

        v = Vec3D(np.array([4.0, 5.0, 6.0]))
        self.assertTrue(np.allclose(v.vec, np.array([4.0, 5.0, 6.0])))

    def test_getters(self):
        v = Vec3D(np.array([1.0, 2.0, 3.0]))
        self.assertEqual(v.get_x(), 1.0)
        self.assertEqual(v.get_y(), 2.0)
        self.assertEqual(v.get_z(), 3.0)

    def test_negation(self):
        v = Vec3D(np.array([1.0, 2.0, 3.0]))
        neg_v = -v
        self.assertTrue(np.allclose(neg_v.vec, np.array([-1.0, -2.0, -3.0])))

    def test_addition(self):
        v1 = Vec3D(np.array([1.0, 2.0, 3.0]))
        v2 = Vec3D(np.array([4.0, 5.0, 6.0]))
        result = v1 + v2
        self.assertTrue(np.allclose(result.vec, np.array([5.0, 7.0, 9.0])))

    def test_subtraction(self):
        v1 = Vec3D(np.array([1.0, 2.0, 3.0]))
        v2 = Vec3D(np.array([4.0, 5.0, 6.0]))
        result = v1 - v2
        self.assertTrue(np.allclose(result.vec, np.array([-3.0, -3.0, -3.0])))

    def test_multiplication(self):
        v1 = Vec3D(np.array([1.0, 2.0, 3.0]))
        c = 2.0
        result = v1 * c
        self.assertTrue(np.allclose(result.vec, np.array([2.0, 4.0, 6.0])))
    
    def test_division(self):
        v1 = Vec3D(np.array([1.0, 2.0, 3.0]))
        c = 2
        result = v1 / c
        self.assertTrue(np.allclose(result.vec, np.array([0.5, 1.0, 1.5])))

    def test_length(self):
        v1 = Vec3D(np.array([0.0, 4.0, 3.0]))
        self.assertTrue(np.isclose(5.0, v1.length()))

        v2 = Vec3D(np.array([0.0, 0.0, 0.0]))
        self.assertFalse(np.isclose(1.0, v2.length()))
    
    def test_length_squared(self):
        v1 = Vec3D(np.array([0.0, 4.0, 3.0]))
        self.assertTrue(np.isclose(25.0, v1.length_squared()))

    def test_dot(self):
        v1 = Vec3D(np.array([1.0, 2.0, 3.0]))
        v2 = Vec3D(np.array([4.0, 5.0, 6.0]))
        result = v1.dot(v2)
        self.assertTrue(np.isclose(result, 32.0))
    
    def test_cross(self):
        v1 = Vec3D(np.array([1.0, 2.0, 3.0]))
        v2 = Vec3D(np.array([4.0, 5.0, 6.0]))
        result = v1.cross(v2)
        self.assertTrue(np.allclose(result.vec, np.array([-3.0, 6.0, -3.0])))

    def test_string(self):
        v1 = Vec3D(np.array([1.0, 2.0, 3.0]))
        result = str(v1)
        self.assertTrue(result, '1.0 2.0 3.0')

if __name__ == '__main__':
    unittest.main()
