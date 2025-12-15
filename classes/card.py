from enum import Enum, IntEnum

class Rank(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def get_chip_value(self) -> int:
        if self is Rank.ACE:
            return 11
        if self.value >= 10:
            return 10
        return self.value

class Suit(Enum):
    DIAMONDS = 1
    CLUBS = 2
    HEARTS = 3
    SPADES = 4

SUIT_SYMBOL = {
    Suit.DIAMONDS: "♦",
    Suit.CLUBS: "♣",
    Suit.HEARTS: "♥",
    Suit.SPADES: "♠",
}

class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{SUIT_SYMBOL[self.suit]} {self.rank.name}"
    
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def get_chip_value(self) -> int:
        return self.rank.get_chip_value()


