'''
Create Tic Tac Toe Game
'''
from ast import literal_eval
import sys

GRID_SIZE = 3
grid = []
player = "O"

def initialize_grid():
    '''
    Function initializes the grid with proper rows and columns
    '''
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for row in range(GRID_SIZE):
        grid.append([])
        for column in range(GRID_SIZE):
            grid[row].append(" ")

def new_game():
    '''
    Function to begin a new game and restore grid after a win or tie
    '''
    global player
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            grid[row][column] = " "
    player = "O"

def play_again():
    '''
    Function to ask user if they want to play again
    '''
    user_input = None
    while user_input not in ["Y", "N"]:
        user_input = input("Would you like to play again? [Y, N] ")

    if user_input == "Y":
        new_game()
    else:
        sys.exit()

# Check Win
def check_win():
    '''
    Check grid for winning combinations
    Input: None
    Output: win_tie_continue - (str) representation of win, tie, or continue
    '''
    if (grid[0][0] == grid[0][1] == grid[0][2] != " " or \
        grid[1][0] == grid[1][1] == grid[1][2] != " " or \
            grid[2][0] == grid[2][1] == grid[2][2] != " "  or \
                grid[0][0] == grid[1][0] == grid[2][0] != " "  or \
                    grid[0][1] == grid[1][1] == grid[2][1] != " "  or \
                        grid[0][2] == grid[1][2] == grid[2][2] != " "  or \
                            grid[0][0] == grid[1][1] == grid[2][2] != " "  or \
                                grid[2][0] == grid[1][1] == grid[0][2] != " " ):
        return "win"
    elif (grid[0][0] != " " and grid[0][1] != " " and grid[0][2] != " " and \
        grid[1][0] != " " and grid[1][1] != " " and grid[1][2] != " " and \
            grid[2][0] != " " and grid[2][1] != " " and grid[2][2] != " "):
        return "tie"
    else:
        return "continue"


def check_valid_input(user_row_input, user_column_input):
    '''
    Function to verify that the user supplied input does not overwrite existing inputs
    Inputs:
        - user_row_input - (int) selected row user selected
        - user_column_input - (int) selected column user selected
    Output:
        - valid_input - (bool) whether grid location is free to choose
    '''
    if grid[user_row_input][user_column_input] != " ":
        return False
    return True

# Mark Grid
def mark_grid(user_row_input, user_column_input):
    '''
    Function to mark the grid with the current user marker O, X
    '''
    global player
    grid[user_row_input][user_column_input] = player

# Print Board
def print_grid():
    '''
    Function to print game grid
    '''
    print("-------------")
    print("|", grid[0][0], "|", grid[0][1], "|", grid[0][2], "|")
    print("-------------")
    print("|", grid[1][0], "|", grid[1][1], "|", grid[1][2], "|")
    print("-------------")
    print("|", grid[2][0], "|", grid[2][1], "|", grid[2][2], "|")
    print("-------------")

def change_player():
    '''
    Function to change player to the next player
    '''
    global player
    if player == "O":
        player = "X"
    else:
        player = "O"

def main():
    '''
    Main function to play game
    '''
    print("Welcome to Tic Tac Toe.")

    initialize_grid()

    continue_game = True
    while continue_game is True:
        print_grid()
        user_row_input = literal_eval(input("Which row would you like to mark for player " 
                                            + player + " (0, 1, or 2): "))
        user_column_input = literal_eval(input("Which column would you like to mark for player " 
                                               + player + " (0, 1, or 2): "))

        while check_valid_input(user_row_input, user_column_input) is False:
            print ("Sorry, that space is already taken. Provide a different entry.")
            user_row_input = literal_eval(input("Which row would you like to mark for player " 
                                                + player + " (1, 2, or 3): "))
            user_column_input = literal_eval(input("Which column would you like to mark for player " 
                                                   + player + " (1, 2, or 3): "))

        mark_grid(user_row_input, user_column_input)

        if check_win() == "win":
            print("***************************")
            print_grid()
            print("***************************")
            print("Congratulations, player", player, "won!")
            print()
            play_again()

        elif check_win() == "tie":
            print("Sorry, tie game!")
            play_again()
        else:
            change_player()

main()
