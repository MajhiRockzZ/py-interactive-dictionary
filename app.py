import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(word, data.keys())[0]
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")
print(translate(word))

"""
import difflib
from difflib import SequenceMatcher
SequenceMatcher(None, "rainn", "rain").ratio()
"""

"""
from difflib import get_close_matches
help(get_close_matches)
get_close_matches("rainn", ["help", "pyramid", "rain"])
get_close_matches("rainn", data.keys())
get_close_matches("rainn", data.keys())[0]
"""
