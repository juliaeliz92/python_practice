#Write a program to shuffle the elements of a list randomly

# method to shuffle the order of the list
# @args: input list
# return shuffled list

import random

def list_shuffle(list):
    print('Original list', list)
    random.shuffle(list)
    print('Shuffled list', list)

list_shuffle([2,5,6,3,7])