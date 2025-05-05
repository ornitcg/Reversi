from constants import *

class Min_Max:
    def __init__(self, transition_model, state_space,  heuristic=None):
        self.state_space = state_space
        self.transition_model = transition_model
        self.heuristic = heuristic



    def min_max_tree(self, node, depth):
        if depth == 0:
            return self.heuristic.calculate(node, node.get_turn())
