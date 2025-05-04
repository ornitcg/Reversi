from constants import *
from action import Action
from node import *
import copy
from transition_model import *


class State_Space:
    def __init__(self, transition_model, board_side_size=SIDE_SIZE ):
        self.transition_model = transition_model
        self.players = self.transition_model.get_players()
        self.initial_state = None
        self.set_initial_state(board_side_size, self.players[0]) # RED is always first




    def set_initial_state(self, size, starting_player):
        board = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(EMPTY)
            board.append(row)

        board[MIDDLE-1][MIDDLE-1] = RED
        board[MIDDLE-1][MIDDLE] = WHITE
        board[MIDDLE][MIDDLE-1] = WHITE
        board[MIDDLE][MIDDLE] = RED
        self.initial_state = Node(board, turn=starting_player, value= 0)


    def get_initial_state(self):
        return self.initial_state


    def is_goal_state(self, node):
        board = node.get_board()
        current_player = node.get_turn()
        # check if any empty cells are left
        empty_cells = sum(row.count(EMPTY) for row in board)
        if empty_cells == 0:
            return True

        # check if current player has legal moves, and if opponent has no legal moves
        has_current_player_moves = self.transition_model.get_legal_moves(node)
        if not has_current_player_moves:
            opponent = self.transition_model.get_next_player(current_player)
            node_as_opponent = Node(board, turn=opponent, value=0)
            has_opponent_moves = self.transition_model.get_legal_moves(node_as_opponent)
            return not has_opponent_moves

    def get_successor(self, node, action):
        return self.transition_model.apply_action(node, action)

    def get_successors(self, node, legal_moves):
        successors = []
        board = node.get_board()
        current_player = node.get_turn()
        # legal_moves = self.transition_model.get_legal_moves(node)
        for action in legal_moves:
            successors.append(self.get_successor(node, action))
        return successors



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