#Create a program to find the second-largest element in a list.

def find_second_largest_element(list):
    list.sort()
    return list[len(list) - 2]

my_list = [5, 3, 7, 9, 1, 2]
print(f'the list {my_list}')
print(f'the second largest element {find_second_largest_element(my_list)}')