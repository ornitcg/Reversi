from constants import *
from action import *
from player import *
from node import *
import copy
from transition_model import Transition_Model


class Heuristic:
    def __init__(self, transition_model):
        # weights for different board positions
        self.position_weights = [
            [100, -20, 10, 5, 5, 10, -20, 100],
            [-20, -50, -2, -2, -2, -2, -50, -20],
            [10, -2, 1, 1, 1, 1, -2, 10],
            [5, -2, 1, 1, 1, 1, -2, 5],
            [5, -2, 1, 1, 1, 1, -2, 5],
            [10, -2, 1, 1, 1, 1, -2, 10],
            [-20, -50, -2, -2, -2, -2, -50, -20],
            [100, -20, 10, 5, 5, 10, -20, 100]
        ]
        self.transition_model = transition_model

    def calculate(self, node, perspective_player):
        """
        Calculate a heuristic value for the given node.
        and from a specific perspective color
        """

        board = node.get_board()
        perspective_color = perspective_player.get_color()
        opponent_color = WHITE if perspective_color == RED else RED

        # Count the number of pieces for each color
        perspective_color_count = node.get_color_count(perspective_color)
        opponent_color_count = node.get_color_count(opponent_color)

        # Mobility score - number of legal moves
        mobility_score = self.calculate_mobility_delta(node, perspective_player)

        # Position score - weighted value of positions
        position_score = self.calculate_position_value(board, perspective_color)

        # Piece difference score
        piece_diff = perspective_color_count - opponent_color_count

        # Combine the scores with appropriate weights
        # Adjust these weights based on testing
        total_score = (piece_diff * 1.0) + (mobility_score * 2.0) + (position_score * 3.0)
        return total_score

    def calculate_mobility_delta(self, node, perspective_player):
        """
        Calculate delta of mobility between both players in the current position
        """
        board = node.get_board()
        opponent_player = self.transition_model.get_next_player(perspective_player)

        # Create test nodes for each player
        perspective_node = copy.deepcopy(node)
        perspective_node.turn = perspective_player

        opponent_node = copy.deepcopy(node)
        opponent_node.turn = opponent_player

        # Count legal moves for each player in the CURRENT position
        perspective_legal_moves = len(self.transition_model.get_legal_moves(perspective_node))
        opponent_legal_moves = len(self.transition_model.get_legal_moves(opponent_node))

        # The mobility advantage is the difference in available moves
        return perspective_legal_moves - opponent_legal_moves


    def calculate_position_value(self, board, perspective_color):
        """Calculate the value of pieces based on their positions"""
        opponent_color = WHITE if perspective_color == RED else RED
        perspective_color_value = 0
        opponent_color_value = 0

        for row in range(SIDE_SIZE):
            for col in range(SIDE_SIZE):
                cell = board[row][col]
                position_weight = self.position_weights[row][col]

                if cell == perspective_color:
                    perspective_color_value += position_weight
                elif cell == opponent_color:
                    opponent_color_value += position_weight

        return perspective_color_value - opponent_color_value