#Create a function that returns the key with the maximum value in a dictionary

def return_max_key_value(dict):
    maxKey = list(dict.keys())[0]
    maxValue = dict[maxKey]
    for x in dict:
        if dict[x] > maxValue:
            maxKey = x
            maxValue = dict[x]
    print(f'{maxKey} : {maxValue}')

my_dict = {
    'a': 6,
    'b': 5,
    'c': 8
}

return_max_key_value(my_dict)