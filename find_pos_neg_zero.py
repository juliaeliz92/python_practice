# Write a program to check if a number is positive, negative, or zero.

# method to check if a number is positive, negative, or zero
# @args: input number
# return none
import re

def check_pos_neg_zero(number):
    if type(re.search(r"^[+|-]{0,1}\d+$", number)).__name__ == 'Match':
        number = int(number)
        if number > 0:
            print(number, 'is positive')
        elif number < 0:
            print(number, 'is negative')
        else:
            print(number, 'is zero')
    else:
        print('input is not a number')

ins = input('Enter the input')
check_pos_neg_zero(ins)