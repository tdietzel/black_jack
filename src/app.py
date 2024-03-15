import random
import os

class BlackJack:
  def __init__(self):
    self.balance = 1000  #starting balance for the player
    self.load_balance()

  def save_balance(self):
    with open("balance.txt", "w") as file:
      file.write(str(self.balance))
    print('New Balance:', self.balance)

  def load_balance(self):
    if os.path.exists("balance.txt"):
      with open("balance.txt", "r") as file:
        self.balance = int(file.read())

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
      print('House card:', f"{hand[0]['rank']} of {hand[0]['suit']}", '\nHouse card: ~ Flipped Over ~')
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
      score += BlackJack.card_value(card)
    return score

  @staticmethod
  def play_hit(player_hand, house_hand, deck, game):
    new_card = deck.pop()
    player_hand.append(new_card)
    player_score = BlackJack.calc_score(player_hand)
    house_score = BlackJack.calc_score(house_hand)

    if player_score > 21:
      print(f'\nYou flipped a {new_card["rank"]}. Your total is {player_score}')
      print('Bust! You lose')
      game.balance -100
      game.save_balance()
    elif player_score == 21:
      print(f'\nYou flipped a {new_card["rank"]}. Your total is {player_score}')
      print('Blackjack! You win')
      game.balance += 100
      game.save_balance()
    else:
      for card in player_hand:
        print('Your cards:', f"{card['rank']} of {card['suit']}")  # prints out new list of player cards
      print("~---~---~---~----~---~---~---~----~")
      print(f"Your total: {player_score} | House total: {house_score}")  # prints out total game score

      game_choice = input("Do you want to hit? ").lower()
      if game_choice == 'yes':
        BlackJack.play_hit(player_hand, house_hand, deck, game)
      elif game_choice == 'no':
        return BlackJack.play_stand(player_score, house_score, house_hand, deck, game)

  @staticmethod
  def play_stand(player_score, house_score, house_hand, deck, game):
    while house_score < player_score and house_score < 21:
      new_card = deck.pop()
      house_hand.append(new_card)
      house_score = BlackJack.calc_score(house_hand)
      print(f"House draws.. {new_card['rank']}", 'House is now at: ', house_score)

    if player_score < house_score and house_score < 21:
      print('You lost')
      game.balance -= 100
      game.save_balance()
      return False
    elif player_score > house_score and player_score < 21:
      print('You win')
      game.balance += 100
      game.save_balance()
      return True
    elif house_score > 21:
      print('House went bust! You win')
      game.balance += 100
      game.save_balance()
      return True
    elif player_score == 21:
      print('Blackjack! You win')
      game.balance += 100
      game.save_balance()
      return True
    elif house_score == 21:
      print('House got Blackjack! You lose')
      game.balance -= 100
      game.save_balance()
      return False
    else:
      print("Draw")
      return False

  @staticmethod
  def play_game():
    game = BlackJack()
    deck = BlackJack.create_deck()
    player_hand, house_hand = BlackJack.deal_hand(deck)

    BlackJack.print_hand(house_hand, True)
    BlackJack.print_hand(player_hand, False)

    print('____________________________________________________')
    game_choice = input('Do you want to hit? ')
    if game_choice == 'yes':
      BlackJack.play_hit(player_hand, house_hand, deck, game)
    elif game_choice == 'no':
      BlackJack.play_stand(BlackJack.calc_score(player_hand), BlackJack.calc_score(house_hand), house_hand, deck, game)

BlackJack.play_game()