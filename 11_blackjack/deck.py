from dataclasses import dataclass
from random import shuffle
from typing import List


nipes = ["Espadas", "Copas", "Paus", "Ouros"]
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

@dataclass
class Card:
    nipe: str
    rank: str

    def __post_init__(self):
        self.value = values[self.rank]

    def __str__(self):
        return f"{self.rank} de {self.nipe}"
    
    def __repr__(self):
        return f"{self.rank} de {self.nipe}"
    

