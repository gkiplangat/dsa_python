import unittest
from list03_maximum import find_max  # Ensure correct import


class TestFindMax(unittest.TestCase):
    def test_standard_list(self):
        """Test a normal list of positive numbers"""
        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(find_max([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        """Test a list with both positive and negative numbers"""
        self.assertEqual(find_max([-10, 0, 10, 5, -5]), 10)

    def test_single_element(self):
        """Test a list with a single element"""
        self.assertEqual(find_max([42]), 42)

    def test_large_numbers(self):
        """Test a list with large numbers"""
        self.assertEqual(find_max([1000000, 999999, 500000]), 1000000)

    def test_duplicate_max_values(self):
        """Test a list where the max value appears multiple times"""
        self.assertEqual(find_max([3, 1, 3, 2, 3]), 3)

    def test_empty_list(self):
        """Test an empty list (should raise an error)"""
        with self.assertRaises(ValueError):
            find_max([])


if __name__ == '__main__':
    unittest.main()
