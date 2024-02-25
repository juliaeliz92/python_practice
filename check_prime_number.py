#Write a function to check if a number is a prime number

def checkPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return "Not a prime"
    return "Prime"

print(checkPrime(2))
print(checkPrime(4))