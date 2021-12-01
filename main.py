game_board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
player = "X"
isWinner = False

def print_board(board_array):
  first_line = f"  {board_array[0]}  |  {board_array[1]}  |  {board_array[2]}  "
  second_line = f"  {board_array[3]}  |  {board_array[4]}  |  {board_array[5]}  "
  third_line = f"  {board_array[6]}  |  {board_array[7]}  |  {board_array[8]}  "

  print(first_line)
  print("----------------")
  print(second_line)
  print("----------------")
  print(third_line)
  
while not isWinner:
    print_board(game_board)
    
    # Prompt the user for their space selection
    print(f"Player is: {player}")
    print("Choose an available space, 0-8")
    user_input = input()
    
    # Try to parse the input as an integer
    space = None
    try:
        space = int(user_input)
    except ValueError:
        print("Invalid input, try again.")
        continue
    
    if space < 0 or space > 8:
        print("Space must be between 0 and 8")
        continue

    # Now we know that the user has input a number 0-8
    # Check to make sure this space isn't currently occupied.
    if game_board[space] is not "-":
        print("Space is not available. Try again.")
        continue

    game_board[space] = player

    # Check to see if this move made the player win

    # Check to see if all of the spaces are full (no more "-" exist in the array)
    # If so, it was a tie

    # Swap player
