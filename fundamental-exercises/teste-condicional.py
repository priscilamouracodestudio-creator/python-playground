print('Welcome to DETRAN!')
print()
idade = int(input('Please, insert your age: '))

if idade > 70:
  print('You have permission, but you need to renew your license every 3 years!')

elif idade >= 18:
  print('You have permission to get your drive/ride license!')

else:
  print("You are a minor. You don't have permission do drive/ride yet.")  