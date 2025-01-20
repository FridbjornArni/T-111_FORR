from card import Card

class Hand:
    NUMBER_OF_CARDS = 13

    def __init__(self):
        # Initialize an empty hand
        self.cards = []

    def __str__(self):
        # Return the string representation of the hand
        return " ".join(str(card) for card in self.cards) if self.cards else "Empty"

    def add_card(self, card):
        # Add a card to the hand if it has fewer than NUMBER_OF_CARDS
        if len(self.cards) < self.NUMBER_OF_CARDS:
            self.cards.append(card)
