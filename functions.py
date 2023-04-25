
game_still_on = True
# current player
current_player = "X"
# Play game
def play_game(game_board):
    '''
    main loop that only terminates on exiting
    :return:Null
    '''
    # display game board
    display_game_board(game_board)

    while game_still_on:
        # Handle a turn
        handle_turn(current_player,game_board)

        # Check if game over
        check_if_game_over(game_board)

        # Flip to the other player
        flip_player()

    # print the winner or tie
    if winner == "X" or winner == "O":
        print(" Congratulations " + winner + ",you won!")
    elif winner == None:
        print("Game draw.")


def display_game_board(game_board):
    '''
    writes the current state of the game board in console
    :return:Null
    '''
    print("\n")
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2] + "     1 | 2 | 3")
    print("---------")
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5] + "     4 | 5 | 6")
    print("---------")
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8] + "     7 | 8 | 9")
    print("\n")


def handle_turn(player,game_board):
    """
    handles the turn console input process
    :param player:currently playing player
    :return:Null
    """
    # input spot from player
    print(player + "'s turn.")
    spot = input("Choose a spot from 1-9: ")

    valid = False
    while not valid:

        while spot not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            spot = input("Hey! Choose a spot from 1-9: ")

        spot = int(spot) - 1

        if game_board[spot] == "-":
            valid = True
        else:
            print("Oops! You have entered an incorrect spot. Try again.")

    game_board[spot] = player

    # display game board
    display_game_board(game_board)


# Check if game over
def check_if_game_over(game_board):
    '''
    checks both wins and ties
    :return:Null
    '''
    check_for_winner(game_board)
    check_for_tie(game_board)


# Check winner
def check_for_winner(game_board):
    '''
    checks which player won the rows columns or diagonals
    '''
    global winner

    row_winner = check_rows(game_board)
    column_winner = check_columns(game_board)
    diagonal_winner = check_diagonals(game_board)
    # Determine the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows(game_board):
    '''
    checks the board rows for a win
    :return:the shape of the winner's piece
    '''
    global game_still_on

    row_1 = game_board[0] == game_board[1] == game_board[2] != "-"
    row_2 = game_board[3] == game_board[4] == game_board[5] != "-"
    row_3 = game_board[6] == game_board[7] == game_board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_on = False
    # Return  winner
    if row_1:
        return game_board[0]
    elif row_2:
        return game_board[3]
    elif row_3:
        return game_board[6]
    else:
        return None


def check_columns(game_board):
    '''
    checks the board columns for a win
    :return:the shape of the winner's piece
    '''
    global game_still_on

    column_1 = game_board[0] == game_board[3] == game_board[6] != "-"
    column_2 = game_board[1] == game_board[4] == game_board[7] != "-"
    column_3 = game_board[2] == game_board[5] == game_board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_on = False
    # Return the winner
    if column_1:
        return game_board[0]
    elif column_2:
        return game_board[1]
    elif column_3:
        return game_board[2]
    else:
        return None


def check_diagonals(game_board):
    '''
    checks the board diagonals for a win
    :return:the shape of the winner's piece
    '''
    global game_still_on

    diagonal_1 = game_board[0] == game_board[4] == game_board[8] != "-"
    diagonal_2 = game_board[2] == game_board[4] == game_board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_on = False
    # Return the winner
    if diagonal_1:
        return game_board[0]
    elif diagonal_2:
        return game_board[2]
    else:
        return None


# check tie
def check_for_tie(game_board):
    """
    checks the board for blank spaces and ends the game if there arent any
    :return Bool: whether the game ended
    """
    global game_still_on

    if "-" not in game_board:
        game_still_on = False
        return True
    else:
        return False


# Flip the current player
def flip_player():
    """
    changes the current player when their turn ends
    :return:Null
    """
    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
