game_board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
player = "X"
is_winner = False


def print_board(board_array):
    first_line = f"  {board_array[0]}  |  {board_array[1]}  |  {board_array[2]}  "
    second_line = f"  {board_array[3]}  |  {board_array[4]}  |  {board_array[5]}  "
    third_line = f"  {board_array[6]}  |  {board_array[7]}  |  {board_array[8]}  "

    print(first_line)
    print("----------------")
    print(second_line)
    print("----------------")
    print(third_line)


def check_win(board, player):
    win_combos = [
        [0, 1, 2],
        [0, 3, 6],
        [0, 4, 8],
        [1, 4, 7],
        [2, 4, 6],
        [2, 5, 8],
        [3, 4, 5],
        [6, 7, 8]
    ]

    for combo in win_combos:
        first = board[combo[0]]
        second = board[combo[1]]
        third = board[combo[2]]
        if first is player and second is player and third is player:
            # If all 3 spaces of this win combo are occupied by player
            return True
    return False


def check_board_full(board):
    for space in board:
        if space == "-":
            # If any space is still a "-" then the board is not full
            return False
    return True


def swap_player(player):
    if player == "X":
        return "O"
    return "X"


while not is_winner:
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

    if space < 1 or space > 9:
        print("Space must be between 0 and 8")
        continue

    # Offset the input by -1 to match the array index.
    # User types 1, it maps to array index 0
    space = space - 1

    # Now we know that the user has input a number 0-8
    # Check to make sure this space isn't currently occupied.
    if game_board[space] != "-":
        print("Space is not available. Try again.")
        continue

    game_board[space] = player

    # Check to see if this move made the player win
    is_winner = check_win(game_board, player)
    if is_winner:
        print(f"Winner is {player}!")
        break

    # Check to see if all of the spaces are full (no more "-" exist in the array)
    # If so, it was a tie
    is_board_full = check_board_full(game_board)
    if is_board_full:
        print("Tie!")
        break

    # Swap player
    player = swap_player(player)

print_board(game_board)
