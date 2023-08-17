import unittest
from sinum import odd

class TestOddFunctions(unittest.TestCase):
    
    def test_isOdd(self):
        self.assertTrue(odd.isOdd(5))
        self.assertFalse(odd.isOdd(8))

    def test_listOdd(self):
        oddList = odd.listOdd(5)
        self.assertEqual(oddList, [1, 3, 5, 7, 9])

    def test_listOddBetween(self):
        oddList = odd.listOddBetween(10, 15)
        expected_list = [11, 13]
        self.assertEqual(oddList, expected_list)

if __name__ == '__main__':
    unittest.main()