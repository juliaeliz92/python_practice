# Write a program to print the multiplication table of a given number.

# method to print multiplication table of a given number
# @args: int
# return none

def multiplication_table(number):
    for i in range(11):
        print(number, '*', i, '=', number * i)
    
try:
    multiplication_table(int(input('Enter a number')))
except:
    print('Invalid input')