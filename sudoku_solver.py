
# Empty spots denoted by 0

board = [
		[0,0,4,9,0,0,0,6,1],
		[2,0,6,0,0,0,0,0,0],
		[1,0,0,3,6,0,0,2,0],
		[0,3,7,0,0,0,0,0,4],
		[0,0,0,1,0,0,6,0,0],
		[0,0,0,0,4,0,3,0,5],
		[7,4,0,0,3,0,0,0,0],
		[0,0,0,0,1,5,0,0,9],
		[0,0,0,0,0,2,0,4,0],
	]


def print_puzzle(board):
	for row in range(len(board)):
		if row != 0:
			# Checks if it is on rows 3 or 6
			if row % 3 == 0:
				print("\n--------------------------", end="")
			print("")

		for col in range(len(board[0])):
			# Checks if it is on columns 3 or 6
			if col % 3 == 0 and col != 0:
				print(" | ", end=" ")

			print(board[row][col], end=" ")

# finds the next empty cell on the board
def find_empty(board):
	for row in range(len(board)):
		for col in range(len(board[0])):
			if board[row][col] == 0:
				return (row,col)
	return None

# Checks if the number provided is a valid number for the specified cell on the board
def is_valid(board, num, row, col):
	# Checks if the given value is found in the same row
	for i in range(len(board[0])):
		if board[row][i] == num:
			return False
	# Checks if the given value is found in the same column
	for j in range(len(board)):
		if board[j][col] == num:
			return False
	# identifies which position the block starts at
	row_start = (row // 3) * 3
	col_start = (col // 3) * 3
	# Checks if the given value is found in the same block
	for i in range(row_start, row_start + 3):
		for j in range(col_start, col_start + 3):
			if board[i][j] == num:
				return False

	return True


def solve(board):
	# Checks if the board has no spots left.
	# If so, the board has been solved.
	if not find_empty(board):
		return True

	row, col = find_empty(board)


	for num in range(1,10):
		if is_valid(board, num, row, col):
			board[row][col] = num
			# Checks if it is possible to solve the puzzle
			# It would be impossible when the loop is finished and 
			# there is no valid number for the cell
			if solve(board):
				return True
			# sets the value to be empty again
			# the for loop causes it to try the next value in the preceding cell
			board[row][col] = 0


print_puzzle(board)
print("\n")

solve(board)
print_puzzle(board)

input() # to view the output before the program terminates