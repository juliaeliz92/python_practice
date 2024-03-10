#Create a program that replaces specific words in a text with their synonyms

import sys
sys.path.append(r"C:\users\julia\appdata\roaming\python\python312\site-packages")
from PyDictionary import PyDictionary
dictionary = PyDictionary()

def replace_synonyms(string):
    output = ''
    words = string.split(' ')
    for i in range(len(words)):
        if dictionary.synonym(words[i]) != None:
            words[i] = dictionary.synonyms(words)[0]
        output = output + words[i] + ' '
    print(output)

replace_synonyms('the article was exquisite')