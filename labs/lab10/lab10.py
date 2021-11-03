"""
Name: Patrick Puckhaber
lab10.py
"""


def build_board():
    return list(range(1, 10))


def display_board(board):
    for i in range(3):
        n = i * 3
        print(board[n], "|", board[n+1], "|", board[n+2])
        print(10 * "_")


def fill_spot(board, pos, piece):
    if piece == "x" or piece == "o":
        board[int(pos) - 1] = piece


def spot_legal(board, pos):
    if board[int(pos) - 1] != "x" and board[int(pos) -1] != "o" and 0 < int(pos) < 9:
        return True
    return False


def game_win(board, piece):
    for i in range(3):
        n = i * 3
        if board[n] != piece:
            continue
        if board[n + 1] != piece:
            continue
        if board[n + 2] != piece:
            continue
        return True
    for j in range(3):
        if board[j] != piece:
            continue
        if board[j + 3] != piece:
            continue
        if board[j + 6] != piece:
            continue
        return True
    if board[0] == piece:
        if board[4] == piece:
            if board[8] == piece:
                return True
    if board[2] == piece:
        if board[4] == piece:
            if board[6] == piece:
                return True
    return False


def game_end(board):
    if game_win(board, "x"):
        return True
    elif game_win(board, "o"):
        return True
    else:
        for i in range(9):
            if board[i] == i + 1:
                return False
        return True


def game_play():
    board = build_board()
    while True:
        display_board(board)
        pos = eval(input("x player, select a position to place:"))
        spot_legal(board, pos)
        fill_spot(board, pos, "x")
        if game_end(board):
            if game_win(board, "x"):
                display_board(board)
                print("Player X won!")
                break
            if game_win(board, "o"):
                display_board(board)
                print("Player o won!")
                break
            else:
                display_board(board)
                print("Game is a tie!")

        # return tie
        display_board(board)
        pos = input("o player, select a position to place:")
        spot_legal(board, pos)
        fill_spot(board, pos, "o")
        if game_win(board, "X"):
            if game_win(board, "x"):
                display_board(board)
                print("Player X won!")
                break
            if game_win(board, "o"):
                display_board(board)
                print("Player o won!")
                break
            else:
                display_board(board)
                print("Game is a tie!")


def main():
    # build_board()
    # display_board()
    # fill_spot()
    # spot_legal()
    # game_win()
    # game_end()
    game_play()
    # add other function calls here


main()
