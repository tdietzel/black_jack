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
      print('____________________________________________________')
      print('House card:', f"{ hand[0]['rank'] } of { hand[0]['suit'] }", '\nHouse card: ~ Flipped Over ~')
    else:
      print('____________________________________________________')
      for card in hand:
        print('Your cards:', f"{ card['rank'] } of { card['suit'] }")
      print(f'Total: { BlackJack.calc_score(hand) }')
    return hidden #changed to hidden from hand for testing
  
  @staticmethod
  def calc_score(hand):
    score = 0
    for card in hand:
      score += BlackJack().card_value(card)
    return score
  
  @staticmethod
  def play_hit(player_hand, house_hand, deck):
    new_card = deck.pop()
    player_hand.append(new_card) # grabs new card
    player_score = BlackJack.calc_score(player_hand) # gets new score
    house_score = BlackJack.calc_score(house_hand)

    if player_score > 21:
      print(f'\nYou flipped a {new_card['rank']}. Your total is {player_score}')
      print('Bust! You lose')
    elif player_score == 21:
      print(f'\nYou flipped a {new_card['rank']}. Your total is {player_score}')
      print('Blackjack! You win')
    else:
      for card in player_hand:
        print('Your cards:', f"{ card['rank'] } of { card['suit'] }") # prints out new list of player cards
      print("~---~---~---~----~---~---~---~----~")
      print(f"Your total: { player_score } | House total: { house_score }") # prints out total game score

      game_choice = input("Do you want to hit?").lower()
      if game_choice == 'yes':
        BlackJack.play_hit(player_hand, house_hand, deck)

  @staticmethod
  def play_game():
    blackjack = BlackJack()
    deck = blackjack.create_deck() #creates deck
    player_hand, house_hand = blackjack.deal_hand(deck) #deals hand

    blackjack.print_hand(player_hand, False)
    blackjack.print_hand(house_hand, True)

    print('____________________________________________________')
    if input('Do you want to hit? ') == 'yes':
      blackjack.play_hit(player_hand, house_hand, deck)

BlackJack.play_game()