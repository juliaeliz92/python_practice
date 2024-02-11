#Create a program that checks if a given string is a valid email address.

# method to check if a given email is valid
# @args: input string
# return none

import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def email_validator(email):
    if re.fullmatch(regex, email):
        print('valid email')
    else:
        print('invalid email')

email_validator('juliapaulmyla@yahoo.com')
email_validator('isthisright@randomemail')