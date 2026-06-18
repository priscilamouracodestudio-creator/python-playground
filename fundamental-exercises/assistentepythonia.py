
print('-----THE PYTHONIA ASSISTENT-----')


print('What can I do for you today?')

command = input('Type a command: ').lower()

match command:
  case 'hi'| 'hello':
    print('Hi!, how are you?')
  case 'bye' | 'goodbye':
    print('Bye! It was good to talk with you!')
  case 'joke' | 'gag':
    print('Did you know who was the patron saint of the people that worked with IT? The Saint Login.')
  case 'climate' | 'clime':
    print("It's very waaaaaarm!")
  case _:
    print("Sorry, i don't understand the command.")