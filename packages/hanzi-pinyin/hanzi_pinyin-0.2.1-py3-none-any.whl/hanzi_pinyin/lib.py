# index.py

import json
from unidecode import unidecode

# Load the dictionary from the JSON file
with open('./dict.json', 'r', encoding='utf-8') as file:
    global _dict
    _dict = json.load(file)

def pinyin(char):
    return list(set([unidecode(p) for p in _dict.get(char, [])]))

def detailedPinyin(char):
    return _dict.get(char, [])

def alls():
    return _dict
