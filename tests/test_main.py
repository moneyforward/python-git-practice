import unittest

class TestMain(unittest.TestCase):
    def test_greet(self):
        from app.main import greet
        self.assertEqual(greet(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()


    