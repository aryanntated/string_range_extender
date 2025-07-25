import unittest
from range_expander import expand_ranges

class TestStage2(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(expand_ranges("5"), [5])

    def test_basic_range(self):
        self.assertEqual(expand_ranges("1-3"), [1, 2, 3])

    def test_mixed_input(self):
        self.assertEqual(expand_ranges("1-3,5,7-8"), [1, 2, 3, 5, 7, 8])

    def test_whitespace_and_empty_parts(self):
        self.assertEqual(expand_ranges(" , 1 - 3 , ,5 "), [1, 2, 3, 5])

    def test_only_commas_and_spaces(self):
        self.assertEqual(expand_ranges(" , , , "), [])

if __name__ == "__main__":
    unittest.main()
