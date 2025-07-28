import unittest
from app.main import greet

class TestMain(unittest.TestCase):
    def test_greet(self):
        expected = "Hello, MoneyForward! Let's learn Git and Python!"
        self.assertEqual(greet(), expected)


if __name__ == "__main__":
    unittest.main()