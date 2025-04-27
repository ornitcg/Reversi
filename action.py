from constants import *


class Action:
    def __init__(self,  turn, x , y ):
        self.turn = turn
        self.x = x
        self.y = y


    def apply(self, board):
        self.add(board)
        pieces_to_flip = self.check_all_directions(board)
        self.flip(board, pieces_to_flip)

    # add a new piece to the board on x,y
    def add(self, board):
        board[self.x][self.y] = self.turn

    def check_all_directions(self, board):
        pieces_to_flip = []
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
            self.check_direction(board, pieces_to_flip, horizontal_direction, vertical_direction)
        return pieces_to_flip


    def check_direction(self,board, pieces_to_flip, horizontal_direction, vertical_direction):
        row = self.x
        col = self.y
        while row >= 0 and col >= 0 and row < SIDE_SIZE and col < SIDE_SIZE:
            row += vertical_direction
            col += horizontal_direction
            if board[row][col] == self.turn:
                break
            elif board[row][col] == EMPTY:
                break
            else:
                pieces_to_flip.append((row, col))


    def flip(self, board, pieces_to_flip):
        for i in pieces_to_flip:
            board[i[0]][i[1]] = self.turn


    def is_legal(self, board):
        to_flip_list = self.check_all_directions(board)
        if len(to_flip_list) > 0:
           return True
        return False

    def get_score(self, board):
        to_flip_list = self.check_all_directions(board)
        return len(to_flip_list) + 1  #+1 for the newly (to be) added piece

    def get_position(self):
        return self.x, self.y

    def get_turn(self):
        return self.turn



