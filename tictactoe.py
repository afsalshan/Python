from colr import color
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def board_draw():
    print(color(board[0]+"|"+board[1]+"|"+board[2],fore='yellow',back='red'))
    print(color(board[3]+"|"+board[4]+"|"+board[5],fore='yellow',back='red'))
    print(color(board[6]+"|"+board[7]+"|"+board[8],fore='yellow',back='red'))


def switch_player():
    global player_no
    if player_no == 1:
        print(color("turn of player o",fore='red'))
        player_no = 0
    else:
        print(color("turn of player x",fore='green'))
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
            if board[i] == "x":
                print("x is the winner")
            else:
                print("o is the winner")

            game_running = False
    # checking coloumns
    for i in (0, 1, 2):
        if board[i] == board[i+3] == board[i+6] == "x" or board[i] == board[i+1] == board[i+2] == "o":
            if board[i] == "x":
                print("x is the winner")
            else:
                print("o is the winner")
            game_running = False
    # for checking corners
    if board[0] == board[4] == board[8] == "x" or board[0] == board[4] == board[8] == "o":
        if board[0] == "x":
            print("x is the winner")
        else:
            print("o is the winner")
        game_running = False
    if board[2] == board[4] == board[6] == "x" or board[2] == board[4] == board[6] == "o":
        if board[2] == "x":
            print("x is the winner")
        else:
            print("o is the winner")
        game_running = False


def main():
    global game_running

    while game_running:

        input_board()
        board_draw()
        switch_player()
        game_termination()

    print("game over")


player_no = 1
game_running = True
main()
# game _winner can be removed and integrated in game termination -done
# to do integrating game score
# integrating ui
# integrating face detection to alter the game result as administrator
# colourize the output to distinguish -done
