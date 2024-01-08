import unittest
from main import Test_class

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        test = Test_class(8, 2)
        self.assertEqual(test.get_sum(), 10, 'The sum is wrong.')
        self.assertEqual(test.get_difference(), 6, 'The difference is wrong.')

    def test_random(self):
        test = Test_class(8, 2)
        self.assertEqual(test.test_fun(), False, "Not equal.")
        self.assertLess(test.test_één(), 4, "Ja dat ging dus fout")
    
if __name__ == '__main__':
    unittest.main()