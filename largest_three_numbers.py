#Create a program to find the largest among three numbers.

# method to find largest of three number
# @args: input number
# return none

def largest_of_three(list):
    list.sort()
    print(f'{list[2]} is the largest of three numbers')

largest_of_three([5, 4, 1])