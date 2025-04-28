from constants import *


class Action:
    def __init__(self,  turn, x , y ):
        self.turn = turn
        self.x = x  # x is the column
        self.y = y  # y is the row



    def get_position(self):
        return self.y, self.x


    def get_turn(self):
        return self.turn



