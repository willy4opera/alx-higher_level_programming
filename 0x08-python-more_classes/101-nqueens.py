#!/usr/bin/python3


import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    bdlis = []
    [bdlis.append([]) for num in range(n)]
    [row.append(' ') for num in range(n) for row in bdlis]
    return (bdlis)


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Function Return the list of lists representation of a solved chessboard."""
    sol= []
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == "Q":
                solution.append([x, y])
                break
    return (sol)


def xout(board, row, col):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for num in range(col + 1, len(board)):
        board[row][num] = "x"
    # X out all backwards spots
    for num in range(col - 1, -1, -1):
        board[row][num] = "x"
    # X out all spots below
    for x in range(row + 1, len(board)):
        board[x][col] = "x"
    # X out all spots above
    for x in range(row - 1, -1, -1):
        board[x][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for num in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for num in range(row - 1, -1, -1):
        if c < 0:
            break
        board[num][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for num in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[num][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for num in range(row + 1, len(board)):
        if c < 0:
            break
        board[num][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):

    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for x in range(len(board)):
        if board[row][x] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][x] = "Q"
            xout(tmp_board, row, x)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
