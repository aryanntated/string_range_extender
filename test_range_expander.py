import unittest
from range_expander import expand_ranges

class TestStage3(unittest.TestCase):
    def test_default_delimiter(self):
        self.assertEqual(expand_ranges("1-3,5"), [1, 2, 3, 5])

    def test_custom_double_dot(self):
        self.assertEqual(expand_ranges("1..3", delimiters=["-", ".."]), [1, 2, 3])

    def test_custom_tilde(self):
        self.assertEqual(expand_ranges("4~6", delimiters=["-", "~"]), [4, 5, 6])

    def test_custom_to(self):
        self.assertEqual(expand_ranges("10 to 12", delimiters=["-", "to"]), [10, 11, 12])

    def test_mixed_delimiters(self):
        self.assertEqual(expand_ranges("1-2, 3..4, 5 to 6, 7~8", delimiters=["-", "..", "to", "~"]),
                         [1, 2, 3, 4, 5, 6, 7, 8])

    def test_invalid_delimiter(self):
        with self.assertRaises(ValueError):
            expand_ranges("2<>5", delimiters=["-", "..", "~"])

if __name__ == "__main__":
    unittest.main()
