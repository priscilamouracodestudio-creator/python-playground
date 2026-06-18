import random
print('-----GUESS THE NUMBER-----')

print('Think about a number between 1 and 10...')

input()

print('... I am thinking...')
input()

chosen_number = random.randint(1, 10)

print('The number you are thinking is...')
input()

print(f'...{chosen_number}! I am right?!')
  
