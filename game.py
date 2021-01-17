import random
import sys

board = [' ' for x in range(10)]


def insert_into_board(letter, position):
    global board
    board[position] = letter


def space_is_free(position):
    return board[position] == ' '


def is_winner(b, l):
    # This function returns if the player has won or not
    # Used b instead of board and l instead of letter
    return ((b[7] == l and b[8] == l and b[9] == l) or  # top
            (b[4] == l and b[5] == l and b[6] == l) or  # middle
            (b[1] == l and b[2] == l and b[3] == l) or  # bottom
            (b[7] == l and b[4] == l and b[1] == l) or  # side
            (b[8] == l and b[5] == l and b[2] == l) or  # down middle
            (b[9] == l and b[6] == l and b[3] == l) or  # down right side
            (b[7] == l and b[5] == l and b[3] == l) or  # diagonal
            (b[9] == l and b[5] == l and b[1] == l))  # diagonal


def player_move():
    value = True
    while value:
        move = input('Please select a position to place an \\\'X\\\' (1-9): ')
        try:
            move = int(move)
            if 0 < move < 10:
                if space_is_free(move):
                    value = False
                    insert_into_board('X', move)
                else:
                    print('This position is already occupied!')
            else:
                print('Print a number within the the range!')
        except:
            print('Please type a number')


def random_move(le):
    length = len(le)
    random_int = random.randrange(0, length)
    return le[random_int]


def computer_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    # Checks for winning move or block opponent from winning
    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    # Tries to take one of the corner
    corners_open = []
    for j in possible_moves:
        if j in [1, 3, 7, 9]:
            corners_open.append(j)

        if len(corners_open) > 0:
            move = random_move(corners_open)
            return move

    # Tries to take the center
    if 5 in possible_moves:
        move = 5
        return move

    # Takes any edge
    edge_open = []
    for e in possible_moves:
        if e in [2, 4, 6, 8]:
            edge_open.append(e)

        if len(edge_open) > 0:
            move = random_move(edge_open)
            return move

    return move


def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def print_board():
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def main():
    print("Welcome to TicTacToe game?")
    msg = input("Start? Y/N ")

    while msg != "y" or msg != "Y":
        if msg == "n" or msg == "N":
            print("Goodbye!")
            sys.exit()

        else:
            break

    print_board()

    while not (is_board_full(board)):
        if not (is_winner(board, "O")):
            player_move()
            print_board()

        else:
            print("O Wins this time")
            break

        if not (is_winner(board, "X")):
            move = computer_move()
            if move == 0:
                print("Game is Tie! No more spaces left")
            else:
                insert_into_board("O", move)
                print('Computer placed an O in position', move, ':')
                print_board()
        else:
            print("X Wins! Good Job")
            break

    if is_board_full(board):
        print("Game is Tie! No more spaces left")


main()

while True:
    again = input("Would you like to play again? Y/N ")
    if again == "Y" or again == "y":
        board = [" " for x in range(10)]
        print("-----------------------------")
        main()
    else:
        print("Thank You For Playing!")
        sys.exit()
