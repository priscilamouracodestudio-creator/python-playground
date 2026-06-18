import time

print('-----A FUNNY STORY-----')

print("Let's create a fun story! Please, answer the questions below...")
print("Press 'Enter' when you are ready!")
input()
name_famous = input('Please, insert a name of a famous person: ').title()
animal = input('Please, insert a animal: ').lower()
adjective = input('Give me a adjective: ').lower()
object_kitchen = input('Enter a type of object kitchen: ').lower()
verb_past = input('Give me a verb in the past: ').lower()
place = input('Think about a place... type here: ').lower()
food = input('Insert a delicious food: ').lower()
number_chosen = input('Give me a quantity in coins: ')
part_body = input('What is your favorite part of body? ').lower()


print('Are you ready to have some laughs? Prepares choices in...')
for second in range(5, 0, -1):
  print(f'Revealing in: {second} seconds...', end='\r')
  time.sleep(1)

print()




print(f"""Last night, a terrible mistery happened. The famous detective {name_famous} was called to investigate the disappearence of a very {adjective} {animal}.

The only clue left at the crime scene was a broken {object_kitchen}. With no time to waste, the detective {verb_past} to the {place} to interregate the suspects.

There, he found the guilty party eating a huge portion of {food}. As punishment, the  thief had to pay {number_chosen} gold coins and promised never to scratch their {part_body} in public again. The case was closed!""")