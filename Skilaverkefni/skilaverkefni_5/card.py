class Card:
    def __init__(self, rank, suit):
        # Initialize rank and suit based on the provided parameters
        if isinstance(rank, int):
            self.rank = rank
        elif isinstance(rank, str):
            self.rank = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}.get(rank.upper(), int(rank))
        self.suit = suit

    def __str__(self):
        # Determine the string representation of the card rank and suit
        rank_str = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}.get(self.rank, str(self.rank))
        return f"{rank_str:>2}{self.suit}"
