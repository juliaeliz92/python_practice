#Write a simple unit test for a function that adds two numbers

import unittest

def addNumbers(number1, number2):
    return number1 + number2

class TestNumberPrimeMethods(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(addNumbers(2, 5), 7)

if __name__ == '__main__':
    unittest.main()
