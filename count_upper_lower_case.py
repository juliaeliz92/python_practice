#Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

# method to count number of upper and lower case character occurances in the string
# @args: input string
# return none

def count_upper_lower_case(string):
    uppercase_ascii = [65, 90]
    lowercase_ascii = [97, 122]
    lower_count = 0
    upper_count = 0
    for i in range(len(string)):
        ascii = ord(string[i])
        if ascii >= uppercase_ascii[0] and ascii <= uppercase_ascii[1]:
            upper_count += 1
        elif ascii >= lowercase_ascii[0] and ascii <= lowercase_ascii[1]:
            lower_count += 1
    print('there are', upper_count, 'upper case letters and', lower_count, 'lower case letters in the string')

count_upper_lower_case('My name is Julia')
count_upper_lower_case('3.14')
count_upper_lower_case('TESTING UPPER CASE')
count_upper_lower_case('testing lower case')

