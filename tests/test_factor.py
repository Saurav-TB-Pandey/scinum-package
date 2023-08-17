import unittest
from sinum import factor

class TestFactorFunctions(unittest.TestCase):
    
    def test_isFactor(self):
        self.assertTrue(factor.isFactor(3, 9))
        self.assertFalse(factor.isFactor(4, 9))

    def test_factors(self):
        factorsList = factor.factors(12)
        self.assertEqual(factorsList, [1, 2, 3, 4, 6, 12])

if __name__ == '__main__':
    unittest.main()