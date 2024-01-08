import unittest
from main import Test_class

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        test = Test_class(8, 2)
        self.assertEqual(test.get_sum(), 10, 'The sum is wrong.')
        self.assertEqual(test.get_difference(), 6, 'The difference is wrong.')
        self.assertEqual(test.test_fun(), True, "Not equal.")

if __name__ == '__main__':
    unittest.main()