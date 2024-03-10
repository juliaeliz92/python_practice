#Create a function that takes a string and returns the reverse of each word

def reverse_words(string):
    output = ''
    words = string.split(' ')
    for i in range(len(words)):
        output = output + ' ' + words[i][::-1]
    print(output)

reverse_words('I am cool')