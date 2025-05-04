from constants import *


class Node:
    def __init__(self, board, parent=None, action=None, turn=None, value= None):
        self.board = board
        self.parent = parent
        self.action = action  # That led to this state
        self.children = []  # list of  nodes
        self.value = None  # For minimax evaluation
        self.turn = turn  # player Red or White # who should play an action on this node
        self.red_count = sum(row.count(RED) for row in board)
        self.white_count = sum(row.count(WHITE) for row in board)


    #getters
    def get_board(self):
        return self.board

    def get_parent(self):
        return self.parent

    def get_action(self):
        return self.action

    def get_children(self):
        return self.children

    def get_value(self):
        return self.value

    def get_turn(self):
        return self.turn

    def get_red_count(self):
        return self.red_count

    def get_color_count(self, color):
        if color == RED:
            return self.red_count
        elif color == WHITE:
            return self.white_count
        else:
            raise ValueError("Invalid color. Use RED or WHITE.")

    def get_white_count(self):
        return self.white_count

    def get_total_count(self):
        return self.red_count + self.white_count