import time
import random

print("------CAN YOU GUESS THE NUMBER?------")

print("Let's have some fun...")

time.sleep(1)

print("... Can you guess the number I'm thinking of?")


pc_number = random.randint(1, 20)
user_attempts = 0

while True:
  user_number = int(input("Please, type your guess (between 1 and 20): "))

  user_attempts += 1
  
  if user_number == pc_number:
    break

  elif user_number < pc_number:
    print("Too low! Try a higher number. ⬆️")

  else:        
    print("Too high! Try a lower number. ⬇️")

print("\n---------------------------------------------------")
print(f"🎉 YOU NAILED IT! The number was {pc_number}.")
print(f"You got it right after {user_attempts} tries. 🏆")
print("-----------------------------------------------------")