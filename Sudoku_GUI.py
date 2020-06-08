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

# Class for each small cube
class Cube:

    def __init__(self, value, row, col, width ,height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width #of the board
        self.height = height #of the board
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        cube_width_height = self.width / 9
        x = self.col * cube_width_height #cooordinates of the cube
        y = self.row * cube_width_height #coordinates of the cube

        #temporary value with a pencil
        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128,128,128))
            win.blit(text, (x+5, y+5))

        #if the value is final, we freeze it with solid font, aligned in the center
        elif not(self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            #align the cube correctly
            win.blit(text, (x + (cube_width_height/2 - text.get_width()/2), y + (cube_width_height/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(win, (255,0,0), (x,y, cube_width_height ,cube_width_height), 3)

    def set_temp(self, num):
        self.temp = num
        
    def set(self, num):
        self.value = num



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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.del()
                    key = None
                if event.key == pygame.K_RETURN:
                    i,j = board.selected
                    if board[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                        key = None

                        if board.is_finished():
                            print("Game over")
                            run = False



if __name__ == '__main__':
    main()
    pygame.quit()



