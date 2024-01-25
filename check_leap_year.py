# Create a program that checks if a year is a leap year.

# method to check if given year is a leap year
# @args: input number
# return none

def check_leap_year(year):
    try:
        if (int(year) % 4 == 0):
            print('it\'s a leap year');
        else:
            print('not a leap year')
    except:
        print('invalid input')

check_leap_year(2014)
check_leap_year('apple')
check_leap_year('2023')
check_leap_year(2000)
