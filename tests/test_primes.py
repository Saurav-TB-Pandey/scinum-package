import unittest
from sinum import primes

class TestPrimesFunctions(unittest.TestCase):
    
    def test_isPrime(self):
        self.assertTrue(primes.isPrime(7))
        self.assertFalse(primes.isPrime(9))

    def test_listPrimeBetween(self):
        primeList = primes.listPrimeBetween(10, 20)
        expected_list = [11, 13, 17, 19]
        self.assertEqual(primeList, expected_list)

    def test_listPrime(self):
        primeList = primes.listPrime(5)
        self.assertEqual(primeList, [2, 3, 5, 7, 11])

if __name__ == '__main__':
    unittest.main()