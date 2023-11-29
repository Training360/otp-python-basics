import unittest
from lib import summarize, divide


class TestLibFunctions(unittest.TestCase):
    def test_summarize(self):
        self.assertEqual(summarize(10, 10), 20)
        self.assertEqual(summarize(-10, -10), -20)
        self.assertEqual(summarize(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 1), 10)
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(10, 5), 2)
        self.assertRaises(ValueError, divide, 10, 0)


if __name__ == '__main__':
    unittest.main()
