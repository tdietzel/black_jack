import random

def create_deck():
  ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
  suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
  random.shuffle(deck)
  return deck