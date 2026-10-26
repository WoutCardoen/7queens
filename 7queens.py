def start_board():
    return [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."]
    ]

def fill_diagonal(board, row, column):
    for i in range(1, 8):
        if row + i < 8 and column + i < 8:
            board[row + i][column + i] = "O"
        if row - i >= 0 and column - i >= 0:
            board[row - i][column - i] = "O"
        if row + i < 8 and column - i >= 0:
            board[row + i][column - i] = "O"
        if row - i >= 0 and column + i < 8:
            board[row - i][column + i] = "O"

def place_queen(board, row, column):
    board[row] = ["O"] * 8
    for r in range(8):
        board[r][column] = "O"
    fill_diagonal(board, row, column)
    board[row][column] = "X"

def reset_board(board):
    for row in range(8):
        for column in range(8):
            board[row][column] = "."

def remove_last_queen(board, queens):
    if queens:
        last_row, last_column = queens.pop()
        reset_board(board)
        for row, column in queens:
            place_queen(board, row, column)
        return last_row, last_column


def __main__():
    board = start_board()
    amount = 0
    queens = []
    tried_positions = [[] for _ in range(7)]
    while amount < 7:
        placed = False
        for row in range(8):
            for column in range(8):
                if board[row][column] == "." and (row, column) not in tried_positions[amount]:
                    tried_positions[amount].append((row, column))
                    place_queen(board, row, column)
                    queens.append((row, column))
                    for i in range(amount + 1, 7):
                        tried_positions[i] = []
                    placed = True
                    amount += 1
                    break
            if placed:
                    break
        if not placed:
            if amount == 0:
                print("No solution")
                return
            tried_positions[amount] = []
            remove_last_queen(board, queens)
            amount -= 1
    for i in range(8):
        print(board[i])
__main__()