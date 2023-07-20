from dataclasses import dataclass, field
from deck import Deck

@dataclass
class Player:
    name: str
    balance: int
    hand: list = field(default_factory=list)
    bet = 0
    hand_value = 0

class Blackjack:
    def __init__(self):
        self.deck = Deck(number_of_decks=4)
        self._id = 1
        self.players = list()
        self.iniciate_players()
        self.dealer_hand = ['*********', '*********']

    def iniciate_players(self, balance=200):
        new_player = input("inserir novo jogador? [s/n]").lower()

        if new_player == 's':
            player_name = input("Qual o nome do jogador?")
            self.players.append(Player(player_name, balance))
            self.iniciate_players()
        elif new_player == 'n':
            print('boa sorte no jogo')
        else:
            self.iniciate_players()
