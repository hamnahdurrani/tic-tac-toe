board=[[" "," "," "],[" "," "," "],[" "," "," "]]
i = 0

# Players
player_one = str(input("Enter Name of Player 1 : "))
player_two = str(input("Enter Name of Player 2 : "))

while i < 9:

  # Which Player's turn
  symbol = "X" if i % 2 == 0 else "O"
  current_player = player_one if symbol == "X" else player_two
  print(current_player, "moves")

  # Tile choosing
  row    = int(input("Enter row : "))
  column = int(input("Enter column : "))

  # Check For Invalid Inputs
  if (row > 2 or column > 2) or (row < 0 or column < 0):
    print("Row or Column does not exist")
    continue
  if board[row][column] != " ":
    print("Tile already occupied")
    continue

  # Input Value and Display Updated Board
  board[row][column] = symbol
  for j in range(3):
     print(*board[j], sep = " | ")
     print(*["-"*10])


  # Check win condition
  # Columns
  if board[0][column] == board[1][column] and board[1][column] == board[2][column]:
    print(current_player,"wins!!!")
    break
  # Rows
  if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
    print(current_player,"wins!!!")
    break
  # Primary Diagonal
  if board[0][0] != " " and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
    print(current_player,"wins!!!")
    break
  # Secondary Diagonal
  if board[2][0] != " " and board[2][0] == board[1][1] and board[2][0] == board[0][2]:
    print(current_player,"wins!!!")
    break

  i += 1