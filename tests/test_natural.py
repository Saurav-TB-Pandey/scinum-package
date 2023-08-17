import unittest
from sinum import natural

class TestNaturalFunctions(unittest.TestCase):
    
    def test_isNatural(self):
        self.assertTrue(natural.isNatural(7))
        self.assertFalse(natural.isNatural(-3))

    def test_listNatural(self):
        naturalList = natural.listNatural(5)
        self.assertEqual(naturalList, [1, 2, 3, 4, 5])

    def test_listNaturalBetween(self):
        naturalList = natural.listNaturalBetween(10, 15)
        expected_list = [10, 11, 12, 13, 14]
        self.assertEqual(naturalList, expected_list)

if __name__ == '__main__':
    unittest.main()