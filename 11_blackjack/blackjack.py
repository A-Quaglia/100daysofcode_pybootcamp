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

    def print_board(self):
        print(f" Dealer: {self.dealer_hand} \n\n")

        for player in self.players:
            # hand = " ".join(player.hand) if len(player.hand)>0 else ['*********', '*********']
            if len(player.hand)==0:
                hand = ['*********', '*********']
            else:
                hand = list()
                for card in player.hand:
                    hand.append(str(card))
                " ".join(hand)

            print(f"{player.name} hand: {hand} \n  balance: {player.balance}\n")

    def start_round(self):
        self._clear_hands()
        self.print_board()
        for player in self.players:
            while True:
                bet = input(f"{player.name} turno. Quanto será sua aposta?")
                try:
                    bet = int(bet)
                except ValueError:
                    pass
                else:
                    break
            player.balance -= bet
            player.bet = bet
            self.print_board()

        for player in self.players:
            player.hand.append(self.deck.deal())
            player.hand.append(self.deck.deal())

        self.dealer_hand[0] = self.deck.deal()
 
    def _clear_hands(self):
        self.dealer_hand = ['*********', '*********']
        for player in self.players:
            player.hand.clear()


    def _calculate_hand_value(self, player: Player):
        total_value = 0
        for card in player.hand:
            total_value += card.value
        
        player.hand_value = total_value


    def player_turn(self, player: Player):
        move = input("Hit, stand or dobble? [h,s,d]").lower()
        self._calculate_hand_value(player)

        while move not in ['h','s','d']:
            self.player_turn(player)
        
        if move == 'h':
            player.hand.append(self.deck.deal())
            self._calculate_hand_value(player)
            self.print_board()
            if player.hand_value > 21:
                print("Bust")