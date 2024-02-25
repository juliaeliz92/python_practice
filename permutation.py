#Write a program that uses recursion to generate all permutations of a list

def get_permutation(number):
    if(number != 1):
        return number * get_permutation(number - 1)
    else:
        return 1;

print(f'permutation of 5 is {get_permutation(5)}')