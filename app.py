#Importing libraries
import json
from difflib import get_close_matches

#Storing the json data as a python library
data = json.load(open("data.json"))

def translate(w):
    q = w.lower() #making the query case insensitive
    if q in data:
        return data[q] # if we have a exact match
    elif len(get_close_matches(q, data.keys())) > 0:
        yn = input("Did you mean %s? (y/n): \n" % get_close_matches(q, data.keys())[0]).lower() #Suggesting a word for the user
        if yn == "y":
            return data[get_close_matches(q, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist, please double check it"
        else:
            return "We didn't understand your entry"
    else:
        return"The word doesn't exist, please double check it" # if we dont have a match


word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
