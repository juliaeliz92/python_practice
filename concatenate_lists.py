# Write a program to return concatenated lists

# method to return concatenated lists
# @args: input lists
# return list

def concatenate_lists(*lists):
    new_list = []
    for i in range(len(lists)):
        new_list = new_list + lists[i]
    return new_list

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = concatenate_lists(list1, list2)
print(f'made {list3} from {list1} and {list2}')