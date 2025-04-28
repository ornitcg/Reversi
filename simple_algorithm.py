from action import *
from constants import *
from state_space import *
from transition_model import *
from node import *

class Simple_Algorithm:
    def __init__(self, state_space, start_node):
        self.state_space = state_space
        self.initial_state = start_node.get_board()
        self.turn = start_node.get_type()


    def play(self, from_state = None, turn = None):
        if from_state is None:
            from_state = self.initial_state
        board = from_state.get_board()
        if turn is None:
            turn = from_state.get_type()

        skipped_turns = 0  # count of skipped turns. if both players skip, no legal moves exist for anyone and game is over
        while skipped_turns < 2 :
            legal_moves = self.state_space.get_legal_actions(board, turn)
            if not legal_moves:
                skipped_turns += 1
                turn = self.state_space.transition_model.get_next_player()







