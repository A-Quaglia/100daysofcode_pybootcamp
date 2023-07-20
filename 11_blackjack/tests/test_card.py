import sys; sys.path.insert(0, "C:/Users/augus/Documents/_Local/100daysofcode_pybootcamp/11_blackjack")
from deck import Card

def test_card_value() -> None:
    nipe = "Ouros"
    rank = 'A'
    card = Card(nipe=nipe,
                rank=rank)
    assert card.value == 1

def test_card_str() -> None:
    nipe = "Ouros"
    rank = 'A'
    card = Card(nipe=nipe,
                rank=rank)
    assert str(card) == "A de Ouros"

def test_card_repr() -> None:
    nipe = "Ouros"
    rank = 'A'
    card = Card(nipe=nipe,
                rank=rank)
    assert repr(card) == "A de Ouros"