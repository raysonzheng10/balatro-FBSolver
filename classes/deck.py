import random
from card import Card, Rank, Suit

class Deck:
    def __init__(self):
        self.cards: list[Card] = []
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(rank, suit))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw_card(self) -> Card:
        return self.cards.pop()
    
    def print_top_cards(self, num_cards: int = 5):
        print(f"Printing top {num_cards} cards of the deck:")
        print("\n".join(str(card) for card in self.cards[:num_cards]))
        
        return