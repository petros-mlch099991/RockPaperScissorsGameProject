import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_choice = input('Please choose between [R]ock, [P]aper or [S]cissors: ').lower()

if player_choice in['r', 'rock']:
    player_choice = rock
elif player_choice in['p', 'paper']:
    player_choice = paper
elif player_choice in['s', 'scissors']:
    player_choice = scissors
else:
    raise SystemExit('Invalid input! Please try again.')

computer_choice = random.randint(1, 3)
computer_move = ''

if computer_choice == 1:
    computer_choice = rock
    computer_move = 'Rock'
    print(f'The computer chose: {computer_move}')
elif computer_choice == 2:
    computer_choice = paper
    computer_move = 'Paper'
    print(f'The computer chose: {computer_move}')
else:
    computer_choice = scissors
    computer_move = 'Scissors'
    print(f'The computer chose: {computer_move}')

if (player_choice == rock and computer_choice == scissors) or \
        (player_choice == paper and computer_choice == rock) or \
        (player_choice == scissors and  computer_choice == paper):
    print('Player wins!')
elif player_choice == computer_choice:
    print('Draw!')
else:
    print('Computer wins!')