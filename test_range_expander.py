
import unittest
from range_expander import expand_ranges

class TestStage6(unittest.TestCase):
    def test_step_forward(self):
        self.assertEqual(expand_ranges("1-10:2"), [1, 3, 5, 7, 9])

    def test_step_backward(self):
        self.assertEqual(expand_ranges("10-1:3"), [1, 4, 7, 10])  # sorted output

    def test_step_equal_range(self):
        self.assertEqual(expand_ranges("3-3:1"), [3])

    def test_missing_step_in_reverse(self):
        self.assertEqual(expand_ranges("5-2"), [2, 3, 4, 5])  # sorted output

    def test_step_auto_fix_negative(self):
        self.assertEqual(expand_ranges("1-5:-1"), [1, 2, 3, 4, 5])

    def test_invalid_step_value(self):
        with self.assertRaises(ValueError):
            expand_ranges("1-5:xyz")

    # Stage 6 tests
    def test_overlapping_ranges(self):
        self.assertEqual(expand_ranges("1-3,2-5"), [1, 2, 3, 4, 5])

    def test_duplicate_numbers(self):
        self.assertEqual(expand_ranges("2,2,2-4"), [2, 3, 4])

    def test_reverse_overlap(self):
        self.assertEqual(expand_ranges("5-3,3-1"), [1, 2, 3, 4, 5])

    def test_full_overlap(self):
        self.assertEqual(expand_ranges("1-5,2-4"), [1, 2, 3, 4, 5])

    def test_with_whitespace_and_commas(self):
        self.assertEqual(expand_ranges(" , 1-3 , , 2-4 , 3 "), [1, 2, 3, 4])

    def test_unsorted_duplicates(self):
        self.assertEqual(expand_ranges("4,2,2,1-3"), [1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()
