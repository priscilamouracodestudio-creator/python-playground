print('-----PASSWORD REGISTRATION----')


registered_password = input('Create your new password: ')
print('Password saved successfully!\n')

print('-----LOGIN SYSTEM-----')

attempt = input('Please, insert your password to login: ')

while attempt != registered_password:
  print('Your password is wrong, please try again!')
  attempt = input('Please, insert your password to login: ')
  
else:
  print('Access granted! Welcome!')