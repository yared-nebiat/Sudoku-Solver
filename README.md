# Python Sudoku Solver
This repository contains a Python implementation of a sudoku solver. The solver takes a sudoku grid as input and returns a solution if one exists. The web solver takes this a step further by taking the link to the sudoku puzzle from the user and providing a solution after scraping the puzzle from the website. Puzzles from the following website are accepted (https://sudoku.puzzlebaron.com/)

## Requirements
Python 3.x

## Input format
The input is a 9x9 matrix representing the sudoku grid, where 0 represents an empty cell.

Example:
```
grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
```
## Output
The output is a 9x9 board representing the solution of the sudoku grid if one exists.

```
7 8 5  |  4 3 9  |  1 2 6
6 1 2  |  8 7 5  |  3 4 9
4 9 3  |  6 2 1  |  5 7 8
--------------------------
8 5 7  |  9 4 3  |  2 6 1
2 6 1  |  7 5 8  |  9 3 4
9 3 4  |  1 6 2  |  7 8 5
--------------------------
5 7 8  |  3 9 4  |  6 1 2
1 2 6  |  5 8 7  |  4 9 3
3 4 9  |  2 1 6  |  8 5 7
```

### Author

Yared Nebiat
