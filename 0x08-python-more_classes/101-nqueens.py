#!/usr/bin/python3
"""
N queens backtracking program to print the coordinates of N queens
on an NxN grid such that they are all in non-attacking positions
"""


from sys import argv

if __name__ == "__main__":
    arry = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list
    for i in range(n):
        arry.append([i, None])

    def existing(y):
        """check that a queen does not already exist in that y value"""
        for x in range(n):
            if y == arry[x][1]:
                return True
        return False

    def dev_reject(x, y):
        """determines whether or not to reject the solution"""
        if (existing(y)):
            return False
        i = 0
        while(i < x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_arry(x):
        """clears the answers from the point of failure on"""
        for i in range(x, n):
            arry[i][1] = None

    def nqueens(x):
        """recursive backtracking function to find the solution"""
        for y in range(n):
            clear_arry(x)
            if dev_reject(x, y):
                arry[x][1] = y
                if (x == n - 1):  # arryccepts the solution
                    print(arry)
                else:
                    nqueens(x + 1)  # moves on to next x value to continue

    # start the recursive process at x = 0
    nqueens(0)
