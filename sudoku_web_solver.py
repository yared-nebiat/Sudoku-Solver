from bs4 import BeautifulSoup
import requests



def print_puzzle(board):
	for row in range(len(board)):
		if row != 0:
			# Checks if it is on rows 3 or 6
			if row % 3 == 0:
				print("\n------------------------", end="")
			print("")

		for col in range(len(board[0])):
			# Checks if it is on columns 3 or 6
			if col % 3 == 0 and col != 0:
				print(" | ", end="")

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
			# Or? when ...?
			if solve(board):
				return True
			# sets the value to be empty again
			# the for loop causes is to try the next value in the preceding cell
			board[row][col] = 0


def main():
	url = input("Enter link for puzzle: ")

	if url == 'q':
		exit()

	result = requests.get(url)  # returns the html of the url page

	# print(result.text) # prints the html code for the page

	doc = BeautifulSoup(result.text, "html.parser")

	grid = doc.find_all("table")[2]

	cells = grid.find_all("td", class_="sudoku-box")

	puzzle = [[],[],[],[],[],[],[],[],[]]

	count = 1
	index = 0

	for each in cells:
		if each.find("div", class_="box readonly"):
			puzzle[index].append(int(each.div.string.strip()))

		elif each.find("div", class_="box"):
			puzzle[index].append(0)

		if count % 9 == 0:
			index += 1
		count += 1

	solve(puzzle)
	print_puzzle(puzzle)
	print("\n")
	main()


if __name__ == '__main__':
	main()
