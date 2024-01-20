# Write a program to check if a number is even or odd.

# method to check if the number is odd or even
# @args: input number
# return none

def check_for_odd_even(number):
    if number % 2 == 0:
        print(number, 'is even')
    else:
        print(number, 'is odd')
    
try:
    check_for_odd_even(int(input('Enter a number')))
except:
    print('invalid input')
