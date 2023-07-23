#%%
import pandas as pd

nato_alphabet_data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = dict()
for index, row in nato_alphabet_data.iterrows():
    nato_alphabet[row.letter] = row.code

#%%
def trasnlate_to_nato(phrase: str) -> list[str]:
    result = []
    for letter in phrase.upper():
        if letter in nato_alphabet.keys():
            result.append(nato_alphabet[letter])
        else:
            result.append(letter)
    
    return result

if __name__ == "__main__":
    phrase = input("Enter a word::  ")
    print(trasnlate_to_nato(phrase))