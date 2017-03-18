# This is a Tic Tac Toe game intended for the Milestone 1
# Project of the Udemy "Complete Python Bootcamp" course.
# You can read more at
# http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Milestone%20Project%201-%20Assignment.ipynb

'''
So the basic premise of my game is that it will be run from the command
prompt. It will use the number grid to represent the squares, matching the standard numpad on a keyboard:
7   8   9
4   5   6
1   2   3

It will need to:
* display a grid
* update the grid with Xs and Os
* accept and validate user input
* determine a winner or a draw
* manage which player is active
'''

from __future__ import print_function
import string

active_player = "Player One"
active_sign = "X"
current_status = "Pending"
gamestate = [[7, 8, 9], [4, 5, 6], [3, 2, 1]]
keycount = 0    # after 9 valid keys, it's a draw

def change_active_player():
    '''
    Toggles between players and X/O signs
    '''
    global active_player
    global active_sign

    if active_player == "Player One":
        active_player = "Player Two"
        active_sign = "O"
    else:
        active_player = "Player One"
        active_sign = "X"
    pass

def display_grid(nextTurn):
    '''
    this function displays the current gameboard
    a 3x3 grid
    '''
    for row in gamestate:
        print(row)

    if nextTurn:
        print_padding()
        print("It is {}'s turn".format(active_player))
    pass

def update_grid(choice):
    '''
    this function updates the current game board
    the gameboard is represented by a 3x3 grid
    '''
    i = 0
    for row in gamestate:
        j = 0
        for cell in row:
            if str(cell) == str(choice):
                gamestate[i][j] = active_sign
                change_active_player()
                break
            j = j + 1
        i = i + 1

def get_user_input():
    '''
    gets user input from the command line
    '''
    valid_input = False
    while valid_input == False:
        userInput = raw_input("Use the numpad to select a square, or 'Q' to Quit:  ")
        if userInput == "Q" or userInput == "q":
            exit(0)
        valid_input = validate_input(userInput)

    return userInput

def validate_input(user_input):
    '''
    returns true if the user input is 1 - 9, else false
    '''
    global keycount
    numbers = string.digits[1:]
    for number in numbers:
        if user_input == number:
            keycount = keycount + 1
            return True

    print("Your choice must be a number 1 - 9")
    return False

def determine_game_status():
    '''
    returns one of the following strings:
    Pending, X wins, O wins, Draw
    '''
    winner = False

    # we're going to use brute force to determine the game status
    # 7 gamestate[0][0]
    # 4 gamestate[1][0]
    # 8 gamestate[0][1]
    if gamestate[0][0] == gamestate[0][1] and gamestate[0][1] == gamestate[0][2]: #top row
        winner = True
    elif gamestate[1][0] == gamestate[1][1] and gamestate[1][1] == gamestate[1][2]: # middle row
        winner = True
    elif gamestate[2][0] == gamestate[2][1] and gamestate[2][1] == gamestate[2][2]: # bottom row
        winner = True
    elif gamestate[0][0] == gamestate[1][0] and gamestate[1][0] == gamestate[2][0]: #left column
        winner = True
    elif gamestate[0][1] == gamestate[1][1] and gamestate[1][1] == gamestate[2][1]: #mid column
        winner = True
    elif gamestate[0][2] == gamestate[1][2] and gamestate[1][2] == gamestate[2][2]: #right column
        winner = True
    elif gamestate[0][0] == gamestate[1][1] and gamestate[1][1] == gamestate[2][2]: #left-to-right diagonal
        winner = True
    elif gamestate[0][2] == gamestate[1][1] and gamestate[1][1] == gamestate[2][0]:
        winner = True
    else:
        winner = False

    if winner:
        change_active_player()
        display_grid(False)
        print_padding()
        print("Congratulations " + active_player + "! You've won!")
        exit(0)

def print_padding():
    '''
    prints 2 empty lines
    '''
    print("")
    print("")
    pass

def welcome_players():
    '''
    prints a welcome, presents the rules
    '''
    print("Welcome to Xeth's Tic tac Toe!")
    print("The game is played by using the numpad on your keyboard")
    print("It looks like this:")
    print_padding()
    display_grid(True)
    print_padding()

welcome_players()
while keycount < 10:
    display_grid(True)
    choice = get_user_input()
    update_grid(choice)
    determine_game_status()

# if we get to here, it's a draw
print_padding()
print("Oh no, we suck again!")
print("(it's a draw)")
print("Fuck off")
exit(0)
