#Write a function to calculate the factorial of a number.

# method to find factorial of a number
# @args: input number
# return none

def factorial_without_recursive(number):
    fact = 1;
    for i in range(1, number + 1):
        fact *= i
    print(f'factorial of {number} is {fact}')

factorial_without_recursive(7)

def factorial_with_recursive(number):
    if number == 0 or number == 1:
        return 1;
    else:
        return number * factorial_with_recursive(number - 1)
    

    
print(f'factorial of {7} is {factorial_with_recursive(7)}')