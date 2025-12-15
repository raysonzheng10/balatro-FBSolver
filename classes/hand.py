from collections import Counter
from enum import Enum
from typing import List, Tuple
from card import Card, Rank

class HandType(Enum):
    """Balatro hand types with their base chips and multiplier"""
    # Ignore hidden hands, not possible in default first blind
    STRAIGHT_FLUSH = ("Straight Flush", 100, 8)
    FOUR_OF_A_KIND = ("Four of a Kind", 60, 7)
    FULL_HOUSE = ("Full House", 40, 4)  
    FLUSH = ("Flush", 35, 4)
    STRAIGHT = ("Straight", 30, 4)
    THREE_OF_A_KIND = ("Three of a Kind", 30, 3)
    TWO_PAIR = ("Two Pair", 20, 2)
    PAIR = ("Pair", 10, 2)
    HIGH_CARD = ("High Card", 5, 1)

    def __init__(self, display_name: str, base_chips: int, base_mult: int):
        self.display_name = display_name
        self.base_chips = base_chips
        self.base_mult = base_mult


class Hand:
    """Represents a poker hand of up to 5 cards and calculates its score"""
    def __init__(self, cards: List[Card]):
        if len(cards) > 5:
            raise ValueError("Hand cannot contain more than 5 cards")
        elif len(cards) == 0:
            raise ValueError("Hand cannot be empty")
        
        self.cards: List[Card] = cards

        self.hand_type: HandType = None
        self.cards_chips: int = 0
        self.score: int = 0

        self.evaluate()

    def evaluate(self) -> Tuple[HandType, int]:
        self.hand_type = self._identify_hand()
        self.score = self._calculate_score()

        return self.hand_type, self.score

    def _identify_hand(self) -> HandType:
        # Check for flush (all same suit)
        is_flush = self._is_flush()
        # Check for straight
        is_straight = self._is_straight()

        if is_straight and is_flush:
            self.cards_chips = self._five_handed_chips()
            return HandType.STRAIGHT_FLUSH
        if is_straight:
            self.cards_chips = self._five_handed_chips()
            return HandType.STRAIGHT
        if is_flush:
            self.cards_chips = self._five_handed_chips()
            return HandType.FLUSH

        # Get rank counts
        rank_counts = self._get_sorted_rank_counts()
        # Four of a Kind
        if rank_counts[0][0] == 4:
            self.cards_chips = rank_counts[0][1].get_chip_value() * 4
            return HandType.FOUR_OF_A_KIND
        
        # Full House
        if rank_counts[0][0] == 3 and len(rank_counts) > 1 and rank_counts[1][0] == 2:
            self.cards_chips = self._five_handed_chips()
            return HandType.FULL_HOUSE

        # Three of a Kind
        if rank_counts[0][0] == 3:
            self.cards_chips = rank_counts[0][1].get_chip_value() * 3
            return HandType.THREE_OF_A_KIND

        # Two Pair
        if rank_counts[0][0] == 2 and len(rank_counts) > 1 and rank_counts[1][0] == 2:
            self.cards_chips = (rank_counts[0][1].get_chip_value() * 2) + (rank_counts[1][1].get_chip_value() * 2)
            return HandType.TWO_PAIR

        # Pair
        if rank_counts[0][0] == 2:
            self.cards_chips = rank_counts[0][1].get_chip_value() * 2
            return HandType.PAIR

        # High Card (default)
        self.cards_chips = rank_counts[0][1].get_chip_value()
        return HandType.HIGH_CARD

    def _calculate_score(self) -> int:
        if self.hand_type is None:
            return 0

        chips = self.hand_type.base_chips + self.cards_chips
        mult = self.hand_type.base_mult

        return chips * mult

    def _five_handed_chips(self) -> int:
        # sums chips of all 5 cards, only valid for valid 5 card hands (ie. flush, straight, etc.)
        total = 0
        for card in self.cards:
            total += card.get_chip_value()
        return total

    def _is_flush(self) -> bool:
        suit_counts = Counter([card.suit for card in self.cards])
        for count in suit_counts.values():
            if count == 5:
                return True
        
        return False
    
    def _is_straight(self) -> bool:
        if len(self.cards) < 5:
            return False

        values = sorted([card.rank.value for card in self.cards])

        # manually check for broadway straight
        if set(values) == {2, 3, 4, 5, 14}:  
            return True
        
        # Check for consecutive values
        for i in range(len(values) - 1):
            if values[i + 1] - values[i] != 1:
                return False
        return True

    def _get_sorted_rank_counts(self) -> List[tuple[int, Rank]]:
        rank_counts = Counter([card.rank for card in self.cards])
        counts = sorted(
            [(count, rank) for rank, count in rank_counts.items()],
            reverse=True
        )

        return counts

    def __str__(self) -> str:
        if self.hand_type:
            return f"{self.hand_type.display_name} - Score: {self.score}"
        return f"Hand with {len(self.cards)} cards"