import numpy as np
import random

# We use random.seed(0) to make sure
# that our random always returns the same result
random.seed(0)


def initialize():
    # This function creates a numpy 3x3 array 
    # that initializes every value to equal 3
    
    # TODO: Fill in numpy arrays so that we have a 3x3 board filled with values 3 [this marks as empty]
    # NOTE: Our array is 3x3 and every index value should be 3 (blank spot)
    # 0's act as O's -- computer
    # 1's act as X's -- you
    # 3's act as placeholders for blank spots !
    board = np.full((3, 3), 3)
    return board
    
def choose_starting_player():
    # This function chooses the starting player and returns the player
    # it uses random to select the starting player
    # return value 0 = computer goes first
    # return value 1 = player goes first
    coin_flip = random.randint(0, 1)
    if coin_flip == 1:
        print(' Your symbol is X.\nYou go first.')
    else:
        print(' Your symbol is X.\nComputer goes first.')
    # Flip a coin to see who goes first with X's return integer (0 or 1)

    return coin_flip

def display_board(board):
    
    # This function displays the board
    # When printing, follow these conventions:
    # index entry 0 = 'O'
    # index entry 1 = 'X'
    # index entry 3 = ' ' (empty spot)
    
    # TODO: Fill this board list with X,O or ' ' (empty) depending on the situation
    # The list L should be a list (not a numpy Matrix!)
    # flatten() method is used to create a one-dimensional copy of an array
    # by collapsing all the dimensions of the array.

    L = []
    
    for row in board:
        for entry in row:
            if entry == 0:
                L.append('O')
            elif entry == 1:
                L.append('X')
            else:
                L.append(' ')

    # NOTE: print function already displays the board_list, you just have to fill it using L
    
    print(f"""
 {L[0]} | {L[1]} | {L[2]}
---+---+---
 {L[3]} | {L[4]} | {L[5]}
---+---+---
 {L[6]} | {L[7]} | {L[8]}
""")
    
    
def return_open_slots(board):
    # Checks for open slots using Boolean arrays.
    # Important when checking for winner (if draw)
    # checking if user's input is valid
    
    open_slots = []

    # Is spot taken by 3's? If so, then spot is open.
    # Append (i + 1), because inputs are indexed to 1

    flat_board = board.flatten()
    for i in range(0, len(flat_board)):
        if flat_board[i] == 3:
            open_slots.append(i + 1)
            
    return open_slots


def notify_game_end(active_player):
    # if active_player is 1, declare user to be winner
    # if active_player is 0, declare the computer to be winner
    if active_player == 1:
        print("You win!")
    elif active_player == 0:
        print("You lost!")
    else:
        print("Draw!")
        
def check_for_winner(active_player, board_arr):
    # Scans rows, columns, and diagonals for last-played mark
    # E.g. if 1 was the last number played, this function would scan for 1's

    for i in range(0, 3):
        # Checks rows and columns for match
        # Note: The all() function in Python is a built-in method that returns True
        # if all elements in an iterable (such as a list, tuple, NumPy array, etc.) evaluate to True. 

        rows_win = (board_arr[i, :] == active_player).all() # True iff all values in row are True
        cols_win = (board_arr[:, i] == active_player).all() # True iff all values in a column are True
        
        if rows_win or cols_win:
            return True
    # np.diag extracts the diagonal elements and returns them as a one-dimensional array
    # np.fliplr() flips an array horizontally (left to right) along the vertical axis.

    diag1_win = (np.diag(board_arr) == active_player).all()
    diag2_win = (np.diag(np.fliplr(board_arr)) == active_player).all()
    
    if diag1_win or diag2_win:
    # Checks both diagonals for match
        return True
    else:
        return False


def place_symbol(current_num, current_input, board_arr):
    
    # This function places the symbol of the active_player
    # to the given location input number (1-9)
    
    # TODO: Place the active_player symbol 
    # to the the input_location at the board
    
    row, col = divmod(current_input - 1, 3)
    board_arr[row, col] = current_num 

def player_turn(board):
    display_board(board)
    
    # TODO: Read user input according to the example below
    # store it in the variable: user_input = ...
    user_input = int(input("Pick an open slot:\n"))
    

    # Now, the code continues operation
    if user_input in return_open_slots(board):
        place_symbol(1, user_input, board)
    else:
        # NOTE: Notice how this function calls itself if the slot is not open!
        print("That's not an open slot.")
        player_turn(board) # Try again!
    

def comp_turn(board):
    # Randomly chooses from open_slots to place its symbol    
    open_slots = return_open_slots(board)
    comp_input = random.choice(open_slots)
    place_symbol(0, comp_input, board)
    
def change_player(active_player):
    if active_player == 0:
        return 1
    else:
        return 0

def main():
    # Initialize everything
    running = True
    turn_number = 1 # counter for marks in the table
    board = initialize()
    active_player = choose_starting_player()
    while running:
        # Lets run the logic
        if active_player == 0:
            comp_turn(board)
        elif active_player == 1:
            player_turn(board)
        
        # Check if someone won?
        winner = check_for_winner(active_player, board)
        if winner:
            display_board(board)
            notify_game_end(active_player)
            running = False
            break
        # Check if the turn_number is 9 (same as full board!)
        if turn_number == 9: # 
            display_board(board)
            notify_game_end(-1)
            running = False
            break
        
        # If not, set the turn for the next player
        turn_number += 1
        active_player = change_player(active_player) # 

main()
input("Press Enter to continue...")
