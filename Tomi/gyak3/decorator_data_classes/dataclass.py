from dataclasses import dataclass, field
from typing import List

@dataclass(order=True)
class PlayingCard:
  sort_value: int = field(init=False, repr=False)
  rank: str
  suit: str

  def __str__(self):
    return f'{self.rank}{self.suit}'

  def __post_init__(self):
    self.sort_value = (RANKS.index(self.rank) * len(SUITS) + SUITS.index(self.suit))

SUITS = ['♣️', '♦️', '❤️', '♠️']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']
def make_deck():
  return [PlayingCard(r, s) for s in SUITS for r in RANKS]

@dataclass(frozen=True)
class Deck:
  cards: List[PlayingCard] = field(default_factory=make_deck)

  def __repr__(self):
    cards = ', '.join(f'{c}' for c in self.cards)
    return f'{self.__class__.__name__}:{cards}'

deck = Deck()
card = PlayingCard('2', '♠️')
card2 = PlayingCard('A', '♦️')
print(card > card2)
