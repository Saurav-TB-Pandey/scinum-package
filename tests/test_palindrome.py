import unittest
from sinum import palindrome

class TestPalindromeFunctions(unittest.TestCase):
    
    def test_isPalindrome(self):
        self.assertTrue(palindrome.isPalindrome(121))
        self.assertFalse(palindrome.isPalindrome(123))

    def test_listPalindrome(self):
        palindromeList = palindrome.listPalindrome(5)
        self.assertEqual(palindromeList, [0, 1, 2, 3, 4])

    def test_listPalindromeBetween(self):
        palindromeList = palindrome.listPalindromeBetween(100, 200)
        expected_list = [101, 111, 121, 131, 141, 151, 161, 171, 181, 191]
        self.assertEqual(palindromeList, expected_list)

if __name__ == '__main__':
    unittest.main()