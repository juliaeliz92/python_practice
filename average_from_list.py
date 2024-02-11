#Create a function that calculates the average of a list of numbers

# method to print the average from a list
# @args: input list
# return none

def get_average_list(my_list):
    print(f'average is {sum(my_list) / len(my_list)}')

list1 = [1, 2, 3, 4, 5]
get_average_list(list1)