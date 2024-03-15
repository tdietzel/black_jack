import random

class black_jack:
  def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

  def card_value(card):
    rank = card['rank']
    if rank in [ 'J', 'Q', 'K']:
      return 10
    elif rank == 'A':
      return 11
    else:
      return int(rank)

  def deal_hand(deck):
    player_hand = [deck.pop(), deck.pop()]
    house_hand = [deck.pop(), deck.pop()]
    return player_hand, house_hand

  def play_game():
    deck = black_jack.create_deck()
    return black_jack.deal_hand(deck)