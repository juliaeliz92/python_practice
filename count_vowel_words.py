#Create a function to find all words in a sentence that start with a vowel

def count_vowel_words(string):
    words = string.split(' ')
    count = 0
    for i in range(len(words)):
        if words[i][0].lower() in "aeiou":
            count = count + 1
    print(count)

count_vowel_words('I ate two apples')