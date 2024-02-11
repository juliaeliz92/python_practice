#Create a program that removes the nth element from a list.

# method to remove a list from list
# @args: input list
# return list

def remove_list_item(my_list, item):
    try:
        my_list.remove(item)
        return my_list
    except:
        return my_list

list1 = [1, 2, 3, 4, 5]

print(f'before removal {list1}')
print(f'removing 2 from list {remove_list_item(list1, 2)}')
print(f'removing 4 from list {remove_list_item(list1, 4)}')
print(f'removing an nonexistent number from list {remove_list_item(list1, 6)}')