
import random

import winsound

def print_board(board):

    for row in board:

        print(" ".join(map(str, row)))

def is_solved(board):

    return board[-1][-1] == 0

def get_blank_position(board):

    for i in range(len(board)):

        for j in range(len(board[0])):

            if board[i][j] == len(board) * len(board[0]) - 1:

                return i, j

def is_valid_move(board, move):

    i, j = get_blank_position(board)

    return 0 <= move < len(board[0]) and (i == 0 or move != j) and (i == len(board) - 1 or move != j)

def make_move(board, move):

    i, j = get_blank_position(board)

    board[i][j], board[i][move] = board[i][move], board[i][j]

    #play_move_sound()

# This will play the system exclamation sound

def shuffle_board(board, num_moves):

    for _ in range(num_moves):

        i, j = get_blank_position(board)

        possible_moves = [m for m in range(len(board[0])) if is_valid_move(board, m)]

        move = random.choice(possible_moves)

        make_move(board, move)

def show_info():

    print("Hi, Welcome to our Puzzle Game")

    print("Arrange the tiles in ascending order.")

    print("Enter the number you want to move, and enter 0 if you want to quit.")

def get_input():

    try:

        return int(input("Enter the number you want: "))

    except ValueError:

        print("Incorrect input. Try again")

        return get_input()

def hint(board):

    row, col = get_blank_position(board)

    print("This is your hint: You can move the blank space to the row number", row, ", and the column number.", col)

def display_score(num_moves):

    num_moves =num_moves-1

    print("Your score:",num_moves , "moves")

def main():

    board_size = 3

    num_moves_to_shuffle = 100

# Initialize the board

    board = [[i * board_size + j + 1 for j in range(board_size)] for i in range(board_size)]

    board[-1][-1] = 0 # The blank space

# Shuffle the board

    shuffle_board(board, num_moves_to_shuffle)

# Display instructions

    show_info()

    while not is_solved(board):

        print_board(board)

        move = -1

        while not is_valid_move(board, move):

            move = get_input()

        if move == 0:

            print("Quitting the game.")

            break

        make_move(board, move)

        hint(board)

    print("Congratulations! You solved the puzzle.")

    display_score(num_moves_to_shuffle)

if __name__ == "__main__":

    main()