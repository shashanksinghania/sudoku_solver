import pygame
import time
# from sudokuSolver import solve, is_valid, get_empty_spots

#To write on the game window
pygame.font.init()

#Methods from the text version to make it faster

# find the next empty spot in the sudoku
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

class Board:

    #This is the puzzle board
    board = [
        [8, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 3, 6, 8, 0, 0, 0, 5],
        [0, 7, 0, 0, 9, 0, 2, 8, 0],
        [0, 5, 0, 0, 0, 7, 0, 9, 0],
        [0, 0, 9, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 9, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 9, 1, 0],
        [7, 9, 0, 0, 0, 0, 4, 0, 0]
    ]

    def __init__(self, num_rows, num_cols, width, height, window):
        self.rows = num_rows
        self.cols = num_cols
        self.width = width
        self.height = height
        self.window = window
        self.ref_model = None
        self.selected = None
        self.cubes = [[Cube(self.board[i][j], i, j, width, height)
                       for j in range(self.cols)] for i in range(self.rows)]

    def revise_model(self):
        self.ref_model =  [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]


    def place(self, value):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(value)
            self.revise_model()

            if is_valid(self.ref_model, value, (row, col)) and solve(self.ref_model):
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.revise_model()
                return False

    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    def draw(self, window):

        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(window, (0, 0, 0), (0, int(i * gap)), (self.width, int(i * gap)), thick)
            pygame.draw.line(window, (0, 0, 0), (int(i * gap), 0), (int(i * gap), self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(window)

    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def remove(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    def click(self, pos):
        """
        :param: pos
        :return: (row, col)
        """
        if pos[0] < self.width and pos[1] < self.height:
            cube_width = self.width / 9
            x = pos[0] // cube_width
            y = pos[1] // cube_width
            return (int(y), int(x))
        else:
            return None

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True

    def solve_it_GUI(self):
        find = get_empty_spots(self.ref_model)
        if not find:
            return True
        row, col = find

        for i in range(1, 10):
            if is_valid(self.ref_model, i, (row, col)):
                self.ref_model[row][col] = i
                self.cubes[row][col].set(i)
                self.cubes[row][col].animation_show(self.window, True)
                self.revise_model()
                pygame.display.update()
                pygame.time.delay(15)

                if self.solve_it_GUI():
                    return True

                self.ref_model[row][col] = 0
                self.cubes[row][col].set(0)
                self.revise_model()
                self.cubes[row][col].animation_show(self.window, False)
                pygame.display.update()
                pygame.time.delay(15)

        return False


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

    def animation_show(self, window, g=True):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        pygame.draw.rect(window, (255, 255, 255), (x, y, gap, gap), 0)

        text = fnt.render(str(self.value), 1, (0, 0, 0))
        window.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))
        if g:
            pygame.draw.rect(window, (0, 255, 0), (x, y, gap, gap), 3)
        else:
            pygame.draw.rect(window, (255, 0, 0), (x, y, gap, gap), 3)

def update_window(window, board, time, incorrect):
    window.fill((255, 255, 255)) #white
    # Draw time
    fnt = pygame.font.SysFont("comicsans", 40)
    text = fnt.render("Time: " + show_time(time), 1, (0, 0, 0))
    window.blit(text, (540 - 175, 560))
    # Draw Strikes
    text = fnt.render("X " * incorrect, 1, (255, 0, 0))
    window.blit(text, (20, 560))
    # Draw grid and board
    board.draw(window)

def show_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    display = " " + str(minute) + " : " + str(sec)
    return display


def main():
    window = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku Puzzle")
    start_time = time.time()
    run = True
    key = None
    board = Board(9, 9, 540, 540, window)
    incorrect = 0

    while run:
        game_time = round(time.time() - start_time)

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
                    board.remove()
                    key = None
                if event.key == pygame.K_RETURN:
                    i,j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                            incorrect += 1
                        key = None

                        if board.is_finished():
                            print("Game over")
                            run = False
                if event.key == pygame.K_SPACE:
                    board.solve_it_GUI()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

            if board.selected and key != None:
                board.sketch(key)

            update_window(window, board, game_time, incorrect)
            pygame.display.update()



if __name__ == '__main__':
    main()
    pygame.quit()



