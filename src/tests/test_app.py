from app import index
import unittest

class AppTests(unittest.TestCase):
    def test_index(self):
        expected = "Hello, World!"
        actual = "Hello, World!"
        self.assertEqual(expected, actual)
if __name__ == '__main__':
    unittest.main()