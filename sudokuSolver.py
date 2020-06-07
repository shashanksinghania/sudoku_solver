board = [
    [9, 1, 4, 5, 7, 3, 8, 2, 6],
    [5, 3, 2, 4, 8, 6, 1, 7, 9],
    [9, 1, 3, 4, 2, 5, 8, 6, 7],
    [7, 1, 8, 2, 9, 3, 4, 5, 6],
    [9, 7, 1, 3, 2, 6, 5, 8, 4],
    [5, 3, 1, 7, 4, 2, 9, 8, 6],
    [1, 8, 6, 5, 3, 9, 2, 4, 7],
    [7, 1, 5, 9, 2, 4, 6, 8, 3],
    [1, 3, 7, 5, 8, 4, 2, 9, 6]
]


def print_board(bd):
    for i in range(len(bd)):
        if i % 3 == 0 and not i == 0:
            print("-----------------------------")
        for j in range(len(bd[0])):
            if j % 3 == 0 and not j == 0:
                print('| ', end="")
            if j == 8:
                print(bd[i][j]," ")
            else:
                print(bd[i][j]," ", end="")


print_board(board)