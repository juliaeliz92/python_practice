#Create a function that generates a random number between a given range

# method to generate number from a given range
# @args: input list
# return list

from random import randrange

def random_generator(*range_args):
    print(randrange(*range_args))

random_generator(10)
random_generator(10, 50)
random_generator(100, 110)