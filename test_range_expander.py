import unittest
from range_expander import expand_ranges

class TestStage5(unittest.TestCase):
    def test_step_forward(self):
        self.assertEqual(expand_ranges("1-10:2"), [1, 3, 5, 7, 9])

    def test_step_backward(self):
        self.assertEqual(expand_ranges("10-1:3"), [10, 7, 4, 1])

    def test_step_equal_range(self):
        self.assertEqual(expand_ranges("3-3:1"), [3])

    def test_missing_step_in_reverse(self):
        self.assertEqual(expand_ranges("5-2"), [5, 4, 3, 2])

    def test_step_auto_fix_negative(self):
        self.assertEqual(expand_ranges("1-5:-1"), [1, 2, 3, 4, 5])

    def test_invalid_step_value(self):
        with self.assertRaises(ValueError):
            expand_ranges("1-5:xyz")


if __name__ == "__main__":
    unittest.main()
