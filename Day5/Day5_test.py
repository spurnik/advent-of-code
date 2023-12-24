
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
		# There are four cases to test:
        totally_overlapped_range = Range(99, 100, 1) # source is 100
        self.assertTrue(totally_overlapped_range in self.range_instance)
        mapped_totally_overlapped_range = self.range_instance[totally_overlapped_range]
        self.assertIsInstance(mapped_totally_overlapped_range , list)
        self.assertIsInstance(mapped_totally_overlapped_range[0], Range)
        self.assertListEqual(mapped_totally_overlapped_range, [ Range(51, 100, 1) ])

        initial_overlapping_range = Range(99, 99, 3) # seeds 99, 100, 101
        self.assertTrue(initial_overlapping_range in self.range_instance)
        mapped_initial_overlapping_range = self.range_instance[initial_overlapping_range ]
        self.assertListEqual(mapped_initial_overlapping_range, [ Range(51, 99, 1), Range(100, 100, 2) ])

        final_overlapping_range = Range(96, 30, 3) # source within 30, 31, 32
        self.assertTrue(final_overlapping_range in self.range_instance)
        mapped_final_overlapping_range = self.range_instance[final_overlapping_range]
        self.assertListEqual(mapped_final_overlapping_range, [ Range(96, 30, 2), Range(50, 32, 1) ])

        non_overlapping_range = Range(96, 96, 2) # seeds 96, 97
        self.assertFalse(non_overlapping_range in self.range_instance)
        mapped_non_overlapping_range = self.range_instance[non_overlapping_range]
        self.assertListEqual(mapped_non_overlapping_range, [ non_overlapping_range ])

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

    def test_getitem_for_range(self):
        # again, four cases:
        range_within_first_map_range = Range(99, 100, 1)
        range_within_second_map_range = Range(60, 0, 38)
        range_within_all_map_ranges = Range(60, 0, 39)
        range_out_of_any_map_range = Range(101, 0, 10)

        # resulting mappings
        mapped_range_within_first_map_range = self.map_instance[range_within_first_map_range]
        mapped_range_within_second_map_range = self.map_instance[range_within_second_map_range]
        mapped_range_within_all_map_ranges = self.map_instance[range_within_all_map_ranges]
        mapped_range_out_of_any_map_range = self.map_instance[range_out_of_any_map_range]

        # assertions
        self.assertListEqual(mapped_range_within_first_map_range, [ Range(51, 100, 1) ])
        self.assertListEqual(mapped_range_within_second_map_range, [ Range(62, 0, 38) ])
        self.assertListEqual(mapped_range_within_all_map_ranges, [ Range(50, 38, 1), Range(62, 0, 38) ])
        self.assertListEqual(mapped_range_out_of_any_map_range, [ Range(101, 0, 10) ])

if __name__ == '__main__':
    unittest.main()