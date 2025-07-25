import unittest
from range_expander import expand_ranges

class TestStage1(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(expand_ranges("5"), [5])

    def test_basic_range(self):
        self.assertEqual(expand_ranges("1-3"), [1, 2, 3])

    def test_mixed_input(self):
        self.assertEqual(expand_ranges("1-3,5,7-8"), [1, 2, 3, 5, 7, 8])

if __name__ == "__main__":
    unittest.main()
