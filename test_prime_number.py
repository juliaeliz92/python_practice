#Write a test case for a function that checks if a number is prime

import unittest

def checkPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

class TestNumberPrimeMethods(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(checkPrime(2), True)

if __name__ == '__main__':
    unittest.main()
