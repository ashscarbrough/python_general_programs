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
    '''
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for row in range(GRID_SIZE):
        grid.append([])
        for column in range(GRID_SIZE):
            grid[row].append(" ")

# Check Win
def check_win():
    '''
    Check grid for winning combinations
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

# Process user input
def play_new_game(user_input):
    '''
    '''
    user_input = user_input.upper()
    if user_input == "Y" or user_input == "YES":
        return True
    else:
        False


def check_valid_input(user_row_input, user_column_input):
    '''
    
    '''
    if grid[user_row_input][user_column_input] != " ":
        return False
    return True

# Mark Grid
def mark_grid(user_row_input, user_column_input):
    '''
    
    '''
    global player
    grid[user_row_input][user_column_input] = player


# Print Board
def print_grid():
    '''
    
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
    
    '''
    global player
    if player == "O":
        player = "X"
    else:
        player = "O"

def main():
    # user_new_game = input("Welcome to Tic Tac Toe.  Would you like to play a new game? [Y, N] ")
    # if play_new_game(user_new_game):
    #     initialize_grid()
    # else:
    #     print("Exiting Game")
    #     sys.exit()
    
    initialize_grid()

    continue_game = True
    while continue_game is True:
        print_grid()
        user_row_input = literal_eval(input("Which row would you like to mark for player " + player + " (0, 1, or 2): "))
        user_column_input = literal_eval(input("Which column would you like to mark for player " + player + " (0, 1, or 2): "))
        
        while check_valid_input(user_row_input, user_column_input) is False:
            print ("Sorry, that space is already taken. Provide a different entry.")
            user_row_input = literal_eval(input("Which row would you like to mark for player " + player + " (1, 2, or 3): "))
            user_column_input = literal_eval(input("Which column would you like to mark for player " + player + " (1, 2, or 3): "))

        mark_grid(user_row_input, user_column_input)

        if check_win() == "win":
            print("***************************")
            print_grid()
            print("***************************")
            print("Congratulations, player", player, "won!")
            print()
            continue_game = False
        elif check_win() == "tie":
            print("Sorry, tie game!")
            continue_game = False
            # play_again = input("Would you like to play again?")
            # if play_again:
            #     play_new_game()
        else:
            change_player()



main()


