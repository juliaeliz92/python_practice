#Write a program to count the occurrences of a specific character in a string.

# method to count number of character occurances in the string
# @args: input string
# return none

def char_occurances_count_string(string, char):
    index = string.find(char)
    mod_string = string
    count = 0
    while index > 0:
        mod_string = mod_string.replace(char, "", 1)
        count += 1
        index = mod_string.find(char)
    print('there are', count, 'occurances of', char, 'in', string)

char_occurances_count_string('baa baa black sheep', 'a')
char_occurances_count_string('hello world', 'r');
char_occurances_count_string('ring a rosa', 'v')