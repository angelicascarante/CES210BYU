#create a board
#display board
#play game
#handle turn
#check win
#check tie
#flip player

#game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#If the game is still going:
game_still_playing = True

winner = None

current_player = "X"

def display_board():
    print (board[0] + "|" + board[1] + "|" + board[2])
    print (board[3] + "|" + board[4] + "|" + board[5])
    print (board[6] + "|" + board[7] + "|" + board[8])


def play_game():
    #display intial board
    display_board()

    while game_still_playing:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(winner + "won.")
    elif winner == None:
        print("That was a tie")

def handle_turn(player):

    print (player + "'s turn")
    position = input("Choose a position between 1 and 9:")

    valid = False
    while not valid:

        while position not in ["1", "2", "3","4","5","6","7","8","9"]:
            position = input ("Please, choose a position between 1 and 9:")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there, try again")

    

    board[position] = player
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():

    #set up global variables
    global winner

    #check rows
    row_winners = check_rows()


    #check columns
    column_winners = check_columns()

    #check diagonals
    diag_winners = check_diagonals()

    if row_winners:
        # wins
        winner = row_winners
    elif column_winners:
        # wins
        winner = column_winners
    elif diag_winners:
        # wins
        winner = diag_winners
    else:
        #no win
        winner = None
    return


def check_rows():
    global game_still_playing
    #check if any of the rows are the same and not empty
    row_1 = board[0]==board[1]==board[2] != "-"
    row_2 = board[3]==board[4]==board[5] != "-"
    row_3 = board[6]==board[7]==board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_playing = False

    #return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return



def check_columns():
    global game_still_playing
    #check if any of the rows are the same and not empty
    column_1 = board[0]==board[3]==board[6] != "-"
    column_2 = board[1]==board[4]==board[7] != "-"
    column_3 = board[2]==board[5]==board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_playing = False

    #return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[3]
    elif column_3:
        return board[6]

    return


def check_diagonals():
    global game_still_playing
    #check if any of the rows are the same and not empty
    diagonals_1 = board[0]==board[4]==board[8] != "-"
    diagonals_2 = board[6]==board[4]==board[2] != "-"
    

    if diagonals_1 or diagonals_2:
        game_still_playing = False

    #return the winner (X or O)
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]

    return


def check_if_tie():
    global game_still_playing

    if "-" not in board:
        game_still_playing = False

    return


def flip_player():

    global current_player
    #if the current player was X change to O
    if current_player == "X":
        current_player = "O"
    #if the current player was O change to X
    elif current_player == "O":
        current_player = "X"
    return



play_game()