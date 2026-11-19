import unittest
from greet import greet


class TestGreet(unittest.TestCase):
    def test_greet_standard_name(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_greet_world(self):
        self.assertEqual(greet("World"), "Hello, World!")

    def test_greet_empty_string(self):
        self.assertEqual(greet(""), "Hello, !")

    def test_greet_with_spaces(self):
        self.assertEqual(greet("Jane Doe"), "Hello, Jane Doe!")


if __name__ == "__main__":
    unittest.main()
