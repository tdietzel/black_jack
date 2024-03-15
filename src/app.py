import random

class BlackJack:
  def __init__(self):
    pass

  @staticmethod
  def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    deck = [{ 'rank': rank, 'suit': suit } for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

  @staticmethod
  def card_value(card):
    rank = card['rank']
    if rank in ['J', 'Q', 'K']:
      return 10
    elif rank == 'A':
      return 11
    else:
      return int(rank)

  @staticmethod
  def deal_hand(deck):
    player_hand = [deck.pop(), deck.pop()]
    house_hand = [deck.pop(), deck.pop()]
    return player_hand, house_hand

  @staticmethod
  def print_hand(hand, hidden):
    if hidden:
      print('House card:', f"{ hand[0]['rank'] } of { hand[0]['suit'] }", '\nHouse card: ~ Flipped Over ~')
    else:
      for card in hand:
        print('Your cards:', f"{ card['rank'] } of { card['suit'] }")
    return hidden #changed to hidden from hand for testing
  
  @staticmethod
  def calc_score(hand):
    score = 0
    for card in hand:
      score += BlackJack().card_value(card)
    return score

  @staticmethod
  def play_game():
    blackjack = BlackJack()
    deck = blackjack.create_deck() #creates deck
    player_hand, house_hand = blackjack.deal_hand(deck) #deals hand

    blackjack.print_hand(player_hand, False)
    blackjack.print_hand(house_hand, True)

BlackJack.play_game()