import unittest
from day5 import get_map_ranges, recursive_convert


class Day5Test(unittest.TestCase):
    def setUp(self):
        with open('day5-test-input.txt', 'r') as f:
            self.lines = f.readlines()

            # Manual run to get map ranges
            self.map_ranges = [
                [3, 5],
                [7, 10],
                [12, 16],
                [18, 20],
                [22, 25],
                [27, 29],
                [31, -1]
            ]

    def test_get_map_ranges(self):
        # Check computed map ranges match up with the manual run
        self.assertEqual(
            get_map_ranges(self.lines),  # Computed
            self.map_ranges  # Manual
        )

    def test_recursive_convert(self):
        # Example final conversions from the question
        expected = [82, 43, 86, 35]

        # Check recursive_convert yields the same results
        res = [
            recursive_convert(seed, 0, self.map_ranges, self.lines)
            for seed in [79, 14, 55, 13]
        ]

        self.assertEqual(res, expected)


if __name__ == '__main__':
    unittest.main()
