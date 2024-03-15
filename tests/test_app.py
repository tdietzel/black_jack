import sys
sys.path.append("../src")
import app
import unittest

class test_black_jack(unittest.TestCase):

  def test_create_deck(self):
    deck = app.create_deck()

    self.assertEqual(len(deck), 52)

  def test_card_value(self):
    deck = app.create_deck()
    cardValue = app.card_value(deck[0])

    self.assertIn(cardValue, range(11))

if __name__ == '__main__':
  unittest.main()