from card import Card
import random

class Deck:
    def __init__(self):
        # Initialize a deck of 52 cards
        suits = ['H', 'S', 'D', 'C']
        self.deck = [Card(rank, suit) for suit in suits for rank in range(2, 15)]

    def __str__(self):
        # Return the string representation of the deck with 13 cards per line
        return '\n'.join(' '.join(str(self.deck[i + j]) for j in range(13)) for i in range(0, len(self.deck), 13))

    def shuffle(self):
        # Shuffle the deck
        random.shuffle(self.deck)

    def deal(self):
        # Deal a single card from the top of the deck
        return self.deck.pop(0) if self.deck else None
