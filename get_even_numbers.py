#Write a function that takes a list of numbers and returns a new list containing only the even numbers.

# method to filter out odd numbers from a list and return only the even numbers
# @args: input list
# return list

def even_number_only(list):
    filtered_list = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            filtered_list.append(list[i])
    return filtered_list

my_list = [3, 7, 8, 4, 8, 11, 50, 47]

print(f'list before filtering {my_list}')
print(f'list after filtering {even_number_only(my_list)}')