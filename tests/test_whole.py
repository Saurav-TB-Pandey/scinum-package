import unittest
from sinum import whole

class TestWholeFunctions(unittest.TestCase):
    
    def test_isWhole(self):
        self.assertTrue(whole.isWhole(7))
        self.assertFalse(whole.isWhole(-3))

    def test_listWhole(self):
        wholeList = whole.listWhole(5)
        self.assertEqual(wholeList, [0, 1, 2, 3, 4])

    def test_listWholeBetween(self):
        wholeList = whole.listWholeBetween(10, 15)
        expected_list = [10, 11, 12, 13, 14]
        self.assertEqual(wholeList, expected_list)

if __name__ == '__main__':
    unittest.main()