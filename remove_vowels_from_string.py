# Write a program to return strings without vowels from a given string

# method to return strings without vowels from a given string
# @args: input string
# return none

import re

def remove_vowels(string):
    print(f'{re.sub("[aeiouAEIOU]", "", string)}')

remove_vowels('apple')
remove_vowels('python')
remove_vowels('bottle')
remove_vowels('computer')
remove_vowels('watch')