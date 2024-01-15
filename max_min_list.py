# Write a program to find the maximum and minimum values in a list

# method to find min and max num element in the list
# @args: list
# return none
def find_min_man(list):
    list.sort()
    min = list[0]
    max = list[len(list) - 1]
    print('smallest number in the list', min)
    print('largest number in the list', max)

list = []
length = int(input('Enter length of list'))
for i in range(length):
    list.append(int(input('Enter element')))

find_min_man(list)