#Write a Python program to check if two strings are anagrams

def check_anagram(string1, string2):
    if(sorted(string1) == sorted(string2)):
        print('Anagram!')
    else:
        print('Not Anagram!')

check_anagram('brush', 'shrub')
check_anagram('needle', 'thread')