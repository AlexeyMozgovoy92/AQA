from three import factorial, absolute, procent, power, logarithm
import unittest

class TestFactorial(unittest.TestCase):
    def test_metod(self):
        self.assertEqual(factorial(5), 120)

if __name__ == "__main__":
    unittest.main()    