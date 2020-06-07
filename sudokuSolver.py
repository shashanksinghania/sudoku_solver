board = [
    [9, 1, 5, 5, 7, 3, 8, 2, 6],
    [5, 1, 2, 2, 8, 6, 1, 7, 9],
    [4, 1, 3, 6, 2, 5, 8, 6, 7],
    [7, 1, 8, 2, 9, 3, 4, 5, 6],
    [9, 7, 1, 3, 2, 6, 5, 8, 4],
    [5, 3, 1, 7, 4, 2, 9, 8, 6],
    [1, 8, 6, 5, 3, 9, 2, 4, 7],
    [7, 1, 5, 9, 2, 4, 6, 8, 3],
    [1, 3, 7, 5, 8, 4, 2, 9, 6]
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
