#Write a program to flatten a nested list

def flatten_extend(matrix):
    flat_list = []
    for row in matrix:
        flat_list.extend(row)
    return flat_list

my_list = [
    [1, 2, 3],
    [4, 5, 6]
]

print(flatten_extend(my_list))