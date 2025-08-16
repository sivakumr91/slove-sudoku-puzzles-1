import random
import sys

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i!= 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j!= 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    
    for i in range(9):
        if board[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def solve_sudoku(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0

    return False

def is_initial_board_valid(board):
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num!= 0:
                board[i][j] = 0
                if not is_valid(board, i, j, num):
                    return False
                board[i][j] = num
    return True

def get_puzzle_input():
    while True:
        print("\nChoose a Sudoku puzzle:")
        print("1. Easy puzzle")
        print("2. Hard puzzle")
        print("3. Enter your own puzzle (81 characters)")
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        
        if choice == '1':
            return [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ]
        elif choice == '2':
            return [
                [8, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 3, 6, 0, 0, 0, 0, 0],
                [0, 7, 0, 0, 9, 0, 2, 0, 0],
                [0, 5, 0, 0, 0, 7, 0, 0, 0],
                [0, 0, 0, 0, 4, 5, 7, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 3, 0],
                [0, 0, 1, 0, 0, 0, 0, 6, 8],
                [0, 0, 8, 5, 0, 0, 0, 1, 0],
                [0, 9, 0, 0, 0, 0, 4, 0, 0]
            ]
                
        elif choice == '3':
            user_puzzle_string = input("Enter the 81-character puzzle string (use '0' for empty cells): ").strip()
            if len(user_puzzle_string)!= 81:
                print("Error: Puzzle string must be exactly 81 characters long.")
                continue
            
            board = [[0 for _ in range(9)] for _ in range(9)]
            try:
                for i in range(9):
                    for j in range(9):
                        char = user_puzzle_string[i * 9 + j]
                        if char == '.':
                            board[i][j] = 0
                        else:
                            board[i][j] = int(char)
                return board
            except ValueError:
                print("Error: Invalid characters in the puzzle string. Please use digits 0-9.")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def main_game():
    print("--- Sudoku Solver ---")
    print("This program solves Sudoku puzzles using backtracking.")

    while True:
        try:
            sudoku_board = get_puzzle_input()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting program...")
            sys.exit(0)
            
        if not sudoku_board:
            continue
        
        print("\nInitial Puzzle:")
        print_board(sudoku_board)

        if not is_initial_board_valid(sudoku_board):
            print("\nError: The initial puzzle is not a valid Sudoku configuration (contains duplicates).")
        elif solve_sudoku(sudoku_board):
            print("\nSolved Sudoku:")
            print_board(sudoku_board)
        else:
            print("\nNo solution exists for this puzzle.")
        
        while True:
            play_again = input("\nSolve another puzzle? (Y/N): ").strip().lower()
            if play_again in ['y', 'yes']:
                break
            elif play_again in ['n', 'no']:
                print("\nThanks for using the Sudoku Solver. Goodbye.")
                sys.exit(0)
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

if __name__ == "__main__":
    main_game()