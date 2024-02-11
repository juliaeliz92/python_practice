#Create a program that uses a lambda function to square each element of a list.

# method to use lambda function to square each element of a list
# @args: input list
# return list

list1 = [1, 2, 3, 4, 5]

square = list(map(lambda x: pow(x, 2), list1))

print(f'{square}')