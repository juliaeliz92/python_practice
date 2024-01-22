# Write a program to reverse a given string.

# method to reverse the string using recursion
# @args: input string
# return none

def reverse_string_recursive(string, len):
    if(len < 0):
        return "";
    return string[len] + reverse_string_recursive(string, len - 1)

print(reverse_string_recursive('apple', (len('apple') - 1)))

# method to reverse the string
# @args: input string
# return none

def reverse_string(string):
    stringChar = [*string]
    stringChar.reverse()
    print(''.join(stringChar))

reverse_string('apple')