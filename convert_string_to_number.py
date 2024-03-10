#Create a function that converts a string to an integer and handles ValueError

def convert_string_number(string):
    try:
        int(string)
        print('convert successful')
    except:
        print('cannot convert string')

convert_string_number('bell')
convert_string_number('56')