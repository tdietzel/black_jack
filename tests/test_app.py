import sys
sys.path.append("../src")
from app import BlackJack
import unittest

class BlackJackTests(unittest.TestCase):

  def test_create_deck(self):
    deck = BlackJack.create_deck()

    self.assertEqual(len(deck), 52)

  def test_card_value(self):
    deck = BlackJack.create_deck()
    cardValue = BlackJack.card_value(deck[0])

    self.assertIn(cardValue, range(11))

  def test_deal_hand(self):
    deck = BlackJack.create_deck()
    playerHand, houseHand = BlackJack.deal_hand(deck)

    self.assertEqual(len(playerHand), 2)
    self.assertEqual(len(houseHand), 2)

  def test_print_hand(self):
    deck = BlackJack.create_deck()
    playerHand, houseHand = BlackJack.deal_hand(deck)

    self.assertEqual(BlackJack.print_hand(playerHand, hidden = False), False)
    self.assertEqual(BlackJack.print_hand(houseHand, hidden = True), True)

  def test_calc_score(self):
    deck = BlackJack.create_deck()
    playerHand, houseHand = BlackJack.deal_hand(deck)
    playerScore = BlackJack.card_value(playerHand[0]) + BlackJack.card_value(playerHand[1])
    houseScore = BlackJack.card_value(houseHand[0]) + BlackJack.card_value(houseHand[1])

    self.assertEqual(BlackJack.calc_score(playerHand), playerScore)
    self.assertEqual(BlackJack.calc_score(houseHand), houseScore)

if __name__ == '__main__':
  unittest.main()

#play_game is untested line #25