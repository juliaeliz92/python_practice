#Create a function that checks if a number is a perfect square
import math

def check_perfect_square(number):
    if int(math.sqrt(number)) == math.sqrt(number):
        print('perfect square')
    else:
        print('not perfect square')

check_perfect_square(4)
check_perfect_square(6)