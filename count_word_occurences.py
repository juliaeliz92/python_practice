# Write a function to count the occurrences of words in a given string 

# method to count the occurrences of words in the string
# @args: input string
# return none

def count_word_occurrences(string):
    words = string.split(" ")
    wordSet = []
    wordOccurrencesDic = {}
    for i in range(len(words)):
        wordSet.append(words[i])
        try: 
            wordOccurrencesDic[words[i]] += 1
        except:
            wordOccurrencesDic.update({words[i]: 1})
    print(wordOccurrencesDic)

count_word_occurrences('this is good world. good world is hard to find')