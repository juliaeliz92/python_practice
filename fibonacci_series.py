# Write a program to print the first n numbers of a Fibonacci sequence

# method to fibannci series of n numbers
# @args: input number
# return None

def fibonacci_series(n):
    num1 = 0
    num2 = 1
    next_number = num2  
    count = 1
    
    while count <= n:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2

fibonacci_series(5)