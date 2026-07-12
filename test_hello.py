import unittest

from hello import add, greet


class TestHello(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_greet(self):
        self.assertEqual(greet("world"), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
