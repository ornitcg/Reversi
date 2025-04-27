from constants import *

class Min_Max:
    def __init__(self, initial_state, state_space, max_depth = 1, heuristic=None):
        self.initial_state = initial_state
        self.state_space = state_space
        self.max_depth = max_depth  # Set a maximum depth for the search
        self.heuristic = heuristic



    def play(self):
        # Start the Min-Max algorithm
        self.start(self.initial_state, self.max_depth, player=MAX)


    def start(self, state, depth, player):
        pass