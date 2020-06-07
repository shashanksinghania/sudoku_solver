board = [
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


# this function prints the board
def print_board(bd):
    for i in range(len(bd)):
        if i % 3 == 0 and not i == 0:
            print('-----------------------------')
        for j in range(len(bd[0])):
            if j % 3 == 0 and not j == 0:
                print('| ', end="")
            if j == 8:
                print(bd[i][j], " ")
            else:
                print(bd[i][j], " ", end="")


# this function finds the next empty spot and returns the index as a tuple
def get_empty_spots(bd):
    for i in range(len(bd)):
        for j in range(len(bd[0])):
            if bd[i][j] == 0:
                return (i, j)
    return None


# this function checks if a number is valid at that a given position
def is_valid(bd, number: int, position: tuple):
    # Checking if the row is valid
    for i in range(len(bd)):
        if position[1] != i and bd[position[0]][i] == number:
            return False

    # Checking if column is valid
    for i in range(len(bd)):
        if position[0] != i and bd[i][position[1]] == number:
            return False

    # Check the square
    for i in range(-2, 3):
        if position[0] // 3 == (position[0] + i) // 3:
            for j in range(0, 3):
                if i == 0 and j == 0:
                    continue
                if position[1] // 3 == (position[1] + j) // 3 and bd[position[0] + i][position[1] + j] == number:
                    return False
                if position[1] // 3 == (position[1] - j) // 3 and bd[position[0] + i][position[1] - j] == number:
                    return False
    return True


# Sudoku solver with backtracking algorithm
def solve(bd):
    empty_spot = get_empty_spots(bd)
    if not empty_spot:
        return True
    x, y = empty_spot
    for i in range(1, 10):
        if is_valid(bd, i, (x, y)):
            bd[x][y] = i
            if solve(bd):
                return True
            else:
                bd[x][y] = 0
    return False

if __name__ == "__main__":
    solve(board)
    print_board(board)