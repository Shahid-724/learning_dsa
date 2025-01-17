# Rock, Paper, Scissors
import sys
import random
from enum import Enum

# Declaring an enumeration for printing names instead of numbers
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# Play continuously using a while loop
play_again = True

while play_again:
    # Taking input from the users
    player_choice = input('Enter\n1 for Rock...\n2 for Paper...\n3 for Scissors\n\n')
    player = int(player_choice)

    # Making sure that the user input is valid
    if player < 1 or player > 3:
        sys.exit('You must enter 1 or 2 or 3')

    # A random choice made by the computer
    computer_choice = random.choice('123')
    computer = int(computer_choice)

    # Displaying the choices of user and computer
    print(f'\nYou chose {RPS(player)}'.replace('RPS.', ''))
    print(f'Python chose {RPS(computer)}\n'.replace('RPS.', ''))

    # The main logic to decide the winner
    if player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
        print('Player wins!🎉')
    elif player == computer: 
        print('Tie game!😲')
    else:
        print('Python wins!🐍\n')

    # Asking user input if he/she wants to play again
    play_again = input('\nPlay again?\n Y for Yes \n Q to Quit\n\n')
     
    if play_again.lower() == 'y':
        continue
    else:
        print('\n🎉🎉🎉🎉')
        print('Thank you for playing!\n')
        play_again = False
        # You can also use break 

sys.exit('Bye!👋\n')
