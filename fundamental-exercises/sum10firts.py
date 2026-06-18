print('---SUM OF THE FIRST TEN NUMBERS---')

sum = 0
n = 1

#while n <= 10:
#  print(f'Actual sum ({sum}) + next number ({n}) = {sum + n}')
#  sum = sum + n
#  n = n + 1
#else:
#  print('-------------------')
#  print(f'The final result is: {sum}')

for i in range(1, 11):
  print(f'Actual sum ({sum}) + next number ({i}) = {sum + i}')
  sum = sum + i
 
else:
  print('-------------------')
  print(f'The final result is: {sum}')