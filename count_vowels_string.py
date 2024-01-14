# Write a function to count the number of vowels in a given string 
import re

# method to count number of vowels in the string
# @args: input string
# return none
def checkForVowel(string):
    vowelArray = re.findall('[aeiouAIEOU]', string)
    if vowelArray:
        print('The string contains', len(vowelArray), 'vowels')
    else:
        print('The string does not contains vowels')

# user inserts a string
string = input('Enter a string');

# checks and prints the number of vowels in the string
checkForVowel(string)
