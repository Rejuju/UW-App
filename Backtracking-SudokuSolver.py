#Implement a Sudoku solver using backtracking.

#Example Board
grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

# Initialize empty sqaures as '.'

def print_grid():
    for line in grid:
        for square in line:
            if square == 0:
                print(".", end=" ")
            else:
                print(square, end=" ")
        print()

print_grid()

#Determine whether the number to be inserted is valid

def is_valid(num, row, col):
    #initialize a global variable to keep track of the grid
    global grid
    # Check if the number is already in the row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check if the number is already in the column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check if the number is already in the 3x3 box using the top left corner of the current 3 x 3 box
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[box_row_start + i][box_col_start + j] == num:
                return False


    return True

#Implement Backtracking 

def solve():
    #start by looking for an empty cell
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # If we find an empty cell
                for num in range(1, 10):  # Try numbers 1 to 9
                    if is_valid(num, row, col):  # Check if the number is valid
                        grid[row][col] = num  # Place the number
                        solve():  # Recursively try to solve the rest of the grid
                        grid[row][col] = 0  # Backtrack by resetting the last input which lead to an unsolvable grid to 0

                return #Return the grid, after all possible inputs have been tried
    print_grid()  # Print the grid 

