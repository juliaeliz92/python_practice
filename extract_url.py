#Create a function to extract all URLs from a given text using regular expressions
import re

def extract_url(string):
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    print(urls)

extract_url('my linkedin link is https://www.linkedin.com/in/julia-paul-a1147b74/ and my github link is https://github.com/juliaeliz92')
