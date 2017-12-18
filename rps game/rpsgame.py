# Rock, Paper, Scissors Game

# import modules
from random import randint
import sys
import os

# ask the player how many games they want to play
def get_game_limit():
  game_limit = 42
  os.system('cls')
  while True:
    try:
      game_limit = int(input('How many games would you like to play?\n--> ' ))
      os.system('cls')
      return int(game_limit)
    except ValueError:
      print ("You didn't enter anything")
    
# randomly generates computer's choice
def get_comp_choice():
  choice = randint(1,3)
  if choice == 1: print ('The computer chose: Rock')   
  elif choice == 2: print ('The computer chose: Paper') 
  elif choice == 3: print ('The computer chose: Scissors')  
  else: print ('The computer malfunctioned')
  return int(choice)

# asks player for their choice
def get_player_choice():
  choice = 0
  while True:
    try:
      choice = int(input( '''Please choose: 
        1: Rock
        2: Paper
        3: Scissors
        --> '''))
    except ValueError: print ("You didn't enter anything")  
    spacer()
    if choice == 1: 
      print ('You chose: Rock')     
      return choice
    if choice == 2: 
      print ('You chose: Paper')     
      return choice
    if choice == 3: 
      print ('You chose: Scissors')
      return choice
      
# compares choices to find a winner
def find_winner(choice1, choice2):
  if choice1 == choice2:
    print ('You tied this round')    
    return 'tie'
  if choice1 == 1 and choice2 == 2:
    print ('You lost this round')    
    return 'comp' 
  if choice1 == 1 and choice2 == 3:
    print ('You won this round!')   
    return 'player'  
  if choice1 == 2 and choice2 == 1:
    print ('You won this round!')    
    return 'player'  
  if choice1 == 2 and choice2 == 3:
    print ('You lost this round')    
    return 'comp'  
  if choice1 == 3 and choice2 == 1:   
    print ('You lost this round')    
    return 'comp' 
  if choice1 == 3 and choice2 == 2:
    print ('You won this round')    
    return 'player'   

# compares wins, losses, and ties
def tally_score(win, lose):
  if win > lose: print ('You won the game!!')  
  elif lose > win: print ('You lost the game!!')
  else: print ('You are evenly matched')

# exits the game
def end_game():
  print ('Thanks for playing!')
  sys.exit()

# prints blank lines and spacers  
def spacer():
  print ()
  print ()
  print ('-' * 50)
  print ()
  print ()

# waits for player to continue  
def wait():
  input("Press Enter to continue...")
  os.system('cls')
  
# main game loop     
def main():
  # defining variables
  game_count = 1
  game_limit = get_game_limit()
  win = 0
  lose = 0
  tie = 0
  
  # continues game loop until game limit reached
  while game_count <= game_limit:
    print ('This is game %d out of %d ' % (game_count, game_limit))
    player_choice = get_player_choice()
    comp_choice = get_comp_choice()
    winner = find_winner(player_choice, comp_choice)
    if winner == 'comp': lose = lose + 1
    if winner == 'player': win = win + 1
    if winner == 'tie': tie = tie + 1
    print ('Wins: %d Losses: %d Ties: %d' % (win, lose, tie))
    game_count = game_count + 1
    wait()
  print ('Wins: %d Losses: %d Ties: %d' % (win, lose, tie))
  tally_score(win, lose)
  end_game()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()