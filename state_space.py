from constants import *
from action import Action
from node import *
import copy
from transition_model import *


class State_Space:
    def __init__(self,  transition_model=None, board_side_size=SIDE_SIZE):
        self.initial_state = self.set_initial_state(board_side_size)
        self.transition_model = transition_model

    def set_initial_state(self, size):
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

        return Node(board, MAX, value= 0)

        # compares counts of both players and returns the winner

    def get_initial_state(self):
        return self.initial_state

    def get_legal_actions(self, board, turn):
        legal_actions = []  #list of action objects
        board_size = len(board)

        # Check each empty cell for a legal move
        for row in range(board_size):
            for col in range(board_size):
                if board[row][col] == EMPTY:
                    action = Action(turn, col, row)
                    if self.transition_model.is_legal(board, action):
                        legal_actions.append(action)
        return legal_actions

    def is_goal_state(self, node):
        board = node.get_board()
        current_player = node.get_turn()
        # check if any empty cells are left
        empty_cells = sum(row.count(EMPTY) for row in board)
        if empty_cells == 0:
            return True

        # check if current player has legal moves, and if opponent has no legal moves
        has_current_player_moves = self.get_legal_actions(board, current_player)
        if not has_current_player_moves:
            opponent = MIN if current_player == MAX else MAX
            has_opponent_moves = self.get_legal_actions(board, opponent)
            return not has_opponent_moves

    def get_neighbor(self, node, action):
        return self.transition_model.apply_action(node, action)

    def get_neighbors(self, node):
        neighbors = []
        board = node.get_board()
        current_player = node.get_turn()
        legal_moves = self.get_legal_actions(board, current_player)
        for action in legal_moves:
            neighbors.append(self.get_neighbor(node, action))
        return neighbors



    def utility(self, board):
        max_pieces, min_pieces = self.__count_pieces(board)
        if max_pieces > min_pieces:
            return MAX
        elif min_pieces > max_pieces:
            return MIN
        else:
            return TIE

        # checks counts for each player

    def __count_pieces(self, board):
        max_pieces = sum(row.count(MAX) for row in board)
        min_pieces = sum(row.count(MIN) for row in board)
        return max_pieces, min_pieces




    #****************************************************************

    def check_for_legal_actions(self, board, turn):
        actions = []
        # Check corners first
        actions.extend(self.check_corners_for_legal_actions(board, turn))
        # Check edges next
        actions.extend(self.check_edges_for_legal_actions(board, turn))
        # Check inner cells last
        actions.extend(self.check_inner_cells_for_legal_actions(board, turn))
        return actions

    def check_corners_for_legal_actions(self, board, turn):
        actions = []
        corners = [(0, 0),
                   (0, len(board) - 1),
                   (len(board) - 1, 0),
                   (len(board) - 1, len(board) - 1)]
        for corner in corners:
            action = Action(turn, corner[0], corner[1])
            if action.is_legal(board):
                actions.append(action)
        return actions

    def check_edges_for_legal_actions(self, board, turn):
        actions = []
        for i in range(1, len(board) - 1):
            i_actions = [Action(turn, 0, i),  # left edge
                         Action(turn, len(board) - 1, i),  # right edge
                         Action(turn, i, 0),  # top edge
                         Action(turn, i, len(board) - 1)]  # bottom edge
            for action in i_actions:
                if action.is_legal(board):
                    actions.append(action)
        return actions

    def check_inner_cells_for_legal_actions(self, board, turn):
        actions = []
        for i in range(1, len(board) - 1):
            for j in range(1, len(board) - 1):
                action = Action(turn, i, j)
                if action.is_legal(board):
                    actions.append(action)
        return actions