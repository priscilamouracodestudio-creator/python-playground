player = 'x'
board = [[' ' for _ in range(3)] for _ in range(3)]

def displayBoard():
  for row in board:
    print(f'|'.join(row))
    print('-' * 5)

def move(row, column):
  if not 0 <= row <= 2 or not 0 <= column <= 2:
    print('Invalid move! Tray again!')
    return player

  if board[row][column] != ' ':
    print('This move has already been made... please try a different one.')
    return player
  board[row][column] = player
  return 'o' if player == 'x' else 'x'

def winner():
  """Check the rows"""
  for row in range(3):
    if(
      board[row][0] != ' ' and
      board[row][0] == board [row][1] and
      board[row][0] == board [row][2]
    ):
      print(f'{board[row][0]} YOU WIN!')
      return True
    

  """Check the columns"""
  for column in range(3):
    if(
      board[0][column] != ' ' and
      board[0][column] == board [1][column] and
      board[0][column] == board [2][column]
    ):
      print(f'{board [0][column]} YOU WIN!')
      return True
    

  """Check the diagonals"""
  if (
    board[1][1] != ' ' and
    (
    
      (    
        board[0][0] == board[1][1] and
        board[0][0] == board[2][2]
      ) or
      (
        board[0][2] == board[1][1] and     
        board[1][1] == board[2][0]      
      )
    )  
  ):
    print(f'{board[1][1]} YOU WIN!')
    return True
  
  """If doesn't have a winner"""
  return False 
  
def draw():
  for row in range(3):
    for column in range(3):
      if board[row][column] == ' ':
        return False
  print('Its a draw! Try again!')      
  return True

while True:
  print(f'Player of the round: {player}')
  try:
    row = int(input('Please, enter your row: '))
    if row not in [0, 1, 2]:
      print('Row invalid! Please, enter number values between 0 and 2...')
      continue

    column = int(input('Please, insert your column: '))
    if column not in [0, 1, 2]:
      print('Column invalid! Please, enter number values between 0 and 2...')
      continue

    player = move(row, column)

  except(ValueError):
    print('Please, enter a valid interger number between 0 and 2.')
  
  displayBoard()
  
  if winner() or draw():
    break  

  
