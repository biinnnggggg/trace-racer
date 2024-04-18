import unittest

from src.interval import Interval

class TestInterval(unittest.TestCase):
    def test_init(self):
        interval = Interval(0, 1)
        self.assertEqual(interval.min, 0)
        self.assertEqual(interval.max, 1)

    def test_size(self):
        interval = Interval(0, 1)
        self.assertEqual(interval.size(), 1)

    def test_surrounds(self):
        interval = Interval(0, 2)
        # inside
        self.assertTrue(interval.surrounds(1))

        # boundary cases
        self.assertFalse(interval.surrounds(0))
        self.assertFalse(interval.surrounds(2))
        
        # outside
        self.assertFalse(interval.surrounds(3))
        self.assertFalse(interval.surrounds(-1))

    def test_clamp(self):
        interval = Interval(0, 2)

        # inside
        self.assertEqual(1, interval.clamp(1))

        # boundary
        self.assertEqual(0, interval.clamp(0))
        self.assertEqual(2, interval.clamp(2))

        # outside
        self.assertEqual(0, interval.clamp(-1))
        self.assertEqual(2, interval.clamp(3))

    def test_contains(self):
        interval = Interval(0, 2)

        # inside
        self.assertTrue(interval.contains(1))
        
        # boundary cases
        self.assertTrue(interval.contains(0))
        self.assertTrue(interval.contains(2))
        
        # outside
        self.assertFalse(interval.contains(-1))
        self.assertFalse(interval.contains(3))

if __name__ == '__main__':
    unittest.main()