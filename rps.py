# Code for Rock, Paper, Scissors
import sys
import random
from enum import Enum

# Defining an enum for display of names instead of numbers
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# Getting User input
player_choice = input('Enter\n1 for Rock\n2 for Paper\n3 for Scissors\n\n')
player = int(player_choice)
print('')

# Making sure that user input is valid
if player < 1 or player > 3:
    sys.exit('You must enter 1 or 2 or 3')

# Computer making a random choice
computer_choice = random.choice('123')
computer = int(computer_choice)

# Displaying the choices of user and computer
print(f'You chose {RPS(player)}'.replace('RPS.', ''))
print(f'Python chose {RPS(computer)}'.replace('RPS.', ''))
print('')

# The main logic for deciding the winner
if player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
    print('Player wins!🎉')
elif player == computer:
    print('Tie game!😲')
else:
    print('Python wins!🐍')

print('')