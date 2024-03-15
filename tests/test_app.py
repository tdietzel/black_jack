import sys
sys.path.append("../src")
from app import black_jack
import unittest

class test_black_jack(unittest.TestCase):

  def test_create_deck(self):
    deck = black_jack.create_deck()

    self.assertEqual(len(deck), 52)

  def test_card_value(self):
    deck = black_jack.create_deck()
    cardValue = black_jack.card_value(deck[0])

    self.assertIn(cardValue, range(11))

  def test_deal_hand(self):
    playerHand, houseHand = black_jack.play_game()
    self.assertEqual(len(playerHand), 2)
    self.assertEqual(len(houseHand), 2)

if __name__ == '__main__':
  unittest.main()

#play_game is untested line #25