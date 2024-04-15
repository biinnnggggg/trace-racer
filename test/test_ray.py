import unittest
import numpy as np

from src.vec3d import Vec3D, Point3D
from src.ray import Ray

class TestRay(unittest.TestCase):
    def setUp(self):
        origin = Point3D(1, 2, 3)
        direction = Vec3D(0, 1, 0)
        self.ray = Ray(origin, direction)

    def test_at(self):
        # Test for t = 0
        expected = Point3D(1, 2, 3)
        result = self.ray.at(0)
        self.assertEqual(result, expected)

        # Test for t = 1
        expected = Point3D(1, 3, 3)
        result = self.ray.at(1)
        self.assertEqual(result, expected)

        # Test for t = -1
        expected = Point3D(1, 1, 3)
        result = self.ray.at(-1)
        self.assertEqual(result, expected)

        # Test for arbitrary t
        t = 2.5
        expected = Point3D(1, 2 + t, 3)
        result = self.ray.at(t)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()