from constants import *


class Action:
    def __init__(self, board, turn, x , y ):
        self.turn = turn
        self.board = board
        self.x = x-1
        self.y = y-1
        self.score = 0
        self.__pieces_to_flip = []
        self.__check_all_directions()
        self.__is_legal = len(self.__pieces_to_flip) > 0


    def execute(self):
        self.__add()
        self.__flip()

    # add a new piece to the board on x,y
    def __add(self):
        self.board[self.x][self.y] = self.turn

    def __check_all_directions(self):
        directions = [(LEFT,STAY),
                      (RIGHT,STAY),
                      (STAY,UP),
                      (STAY,DOWN),
                      (RIGHT,UP),
                      (LEFT,DOWN),
                      (LEFT,UP),
                      (RIGHT,DOWN)]

        for direction in directions:
            horizontal_direction = direction[0]
            vertical_direction = direction[1]
            self.__check_direction(horizontal_direction, vertical_direction)




    def __check_direction(self, horizontal_direction, vertical_direction):
        row = self.x
        col = self.y
        while row >= 0 and col >= 0 and row < SIDE_SIZE and col < SIDE_SIZE:
            row += vertical_direction
            col += horizontal_direction
            if self.board[row][col] == self.turn:
                break
            elif self.board[row][col] == EMPTY:
                break
            else:
                self.__pieces_to_flip.append((row, col))


    def __flip(self):
        for i in self.__pieces_to_flip:
            self.board[i[0]][i[1]] = self.turn




    def is_legal(self):
        return self.__is_legal


    def get_score(self):
        return self.score

    def get_pieces_to_flip(self):
        return self.__pieces_to_flip

    def get_position(self):
        return self.x, self.y

    def get_turn(self):
        return self.turn

    def get_board(self):
        return self.board


