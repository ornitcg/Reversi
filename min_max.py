from constants import *

class Min_Max:
    def __init__(self, initial_state, state_space, max_depth = 1, heuristic=None):
        self.initial_state = initial_state
        self.state_space = state_space
        self.max_depth = max_depth  # Set a maximum depth for the search
        self.heuristic = heuristic



    def play(self):
        # Start the Min-Max algorithm
        self.minmax(self.initial_state, self.max_depth, MAX)


    def minmax(self, state, depth, current_player):
        current_board = state.get_board()
        game_over = self.state_space.is_terminal_state(current_board, current_player)
        if game_over:
            return self.state_space.utility(current_board)

        turn = self.state_space.get_next_player(current_player)
        children = self.state_space.transition_model.expand_node(state)