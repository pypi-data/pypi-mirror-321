import unittest

from src.list import (
    filter_duplicate,
    filter_falsy,
)


class TestUtilityFunctions(unittest.TestCase):
    def test_filter_falsy(self):
        """Test filtering falsy values."""
        self.assertEqual(
            filter_falsy([0, 1, False, True, None, "", "hello", [], {}, set(), 42]),
            [1, True, "hello", 42],
        )
        self.assertEqual(filter_falsy([]), [])  # Empty list should return empty
        self.assertEqual(filter_falsy([False, None, 0, ""]), [])
        self.assertEqual(filter_falsy(["Python", 3.14, 0, None, ""]), ["Python", 3.14])

    def test_filter_duplicate(self):
        """Test filtering duplicate values while preserving order."""
        self.assertEqual(filter_duplicate([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(filter_duplicate(["a", "b", "a", "c", "b"]), ["a", "b", "c"])
        self.assertEqual(filter_duplicate([]), [])  # Empty list should return empty
        self.assertEqual(filter_duplicate([1, 1, 1, 1]), [1])
        self.assertEqual(
            filter_duplicate([None, None, "hello", None, "world"]),
            [None, "hello", "world"],
        )
        self.assertEqual(
            filter_duplicate(["apple", "banana", "apple", "cherry"]),
            ["apple", "banana", "cherry"],
        )
