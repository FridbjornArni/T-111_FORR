from card import Card
from deck import Deck
from hand import Hand

# Test the Card class
card = Card(10, 'H')
print(card)

# Test the Deck class
deck = Deck()
print(deck)

# Shuffle and deal cards
deck.shuffle()
print(deck.deal())

# Test the Hand class
hand = Hand()
for _ in range(5):
    hand.add_card(deck.deal())
print(hand)
