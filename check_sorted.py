#Write a function to check if a given list is sorted

def check_for_sorted(list):
    if(list == sorted(list)):
        print('Sorted!')
    else:
        print('not sorted')

check_for_sorted([1, 2, 3, 4])
check_for_sorted([8, 4, 6, 1])