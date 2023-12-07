
from Day5 import Map, Range

import unittest

class TestRange(unittest.TestCase):
    def setUp(self):
        self.range_instance = Range(50, 98, 2)

    def test_range_contains(self):
        self.assertNotIn(97, self.range_instance)
        self.assertIn(98, self.range_instance)
        self.assertIn(99, self.range_instance)
        self.assertNotIn(100, self.range_instance)
        self.assertNotIn(50, self.range_instance)

    def test_range_getitem(self):
        with self.assertRaises(KeyError):
            self.range_instance[97]

        self.assertEqual(self.range_instance[98], 50)
        self.assertEqual(self.range_instance[99], 51)

        with self.assertRaises(KeyError):
            self.range_instance[90]

        with self.assertRaises(KeyError):
            self.range_instance[50]

    def test_range_map_range(self):
        other_range = Range(0, 48, 5)
        mapped_ranges = self.range_instance[other_range]
        self.assertIsInstance(mapped_ranges, list)
        self.assertIsInstance(mapped_ranges[0], Range)
        self.assertEqual(mappend_range.source)
            

class TestMap(unittest.TestCase):
    def setUp(self):
        self.map_instance = Map([ Range(50, 98, 2), Range(52, 50, 48) ])

    def test_getitem(self):
        self.assertEqual(self.map_instance[98], 50)
        self.assertEqual(self.map_instance[99], 51)
        self.assertEqual(self.map_instance[100], 100)
        self.assertEqual(self.map_instance[50], 52)
        self.assertEqual(self.map_instance[60], 62)
        self.assertEqual(self.map_instance[97], 99)
        self.assertEqual(self.map_instance[49], 49)
        self.assertEqual(self.map_instance[0], 0)
        self.assertEqual(self.map_instance[10000], 10000)

if __name__ == '__main__':
    unittest.main()