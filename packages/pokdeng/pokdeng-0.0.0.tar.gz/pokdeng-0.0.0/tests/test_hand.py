from unittest import TestCase, main
from pokdeng.card import Card, Rank, Suit
from pokdeng.exception import DuplicateCards, HandLessThan2Cards, HandMoreThan3Cards
from pokdeng.hand import Hand

class TestHand(TestCase):

    def test_DuplicateCards(self):
        with self.assertRaises(DuplicateCards):
            Hand(cards = [Card(Rank.ACE, Suit.SPADE), Card(Rank.ACE, Suit.SPADE)])

    def test_HandLessThan2Cards(self):
        with self.assertRaises(HandLessThan2Cards):
            Hand(cards = [Card(Rank.ACE, Suit.SPADE)])
    
    def test_HandMoreThan3Cards(self):
        with self.assertRaises(HandMoreThan3Cards):
            Hand(cards = [Card(Rank.NINE, Suit.CLUB), Card(Rank.NINE, Suit.DIAMOND), Card(Rank.NINE, Suit.HEART), Card(Rank.NINE, Suit.SPADE)])

    def test_pok_nine(self):
        hand = Hand(cards = [Card(Rank.ACE, Suit.CLUB), Card(Rank.EIGHT, Suit.HEART)])
        self.assertEqual(hand.pok_nine(), True)

        hand = Hand(cards = [Card(Rank.ACE, Suit.CLUB), Card(Rank.SEVEN, Suit.HEART)])
        self.assertEqual(hand.pok_nine(), False)

        hand = Hand(cards = [Card(Rank.ACE, Suit.CLUB), Card(Rank.TWO, Suit.SPADE), Card(Rank.SIX, Suit.HEART)])
        self.assertEqual(hand.pok_nine(), False)

    def test_pok_eight(self):
        hand = Hand(cards = [Card(Rank.ACE, Suit.CLUB), Card(Rank.SEVEN, Suit.HEART)])
        self.assertEqual(hand.pok_eight(), True)

        hand = Hand(cards = [Card(Rank.ACE, Suit.CLUB), Card(Rank.EIGHT, Suit.HEART)])
        self.assertEqual(hand.pok_eight(), False)

        hand = Hand(cards = [Card(Rank.ACE, Suit.CLUB), Card(Rank.ACE, Suit.SPADE), Card(Rank.SIX, Suit.HEART)])
        self.assertEqual(hand.pok_eight(), False)

    def test_tong(self):
        hand = Hand(cards = [Card(Rank.NINE, Suit.CLUB), Card(Rank.NINE, Suit.DIAMOND), Card(Rank.NINE, Suit.HEART)])
        self.assertEqual(hand.tong(), True)

        hand = Hand(cards = [Card(Rank.NINE, Suit.CLUB), Card(Rank.NINE, Suit.DIAMOND), Card(Rank.TEN, Suit.HEART)])
        self.assertEqual(hand.tong(), False)

        hand = Hand(cards = [Card(Rank.JACK, Suit.CLUB), Card(Rank.JACK, Suit.DIAMOND), Card(Rank.JACK, Suit.HEART)])
        self.assertEqual(hand.tong(), True)
    
    def test_straight_flush(self):
        hand = Hand(cards = [Card(Rank.TWO, Suit.CLUB), Card(Rank.THREE, Suit.CLUB), Card(Rank.FOUR, Suit.CLUB)])
        self.assertEqual(hand.straight_flush(), True)

        hand = Hand(cards = [Card(Rank.JACK, Suit.CLUB), Card(Rank.QUEEN, Suit.CLUB), Card(Rank.KING, Suit.CLUB)])
        self.assertEqual(hand.straight_flush(), True)

        hand = Hand(cards = [Card(Rank.QUEEN, Suit.CLUB), Card(Rank.KING, Suit.CLUB), Card(Rank.ACE, Suit.CLUB)])
        self.assertEqual(hand.straight_flush(), True)

        hand = Hand(cards = [Card(Rank.KING, Suit.CLUB), Card(Rank.ACE, Suit.CLUB), Card(Rank.TWO, Suit.CLUB)])
        self.assertEqual(hand.straight_flush(), False)

        hand = Hand(cards = [Card(Rank.ACE, Suit.CLUB), Card(Rank.TWO, Suit.CLUB), Card(Rank.THREE, Suit.CLUB)])
        self.assertEqual(hand.straight_flush(), False)

        hand = Hand(cards = [Card(Rank.FIVE, Suit.CLUB), Card(Rank.SIX, Suit.CLUB), Card(Rank.SEVEN, Suit.HEART)])
        self.assertEqual(hand.straight_flush(), False)

        hand = Hand(cards = [Card(Rank.FOUR, Suit.CLUB), Card(Rank.FIVE, Suit.CLUB)])
        self.assertEqual(hand.straight_flush(), False)

    def test_straight(self):
        hand = Hand(cards = [Card(Rank.TWO, Suit.CLUB), Card(Rank.THREE, Suit.CLUB), Card(Rank.FOUR, Suit.CLUB)])
        self.assertEqual(hand.straight(), True)

        hand = Hand(cards = [Card(Rank.JACK, Suit.CLUB), Card(Rank.QUEEN, Suit.CLUB), Card(Rank.KING, Suit.CLUB)])
        self.assertEqual(hand.straight(), True)

        hand = Hand(cards = [Card(Rank.QUEEN, Suit.CLUB), Card(Rank.KING, Suit.CLUB), Card(Rank.ACE, Suit.CLUB)])
        self.assertEqual(hand.straight(), True)

        hand = Hand(cards = [Card(Rank.KING, Suit.CLUB), Card(Rank.ACE, Suit.CLUB), Card(Rank.TWO, Suit.CLUB)])
        self.assertEqual(hand.straight(), False)

        hand = Hand(cards = [Card(Rank.ACE, Suit.CLUB), Card(Rank.TWO, Suit.CLUB), Card(Rank.THREE, Suit.CLUB)])
        self.assertEqual(hand.straight(), False)

        hand = Hand(cards = [Card(Rank.FIVE, Suit.CLUB), Card(Rank.SIX, Suit.CLUB), Card(Rank.SEVEN, Suit.HEART)])
        self.assertEqual(hand.straight(), True)

        hand = Hand(cards = [Card(Rank.FOUR, Suit.CLUB), Card(Rank.FIVE, Suit.CLUB)])
        self.assertEqual(hand.straight(), False)

    def test_three_yellow(self):
        hand = Hand(cards = [Card(Rank.JACK, Suit.CLUB), Card(Rank.JACK, Suit.DIAMOND), Card(Rank.QUEEN, Suit.HEART)])
        self.assertEqual(hand.three_yellow(), True)

        hand = Hand(cards = [Card(Rank.JACK, Suit.CLUB), Card(Rank.JACK, Suit.DIAMOND), Card(Rank.JACK, Suit.HEART)])
        self.assertEqual(hand.three_yellow(), True)

        hand = Hand(cards = [Card(Rank.JACK, Suit.CLUB), Card(Rank.JACK, Suit.DIAMOND), Card(Rank.ACE, Suit.HEART)])
        self.assertEqual(hand.three_yellow(), False)
    
    def test_compare_hand(self):
        hand1 = Hand(cards = [Card(Rank.ACE, Suit.CLUB), Card(Rank.EIGHT, Suit.CLUB)])
        hand2 = Hand(cards = [Card(Rank.ACE, Suit.CLUB), Card(Rank.EIGHT, Suit.SPADE)])
        self.assertTrue(hand1 == hand2) # compare deng later

        hand1 = Hand(cards = [Card(Rank.ACE, Suit.CLUB), Card(Rank.EIGHT, Suit.SPADE)])
        hand2 = Hand(cards = [Card(Rank.ACE, Suit.CLUB), Card(Rank.SEVEN, Suit.CLUB)])
        self.assertTrue(hand1 > hand2)

        hand1 = Hand(cards = [Card(Rank.ACE, Suit.CLUB), Card(Rank.EIGHT, Suit.SPADE)])
        hand2 = Hand(cards = [Card(Rank.TWO, Suit.CLUB), Card(Rank.SEVEN, Suit.HEART)])
        self.assertTrue(hand1 == hand2)

        hand1 = Hand(cards = [Card(Rank.ACE, Suit.CLUB), Card(Rank.SEVEN, Suit.SPADE)])
        hand2 = Hand(cards = [Card(Rank.TWO, Suit.CLUB), Card(Rank.THREE, Suit.HEART), Card(Rank.FOUR, Suit.DIAMOND)])
        self.assertTrue(hand1 > hand2)

        hand1 = Hand(cards = [Card(Rank.TWO, Suit.CLUB), Card(Rank.THREE, Suit.HEART), Card(Rank.FOUR, Suit.DIAMOND)])
        hand2 = Hand(cards = [Card(Rank.THREE, Suit.CLUB), Card(Rank.FOUR, Suit.HEART), Card(Rank.FIVE, Suit.DIAMOND)])
        self.assertTrue(hand1 > hand2)

        hand1 = Hand(cards = [Card(Rank.JACK, Suit.CLUB), Card(Rank.KING, Suit.HEART), Card(Rank.QUEEN, Suit.DIAMOND)])
        hand2 = Hand(cards = [Card(Rank.JACK, Suit.SPADE), Card(Rank.KING, Suit.SPADE), Card(Rank.QUEEN, Suit.SPADE)])
        self.assertTrue(hand1 < hand2)

        hand1 = Hand(cards = [Card(Rank.JACK, Suit.SPADE), Card(Rank.KING, Suit.SPADE), Card(Rank.QUEEN, Suit.SPADE)])
        hand2 = Hand(cards = [Card(Rank.TWO, Suit.SPADE), Card(Rank.THREE, Suit.SPADE), Card(Rank.FOUR, Suit.SPADE)])
        self.assertTrue(hand1 < hand2)

        hand1 = Hand(cards = [Card(Rank.JACK, Suit.SPADE), Card(Rank.KING, Suit.SPADE), Card(Rank.QUEEN, Suit.SPADE)])
        hand2 = Hand(cards = [Card(Rank.TWO, Suit.SPADE), Card(Rank.THREE, Suit.SPADE), Card(Rank.FOUR, Suit.HEART)])
        self.assertTrue(hand1 > hand2)

        hand1 = Hand(cards = [Card(Rank.JACK, Suit.SPADE), Card(Rank.KING, Suit.SPADE), Card(Rank.JACK, Suit.HEART)])
        hand2 = Hand(cards = [Card(Rank.ACE, Suit.SPADE), Card(Rank.THREE, Suit.SPADE), Card(Rank.FOUR, Suit.SPADE)])
        self.assertTrue(hand1 > hand2)

        hand1 = Hand(cards = [Card(Rank.ACE, Suit.SPADE), Card(Rank.THREE, Suit.SPADE), Card(Rank.FOUR, Suit.SPADE)])
        hand2 = Hand(cards = [Card(Rank.ACE, Suit.HEART), Card(Rank.THREE, Suit.HEART), Card(Rank.FOUR, Suit.DIAMOND)])
        self.assertTrue(hand1 == hand2) # compare deng later

        hand1 = Hand(cards = [Card(Rank.ACE, Suit.SPADE), Card(Rank.THREE, Suit.SPADE), Card(Rank.FOUR, Suit.CLUB)])
        hand2 = Hand(cards = [Card(Rank.ACE, Suit.HEART), Card(Rank.THREE, Suit.HEART), Card(Rank.FOUR, Suit.DIAMOND)])
        self.assertTrue(hand1 == hand2)

        hand1 = Hand(cards = [Card(Rank.ACE, Suit.SPADE), Card(Rank.THREE, Suit.SPADE)])
        hand2 = Hand(cards = [Card(Rank.ACE, Suit.HEART), Card(Rank.ACE, Suit.SPADE), Card(Rank.TWO, Suit.DIAMOND)])
        self.assertTrue(hand1 == hand2) # compare deng later

        hand1 = Hand(cards = [Card(Rank.ACE, Suit.SPADE), Card(Rank.THREE, Suit.DIAMOND)])
        hand2 = Hand(cards = [Card(Rank.ACE, Suit.HEART), Card(Rank.ACE, Suit.SPADE), Card(Rank.TWO, Suit.DIAMOND)])
        self.assertTrue(hand1 == hand2)

        hand1 = Hand(cards = [Card(Rank.ACE, Suit.SPADE), Card(Rank.TWO, Suit.SPADE)])
        hand2 = Hand(cards = [Card(Rank.ACE, Suit.HEART), Card(Rank.TEN, Suit.HEART), Card(Rank.TWO, Suit.HEART)])
        self.assertTrue(hand1 == hand2) # compare deng later

        hand1 = Hand(cards = [Card(Rank.ACE, Suit.SPADE), Card(Rank.TWO, Suit.HEART)])
        hand2 = Hand(cards = [Card(Rank.ACE, Suit.HEART), Card(Rank.TEN, Suit.HEART), Card(Rank.JACK, Suit.DIAMOND)])
        self.assertTrue(hand1 > hand2)

        hand1 = Hand(cards = [Card(Rank.FIVE, Suit.SPADE), Card(Rank.FOUR, Suit.CLUB)])
        hand2 = Hand(cards = [Card(Rank.NINE, Suit.SPADE), Card(Rank.NINE, Suit.DIAMOND)])
        self.assertTrue(hand1 > hand2)

if __name__ == '__main__':
    main()
