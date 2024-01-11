import unittest
from main import Test_class

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        test = Test_class(8, 2)
        self.assertEqual(test.get_sum(), 10, 'The sum is wrong.')
        self.assertEqual(test.get_difference(), 6, 'The difference is wrong.')

    def test_nieuw(self):
        test = Test_class(8, 2)
        self.assertEqual(test.test_fun(), True, "Waardes niet gelijk.")
        self.assertLess(test.test_één(), 4, "Ja dat ging dus fout")
        self.assertEqual(test.nieuwe_functie(1), 1, "Waardes zijn niet gelijk!")
    
if __name__ == '__main__':
    print("testen")
    unittest.main()