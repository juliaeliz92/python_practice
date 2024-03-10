#Create a program that checks if a string is a palindrome

def check_palindrome(string):
    if string == string[::-1]:
        print('palindrome')
    else:
        print('not palindrome')

check_palindrome('malayalam')
check_palindrome('apple')

