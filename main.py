from IPython.display import clear_output
import random

def display_board(board):

    clear_output(board)
    print('\n'+ board[7]+'|' + board[8]+'|' + board[9])
    print(board[4]+'|' + board[5]+'|' + board[6])
    print(board[1]+'|' + board[2]+'|' + board[3] + '\n')

def player_input():
    marker = ''

    while marker !='X' and marker !='O':
        marker = input('Player 1: Choose X or O: ').upper()
        if marker == 'X':
            print("player 1 : X\nPlayer 2 : O")
            return ('X','O')
        elif marker == 'O':
            print("player 1 : O\nPlayer 2 : X")
            return ('O','X')


test_board = ['#','X','O','X','O','X','O','X','O','X']
board = [' ',' ' ,' ',' ',' ',' ',' ',' ',' 6','7 ']

def place_marker(board, marker, position):

    board[position] = marker


def win_check(board, mark):

    return (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark) or (board[7] == board[4] == board[1] == mark) or (board[8] == board[5] == board[2] == mark) or (board[9] == board[6] == board[3] == mark) or (board[7] == board[5] == board[3] == mark) or (board[9] == board[5] == board[1] == mark)

def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def check_space(board, position):

    return board[position] == ' '

def full_board_check(board):

    for i in range(1,10):
        if check_space(board, i):
            return False

    return True

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not check_space(board,position):
        position = int(input('Choose a position: (1-9): '))

    return position

def replay():

    choice = input('Play again?\nEnter Yes or No: ').upper()

    return choice == 'YES' or choice == 'Y'

print('Welcome to Tic Tac Toe')

while True:

    the_board = [' ']*10
    player1,player2 = player_input()

    turn = choose_first()
    print(f"{turn} will go first")

    play_game = input('Ready to play? \nY or N : ').upper()

    if play_game == "YES" or play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1,position)

            if win_check(the_board,player1):
                display_board(the_board)
                print('Player 1 has Won!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board, player2, position)

                if win_check(the_board, player2):
                    display_board(the_board)
                    print('Player 2 has Won!!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('Tie Game!!')
                        game_on = False
                    else:
                        print("Player 1 Turn")
                        turn = "Player 1"

    if not replay():
        break