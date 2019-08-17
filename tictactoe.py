board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def board_draw():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])


def switch_player():
    global player_no
    if player_no == 1:
        print("turn of player o")
        player_no = 0
    else:
        print("turn of player x")
        player_no = 1


def input_board():
    global player_no
    positon = input("choose the input positon 1 to 9 ")

    positon = int(positon) - 1
    player = ["o", "x"]
    # check the positon is already taken
    if board[positon] == "-":

        board[positon] = player[player_no]
    else:
        print("positon is already taken")
        input_board()


def game_termination():
    global game_running
    # checking rows
    for i in (0, 3, 6):
        if board[i] == board[i+1] == board[i+2] == "x" or board[i] == board[i+1] == board[i+2] == "o":
            game_running = False
    # checking coloumns
    for i in (0, 1, 2):
        if board[i] == board[i+3] == board[i+6] == "x" or board[i] == board[i+1] == board[i+2] == "o":
            game_running = False
    # for checking corners
    if board[0] == board[4] == board[8] == "x" or board[0] == board[4] == board[8] == "o":
        game_running = False
    if board[2] == board[4] == board[6] == "x" \or board[2] == board[4] == board[6] == "o":
        game_running = False


def game_winner():

    # checking rows
    for i in (0, 3, 6):
        if board[i] == board[i+1] == board[i+2] == "x":
            print("x is the winner")
        if board[i] == board[i+1] == board[i+2] == "o":
            print(" o is the winner")
    # checking coloumns
    for i in (0, 1, 2):
        if board[i] == board[i+3] == board[i+6] == "x":
            print("x is the winner")
        if board[i] == board[i+1] == board[i+2] == "o":
            print("o is the winner")
    # for checking corners
    if board[0] == board[4] == board[8] == "x":
        print("x is the winner")
    if board[0] == board[4] == board[8] == "o":
        print("o is the winner")
    if board[2] == board[4] == board[6] == "x":
        print("x is the winner")
    if board[2] == board[4] == board[6] == "o":
        print("o is the winner")


def main():
    global game_running

    while game_running:

        input_board()
        board_draw()
        game_termination()
        switch_player()
    print("game over")
    game_winner()


player_no = 1
game_running = True
main()
# game _winner can be removed and integrated in game termination
# to do integrating game score
# integrating ui
# integrating face detection to alter the game result as administrator
# colourize the output to distinguish
