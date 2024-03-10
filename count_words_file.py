#Create a program that counts the occurrences of each word in a text file
import os

def read_count_occurrences_file(data):
    words = data.split(" ")
    wordSet = []
    wordOccurrencesDic = {}
    for i in range(len(words)):
        wordSet.append(words[i])
        try: 
            wordOccurrencesDic[words[i]] += 1
        except:
            wordOccurrencesDic.update({words[i]: 1})
    print(wordOccurrencesDic)

data = ''
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'poem.txt')

with open(file_path, 'r') as file:
    data = file.read().replace('\n', '')

read_count_occurrences_file(data)
