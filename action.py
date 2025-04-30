from constants import *


class Action:
    def __init__(self,  type, x = None , y = None ):
        self.type = type
        self.x = x  # x is the column
        self.y = y  # y is the row



    def get_type(self): #(ADD or SKIP)
        return self.type

    def get_position(self):
        return self.y, self.x






