# Write a program to remove duplicates from a list.

# method to remove duplicates from a given list
# @args: input list
# return list

def remove_duplicates(mylist):
    mylist = list(dict.fromkeys(mylist))
    return mylist

try:
    length = int(input('Enter length of list'))
    inputlist = []
    for i in range(length):
        inputlist.append(input('Enter list element'))
    print(remove_duplicates(inputlist))
except:
    print('Invalid input')