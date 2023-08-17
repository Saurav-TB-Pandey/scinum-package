import unittest
from sinum import fibonacci

class TestFibonacciFunctions(unittest.TestCase):
    
    def test_listFibonacci(self):
        fibonacciList = fibonacci.listFibonacci(5)
        self.assertEqual(fibonacciList, [0, 1, 1, 2, 3])

if __name__ == '__main__':
    unittest.main()