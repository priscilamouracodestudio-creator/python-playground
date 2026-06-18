import json

print('-----GUESS THE ANIMAL-----')

with open("animal_data.json", "r", encoding="utf-8") as file:
  questions = json.load(file)

while True:
  print('Think about an animal...')

  right = False

  for question in questions:
    answer = input(f'{question[0]} (yes/no): ').lower()
    if answer == 'yes':
      print(f'You thought of a {question[1]}!')
      right = True
      break

  if not right:  
    animal = input('I give up! Which animal do you thought?: ').lower()
    new_question = input('What question would you ask to differentiate this animal?: ').capitalize()
    if not new_question.endswith('?'):
      new_question += '?'
    questions.append([new_question, animal])
    with open("animal_data.json", "w", encoding="utf-8") as file:
      json.dump(questions, file, indent=4, ensure_ascii=False)

  response = input('Do you wanna play more? (yes/no): ').lower()
  if response != 'yes':
    print('Ok! It was good to play with you!')
    break
