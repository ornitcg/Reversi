from node import *
from constants import *



class Heuristic:
    def __init__(self, board_size=SIDE_SIZE):
        self.weights = {
            'corner': 1000,
            'edge': 100,
            'mobility': 10,
            'stability': 5,
            'parity': 1
        }
        self.corners = [(0, 0), (0, board_size-1), (board_size-1, 0), (board_size-1, board_size-1)]
        self.edges = [(0, i) for i in range(1, board_size-1)] + [(board_size-1, i) for i in range(1, board_size-1)] + [(i, 0) for i in range(1, board_size-1)] + [(i, board_size-1) for i in range(1, board_size-1)]


    def evaluate(self, node):
        player = node.get_turn()
        opponent = node.get_opponent()
