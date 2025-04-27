from constants import *
from action import Action
from node import *

class State_Space:
    def __init__(self,  transition_model=None, board_side_size=SIDE_SIZE):
        self.initial_state = self.set_initistial_state(board_side_size)
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

    def set_initistial_state(self, size):
        board = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(EMPTY)
            board.append(row)

        board[MIDDLE-1][MIDDLE-1] = TURN_RED
        board[MIDDLE-1][MIDDLE] = TURN_WHITE
        board[MIDDLE][MIDDLE-1] = TURN_WHITE
        board[MIDDLE][MIDDLE] = TURN_RED

        return Node(board, MAX)