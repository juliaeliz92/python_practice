# Write a program to find the sum of all elements in a list.

# method to sum of elements in the list
# @args: input list
# return none
def sumListElements(list):
    sum = 0
    for elem in list:
        sum += elem
    print('the sum of all the elements in the list is', sum)


# user enters the number of the list elements
length = int(input('Enter list length'))
#user enters the list
list = []
for i in range(length):
    list.append(int(input('Enter element')))

#calling sum function
sumListElements(list)
