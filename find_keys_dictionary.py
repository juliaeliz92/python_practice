# Write a program to check existence of a given key in a dictionary

# method to check existence of a given key in a dictionary
# @args: input key, dictionary
# return none

def check_key_dictionary(key, dictionary):
    try:
        dictionary[key]
        print(f'{key} exists')
    except:
        print(f'{key} does not exist')

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

check_key_dictionary('brand', car)
check_key_dictionary('year', car)
check_key_dictionary('color', car)