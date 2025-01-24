# index.py

import os
import json
from unidecode import unidecode

current_dir = os.path.dirname(os.path.abspath(__file__))
# Load the dictionary from the JSON file
with open(os.path.join(current_dir, 'dict.json'), 'r', encoding='utf-8') as file:
    global _dict
    _dict = json.load(file)

def pinyin(char):
    return list(set([unidecode(p) for p in _dict.get(char, [])]))

def detailed_pinyin(char):
    return _dict.get(char, [])

def alls():
    return _dict
