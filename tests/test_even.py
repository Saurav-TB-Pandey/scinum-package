import unittest
from sinum import even

class TestEvenFunctions(unittest.TestCase):
    
    def test_isEven(self):
        self.assertTrue(even.isEven(4))
        self.assertFalse(even.isEven(7))

    def test_listEven(self):
        evenList = even.listEven(5)
        self.assertEqual(evenList, [0, 2, 4, 6, 8])

    def test_listEvenBetween(self):
        evenList = even.listEvenBetween(10, 20)
        expected_list = [10, 12, 14, 16, 18]
        self.assertEqual(evenList, expected_list)

if __name__ == '__main__':
    unittest.main()