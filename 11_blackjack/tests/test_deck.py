import sys; sys.path.insert(0, "C:/Users/augus/Documents/_Local/100daysofcode_pybootcamp/11_blackjack")
from deck import Deck, Card, create_deck

def test_new_deck() -> None:
    deck = Deck(2)
    deck.new_deck()
    assert len(deck.deck) == 104

def test_deal() -> None:
    deck = Deck(1)
    card = deck.deal()
    assert isinstance(card, Card) == True

def test_suffle() -> None:
    deck = Deck()
    deck_org = deck.deck.copy()
    deck.shuffle()
    assert deck.deck != deck_org