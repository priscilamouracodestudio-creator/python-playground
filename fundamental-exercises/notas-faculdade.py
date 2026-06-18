print('The student is approved?')

student_note = float(input('Please, insert the note: '))

if student_note >= 7.0:
  print('The student is approved!')

elif student_note >= 5.0:
  print('The student is in remediation (recovery)!')

else:
  print('The student has failed!')
