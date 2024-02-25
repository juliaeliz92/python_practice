#Write a program that uses a try-except block to handle division by zero

def divide(number1, number2):
    try:
        print(number1 / number2)
    except:
        print('divide by zero not possible')

divide(2,0)