#Write a Python program to merge two dictionaries

def merge_dictionary(dict1, dict2):
    return dict1.update(dict2)

my_dict1 = { 'a': '10', 'b': '45'}
my_dict2 = { 'c': '35', 'd': '90', 'e': '22'}

merge_dictionary(my_dict1, my_dict2)

print(my_dict1)
