import unittest
from sinum import armstrong

class TestArmstrongFunctions(unittest.TestCase):

    def test_isArmstrong(self):
        self.assertTrue(armstrong.isArmstrong(153))
        self.assertFalse(armstrong.isArmstrong(123))

    def test_listArmstrong(self):
        armstrongList = armstrong.listArmstrong(5)
        self.assertEqual(armstrongList, [0, 1, 2, 3, 4])

    def test_listArmstrongBetween(self):
        armstrongList = armstrong.listArmstrongBetween(100, 1000)
        expected_list = [153, 370, 371, 407]
        self.assertEqual(armstrongList, expected_list)

if __name__ == '__main__':
    unittest.main()