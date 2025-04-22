from constants import *


class Action:
    def __init__(self, board, turn, x , y ):
        self.turn = turn
        self.board = board
        self.x = x
        self.y = y

    def execute(self):
        self.add()
        self.flip()


    def add(self):
        self.board[self.x][self.y] = self.turn

    def flip(self):
        self.__flip_horizontal(LEFT)
        self.__flip_horizontal(RIGHT)
        self.__flip_vertical(UP)
        self.__flip_vertical(DOWN)
        self.__flip_diagonal_main()
        self.__flip_diagonal_secondary()


    def __flip_horizontal(self, direction):
        row = self.x
        col = self.y
        to_flip = []
        while col > 0 and col < SIDE_SIZE:
            col += direction
            if self.board[row][col] == self.turn:
                break
            elif self.board[row][col] == EMPTY:
                break
            else:
                to_flip.append(col)
        for i in to_flip:
            self.board[row][i] = self.turn


    def __flip_vertical(self, direction):
        row = self.x
        col = self.y
        to_flip = []
        while row > 0 and row < SIDE_SIZE:
            row += direction
            if self.board[row][col] == self.turn:
                break
            elif self.board[row][col] == EMPTY:
                break
            else:
                to_flip.append(row)
        for i in to_flip:
            self.board[i][col] = self.turn
