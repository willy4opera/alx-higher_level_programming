#!/usr/bin/python3

"""SThis program solves the N-queens puzzle.

It Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    bd = []
    [bd.append([]) for num in range(n)]
    [row.append(' ') for num in range(n) for row in bd]
    return (bd)


def bd_deepcpy(bd):
    """Return a deepcopy of a chessboard."""
    if isinstance(bd, list):
        return list(map(bd_deepcpy, bd))
    return (bd)


def get_solution(bd):
    """Return the list of lists representation of a solved chessboard."""
    soltion = []
    for r in range(len(bd)):
        for c in range(len(bd)):
            if bd[r][c] == "Q":
                soltion.append([r, c])
                break
    return (soltion)


def xout(bd, row, col):
    """X out spots on a chessbd.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for c in range(col + 1, len(bd)):
        bd[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        bd[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(bd)):
        bd[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        bd[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(bd)):
        if c >= len(bd):
            break
        bd[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        bd[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(bd):
            break
        bd[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(bd)):
        if c < 0:
            break
        bd[r][c] = "x"
        c -= 1


def recursive_solve(bd, row, queens, soltions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(bd):
        soltions.append(get_solution(bd))
        return (soltions)

    for c in range(len(bd)):
        if bd[row][c] == " ":
            tmp_board = bd_deepcpy(bd)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            soltions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, soltions)

    return (soltions)


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

    bd = init_board(int(sys.argv[1]))
    soltions = recursive_solve(board, 0, 0, [])
    for sol in soltions:
        print(sol)
