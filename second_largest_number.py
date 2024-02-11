#Create a function that finds the second smallest element in a list.

# method to find the second smallest element in a list.
# @args: input list
# return none

def second_largest_number(list1):
    list1.sort()
    print(f'{list1[len(list1) - 2]}')

second_largest_number([1, 7, 5, 2, 0])