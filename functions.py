
def play_game(game_board,current_player):
    '''
    main loop that only terminates on exiting
    :return:Null
    '''
    # display game board
    display_game_board(game_board)
    game_still_on = True
    winner = None
    while game_still_on:
        # Handle a turn
        handle_turn(current_player,game_board)

        # Check if game over
        game_still_on = '-' in game_board
        game_still_on,winner = check_for_winner(game_board)

        # Flip to the other player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    # print the winner or tie
    if winner == "X" or winner == "O":
        print(" Congratulations " + winner + ",you won!")
        return True
    elif winner == None:
        print("Game draw.")
        return True


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
            spot = input("Choose a spot from 1-9: ")

        spot = int(spot) - 1

        if game_board[spot] == "-":
            valid = True
        else:
            print("Oops! You have entered an incorrect spot. Try again.")

    game_board[spot] = player

    # display game board
    display_game_board(game_board)



# Check winner
def check_for_winner(game_board):
    '''
    checks which player won the rows columns or diagonals
    '''

    check,winner = check_rows(game_board)
    if check:
        return False,winner
    check,winner = check_columns(game_board)
    if check:
        return False,winner
    check,winner = check_diagonals(game_board)
    if check:
        return False,winner
    return True,None


def check_rows(game_board):
    '''
    checks the board rows for a win
    :return:bool of if the game is over,the shape of the winner's piece
    '''

    if game_board[0] == game_board[1] == game_board[2] != "-":
        return True,game_board[0]
    elif game_board[3] == game_board[4] == game_board[5] != "-":
        return True,game_board[3]
    elif game_board[6] == game_board[7] == game_board[8] != "-":
        return True,game_board[6]
    else:
        return False,None


def check_columns(game_board):
    '''
    checks the board columns for a win
    :return:the shape of the winner's piece
    '''


    if game_board[0] == game_board[3] == game_board[6] != "-":
        return True,game_board[0]
    elif game_board[1] == game_board[4] == game_board[7] != "-":
        return True,game_board[1]
    elif game_board[2] == game_board[5] == game_board[8] != "-":
        return True,game_board[2]
    else:
        return False,None



def check_diagonals(game_board):
    '''
    checks the board diagonals for a win
    :return:the shape of the winner's piece
    '''

    if game_board[0] == game_board[4] == game_board[8] != "-":
        return True,game_board[0]
    elif game_board[2] == game_board[4] == game_board[6] != "-":
        return True,game_board[2]
    else:
        return False,None




