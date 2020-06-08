import pygame
import time
from sudokuSolver import solve, is_valid

#To write on the game window
pygame.font.init()

class Board:

    #This is the puzzle board
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

    def __init__(self, num_rows, num_cols, width, height):
        self.rows = num_rows
        self.cols = num_cols
        self.width = width
        self.height = height
        self.ref = None
        self.selected = None



def main():
    window = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku Puzzle")
    start_time = time.time()
    run = True
    key = None
    board = Board(9, 9, 540, 540)

    while run:
        game_time = time.time() - start_time

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False


if __name__ == '__main__':
    main()
    pygame.quit()



