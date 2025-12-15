import sys
sys.path.append('classes')

from classes.card import Card, Rank, Suit
from classes.deck import Deck
from classes.hand import Hand, HandType


def test_individual_hands():
    """Test specific hand combinations"""
    print("=" * 60)
    print("TESTING INDIVIDUAL HAND TYPES")
    print("=" * 60)

    # Test 1: Royal Flush (Straight Flush with high cards)
    print("\n1. Royal Flush (Straight Flush):")
    royal_flush = Hand([
        Card(Rank.ACE, Suit.HEARTS),
        Card(Rank.KING, Suit.HEARTS),
        Card(Rank.QUEEN, Suit.HEARTS),
        Card(Rank.JACK, Suit.HEARTS),
        Card(Rank.TEN, Suit.HEARTS)
    ])
    print(f"   Cards: {', '.join(str(c) for c in royal_flush.cards)}")
    print(f"   Result: {royal_flush}")
    print(f"   Hand Type: {royal_flush.hand_type.display_name}")
    print(f"   Score: {royal_flush.score}")

    # Test 2: Four of a Kind
    print("\n2. Four of a Kind:")
    four_kind = Hand([
        Card(Rank.SEVEN, Suit.HEARTS),
        Card(Rank.SEVEN, Suit.DIAMONDS),
        Card(Rank.SEVEN, Suit.CLUBS),
        Card(Rank.SEVEN, Suit.SPADES),
        Card(Rank.ACE, Suit.HEARTS)
    ])
    print(f"   Cards: {', '.join(str(c) for c in four_kind.cards)}")
    print(f"   Result: {four_kind}")

    # Test 3: Full House
    print("\n3. Full House:")
    full_house = Hand([
        Card(Rank.KING, Suit.HEARTS),
        Card(Rank.KING, Suit.DIAMONDS),
        Card(Rank.KING, Suit.CLUBS),
        Card(Rank.NINE, Suit.SPADES),
        Card(Rank.NINE, Suit.HEARTS)
    ])
    print(f"   Cards: {', '.join(str(c) for c in full_house.cards)}")
    print(f"   Result: {full_house}")

    # Test 4: Flush
    print("\n4. Flush:")
    flush = Hand([
        Card(Rank.TWO, Suit.DIAMONDS),
        Card(Rank.FIVE, Suit.DIAMONDS),
        Card(Rank.SEVEN, Suit.DIAMONDS),
        Card(Rank.NINE, Suit.DIAMONDS),
        Card(Rank.KING, Suit.DIAMONDS)
    ])
    print(f"   Cards: {', '.join(str(c) for c in flush.cards)}")
    print(f"   Result: {flush}")

    # Test 5: Straight
    print("\n5. Straight:")
    straight = Hand([
        Card(Rank.FIVE, Suit.HEARTS),
        Card(Rank.SIX, Suit.DIAMONDS),
        Card(Rank.SEVEN, Suit.CLUBS),
        Card(Rank.EIGHT, Suit.SPADES),
        Card(Rank.NINE, Suit.HEARTS)
    ])
    print(f"   Cards: {', '.join(str(c) for c in straight.cards)}")
    print(f"   Result: {straight}")

    # Test 6: Ace-low Straight
    print("\n6. Ace-low Straight (A-2-3-4-5):")
    ace_low_straight = Hand([
        Card(Rank.ACE, Suit.HEARTS),
        Card(Rank.TWO, Suit.DIAMONDS),
        Card(Rank.THREE, Suit.CLUBS),
        Card(Rank.FOUR, Suit.SPADES),
        Card(Rank.FIVE, Suit.HEARTS)
    ])
    print(f"   Cards: {', '.join(str(c) for c in ace_low_straight.cards)}")
    print(f"   Result: {ace_low_straight}")

    # Test 7: Three of a Kind
    print("\n7. Three of a Kind:")
    three_kind = Hand([
        Card(Rank.QUEEN, Suit.HEARTS),
        Card(Rank.QUEEN, Suit.DIAMONDS),
        Card(Rank.QUEEN, Suit.CLUBS),
        Card(Rank.FIVE, Suit.SPADES),
        Card(Rank.TWO, Suit.HEARTS)
    ])
    print(f"   Cards: {', '.join(str(c) for c in three_kind.cards)}")
    print(f"   Result: {three_kind}")

    # Test 8: Two Pair
    print("\n8. Two Pair:")
    two_pair = Hand([
        Card(Rank.JACK, Suit.HEARTS),
        Card(Rank.JACK, Suit.DIAMONDS),
        Card(Rank.FOUR, Suit.CLUBS),
        Card(Rank.FOUR, Suit.SPADES),
        Card(Rank.ACE, Suit.HEARTS)
    ])
    print(f"   Cards: {', '.join(str(c) for c in two_pair.cards)}")
    print(f"   Result: {two_pair}")

    # Test 9: Pair
    print("\n9. Pair:")
    pair = Hand([
        Card(Rank.TEN, Suit.HEARTS),
        Card(Rank.TEN, Suit.DIAMONDS),
        Card(Rank.FIVE, Suit.CLUBS),
        Card(Rank.SEVEN, Suit.SPADES),
        Card(Rank.KING, Suit.HEARTS)
    ])
    print(f"   Cards: {', '.join(str(c) for c in pair.cards)}")
    print(f"   Result: {pair}")

    # Test 10: High Card
    print("\n10. High Card:")
    high_card = Hand([
        Card(Rank.ACE, Suit.HEARTS),
        Card(Rank.KING, Suit.DIAMONDS),
        Card(Rank.EIGHT, Suit.CLUBS),
        Card(Rank.FIVE, Suit.SPADES),
        Card(Rank.TWO, Suit.HEARTS)
    ])
    print(f"   Cards: {', '.join(str(c) for c in high_card.cards)}")
    print(f"   Result: {high_card}")

    # Test 11: Single Card
    print("\n11. Single Card (High Card):")
    single = Hand([Card(Rank.KING, Suit.HEARTS)])
    print(f"   Cards: {', '.join(str(c) for c in single.cards)}")
    print(f"   Result: {single}")

    # Test 12: Three Card Hand
    print("\n12. Three Card Hand (Pair):")
    three_card = Hand([
        Card(Rank.EIGHT, Suit.HEARTS),
        Card(Rank.EIGHT, Suit.DIAMONDS),
        Card(Rank.TWO, Suit.CLUBS)
    ])
    print(f"   Cards: {', '.join(str(c) for c in three_card.cards)}")
    print(f"   Result: {three_card}")


def test_deck_integration():
    """Test integration with Deck class"""
    print("\n" + "=" * 60)
    print("TESTING DECK INTEGRATION")
    print("=" * 60)

    # Create a deck and draw 5 random cards
    deck = Deck()
    print("\nDrawing 5 random cards from deck:")

    random_cards = []
    for i in range(5):
        random_cards.append(deck.draw_card())

    print(f"Drawn cards: {', '.join(str(c) for c in random_cards)}")

    # Evaluate the hand
    random_hand = Hand(random_cards)
    print(f"Hand evaluation: {random_hand}")
    print(f"Score: {random_hand.score}")

if __name__ == "__main__":
    print("\n" + "#" * 60)
    print("# BALATRO HAND EVALUATOR TEST SUITE")
    print("#" * 60)

    test_individual_hands()
    test_deck_integration()

    print("\n" + "#" * 60)
    print("# ALL TESTS COMPLETED")
    print("#" * 60 + "\n")
