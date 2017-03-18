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

def display_grid():
    '''
    this function displays the current gameboard
    a 3x3 grid
    '''
    for row in gamestate:
        print(row)

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

    determine_game_status()
    return userInput

def validate_input(user_input):
    '''
    returns true if the user input is 1 - 9, else false
    '''
    numbers = string.digits[1:]
    for number in numbers:
        if user_input == number:
            return True

    print("Your choice must be a number 1 - 9")
    return False

def determine_game_status():
    '''
    returns one of the following strings:
    Pending, X wins, O wins, Draw
    '''
    


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
    display_grid()
    print_padding()

welcome_players()
while current_status == "Pending":
    display_grid()
    choice = get_user_input()
    update_grid(choice)
