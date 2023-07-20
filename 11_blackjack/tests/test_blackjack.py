import sys; sys.path.insert(0, "C:/Users/augus/Documents/_Local/100daysofcode_pybootcamp/11_blackjack")
from unittest.mock import patch

import pytest 

from blackjack import Player, Blackjack

def test_create_player() -> None:
    player = Player(name='test_player',
           balance=200,
           hand=['card1, card2'])
    assert player.name == 'test_player'

@pytest.fixture
def blackjack_two_players(monkeypatch) -> Blackjack:
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    bj_game = Blackjack()
    bj_game.players = list(Player('tester_one', balance=300),
                           Player('tester_two', balance=400))
    return bj_game


def test_iniciate_player(monkeypatch) -> None:
    inputs = iter(['s', 'tester', 'n'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    bj_game = Blackjack()

    assert bj_game.players[0].name == 'tester'