import json
from random import choice

from hangman import Hangman

with open("words_pt.json", 'r') as file:
    words = json.load(file)

if __name__ == "__main__":
    Hangman(choice(words))