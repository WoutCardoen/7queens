# 7 Queens

A Python program that places 7 queens on an 8×8 chessboard so that no two queens attack each other: no two share a row, a column or a diagonal.

## How it works

The board is a list of 8 rows, where each square is one of:

- `.`: free square
- `X`: a queen
- `O`: a square attacked by a queen

The program uses **backtracking**:

1. It scans the board row by row for the first free square (`.`) that hasn't been tried yet for the current queen.
2. It places a queen there and marks every square it attacks (its row, column and both diagonals) with `O`.
3. If no free square is left for the next queen, it **backtracks**: it removes the last queen, rebuilds the board from the remaining queens, and tries that queen on its next untried square.
4. This repeats until 7 queens are on the board, or until every option for the first queen is exhausted ("No solution").

For each queen, the program keeps a list of positions it has already tried, so it never tries the same position twice. When a queen moves to a new position, the lists of all later queens are cleared, because they now have a new board to work with.

## Run it

No external packages are needed.

```
python 7queens.py
```

The final board is printed row by row.