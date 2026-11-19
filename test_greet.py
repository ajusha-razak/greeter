"""Unit tests for the greeter module."""

import unittest
from greet import greet


class TestGreet(unittest.TestCase):
    """Test cases for the greet function."""

    def test_greet_standard_name(self):
        """Test greet with a standard name."""
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_greet_world(self):
        """Test greet with the word 'World'."""
        self.assertEqual(greet("World"), "Hello, World!")

    def test_greet_empty_string(self):
        """Test greet with an empty string."""
        self.assertEqual(greet(""), "Hello, !")


if __name__ == "__main__":
    unittest.main()
