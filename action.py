from constants import *


class Action:
    def __init__(self, board, turn, x , y ):
        self.turn = turn
        self.board = board
        self.x = x
        self.y = y
        self.to_flip = []
        self.__check_all_directions()
        self.is_legal = len(self.to_flip) > 0

    def execute(self):
        self.__add()
        self.__fill_to_flip()


    def __add(self):
        self.board[self.x][self.y] = self.turn

    def __check_all_directions(self):
        self.__check_horizontal(LEFT)
        self.__check_horizontal(RIGHT)
        self.__check_vertical(UP)
        self.__check_vertical(DOWN)
        self.__check_diagonal(RIGHT, UP)   #main diagonal
        self.__check_diagonal(LEFT, DOWN)  #main diagonal
        self.__check_diagonal(LEFT, UP)    #second diagonal
        self.__check_diagonal(RIGHT, DOWN)  #second diagonal


    def __check_horizontal(self, direction):
        self.__fill_to_flip(direction, STAY)


    def __check_vertical(self, direction):
        self.__fill_to_flip(STAY, direction)

    def __check_diagonal(self, horizontal_direction, vertical_direction):
        self.__fill_to_flip(horizontal_direction, vertical_direction)


    def __fill_to_flip(self, horizontal_direction, vertical_direction):
        row = self.x
        col = self.y
        while row > 0 and col > 0:
            row += vertical_direction
            col += horizontal_direction
            if self.board[row][col] == self.turn:
                break
            elif self.board[row][col] == EMPTY:
                break
            else:
                self.to_flip.append((row, col))


    def flip(self):
        for i in self.to_flip:
            self.board[i[0]][i[1]] = self.turn


