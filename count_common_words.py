#Write a program to find the most common words in a text file

def common_words(string):
    words = string.split(' ')
    dict = {}
    for i in range(len(words)):
        try:
            dict[words[i]] = dict[words[i]] + 1
        except KeyError:
            dict[words[i]] = 1
    largest_freq = dict[list(dict.keys())[0]]
    largest_freq_key = list(dict.keys())[0]
    for i in range(len(dict.keys())):
        if(dict[list(dict.keys())[i]] > largest_freq):
            largest_freq = dict[list(dict.keys())[i]]
            largest_freq_key = list(dict.keys())[i]
    print(f'key: {largest_freq_key}, value: {largest_freq}')

common_words('apple is red. red is my favorite color. but apple is not my favorite fruit')