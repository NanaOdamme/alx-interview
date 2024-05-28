#!/usr/bin/python3
import sys


def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)


def print_number_error_and_exit():
    print("N must be a number")
    sys.exit(1)


def print_minimum_error_and_exit():
    print("N must be at least 4")
    sys.exit(1)


def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    def solve(row, board):
        if row == N:
            solutions.append(board[:])
        else:
            for col in range(N):
                if is_valid(board, row, col):
                    board[row] = col
                    solve(row + 1, board)
    
    solutions = []
    solve(0, [-1] * N)
    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_number_error_and_exit()

    if N < 4:
        print_minimum_error_and_exit()

    solve_nqueens(N)
