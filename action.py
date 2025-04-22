from constants import *


class Action:
    def __init__(self, board, turn, x , y ):
        self.turn = turn
        self.board = board
        self.x = x
        self.y = y

    def execute(self):
        self.__add()
        self.__flip()


    def __add(self):
        self.board[self.x][self.y] = self.turn

    def __flip(self):
        self.__flip_horizontal(LEFT)
        self.__flip_horizontal(RIGHT)
        self.__flip_vertical(UP)
        self.__flip_vertical(DOWN)
        self.__flip_diagonal(RIGHT, UP)   #main diagonal
        self.__flip_diagonal(LEFT, DOWN)  #main diagonal
        self.__flip_diagonal(LEFT, UP)    #second diagonal
        self.__flip_diagonal(RIGHT, DOWN)  #second diagonal


    def __flip_horizontal(self, direction):
        self.__flip(direction, STAY)


    def __flip_vertical(self, direction):
        self.__flip(STAY, direction)

    def __flip_diagonal(self, horizontal_direction ,vertical_direction):
        self.__flip(horizontal_direction, vertical_direction)


    def __flip(self, horizontal_direction ,vertical_direction):
        row = self.x
        col = self.y
        to_flip = []  #list of tuples
        while row > 0 and col > 0:
            row += vertical_direction
            col += horizontal_direction
            if self.board[row][col] == self.turn:
                break
            elif self.board[row][col] == EMPTY:
                break
            else:
                to_flip.append((row, col))
        for i in to_flip:
            self.board[i[0]][i[1]] = self.turn