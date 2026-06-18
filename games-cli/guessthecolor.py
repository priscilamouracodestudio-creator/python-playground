import random

print('--- GUESS THE COLOR ---')

print('Let me try read your mind and find what color you are thinking...')

input('Are you ready?...')

input('... Hummm...')

colors = ['navy-blue', 'baby-blue', 'blue', 'light-blue', 
'dark-blue', 'turquoise', 'orange', 'yellow', 'white', 
'dark-gray', 'light-gray', 'gray', 'dark-brown', 'light-brown',
'light-pink', 'dark-pink', 'pink', 'dark-green', 'light-green', 'green',
'violet', 'dark-purple', 'light-purple', 'red', 'black', 'beige'
]

chosen_color = random.choice(colors)

print(f'... the color in your mind is {chosen_color}! Am I right?')