#Write a program that reads an integer from the user and handles invalid inputs

def read_int(user_input):
    try:
        int(user_input)
        print('Valid input')
    except:
        print('invalid input')

read_int(input('Insert an integer'))