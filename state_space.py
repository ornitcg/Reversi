from constants import *
from action import Action


class State_Space:
    def __init__(self, game_board, transition_model=None):
        self.initial_state = game_board
        self.transition_model = transition_model


    def get_initial_state(self):
        return self.initial_state

    def get_legal_actions(self, board, turn):
        legal_actions = []  #list of action objects
        board_size = len(board)

        # Check each empty cell for a legal move
        for row in range(board_size):
            for col in range(board_size):
                if board[row][col] == EMPTY:
                    action = Action(board, turn, row, col)
                    if action.is_legal():
                        legal_actions.append(action)

        return legal_actions