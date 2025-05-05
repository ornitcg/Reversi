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
        board = node.get_board()
        perspective_color = perspective_player.get_color()
        opponent_color = WHITE if perspective_color == RED else RED

        # Count the number of pieces for each color
        perspective_color_count = node.get_color_count(perspective_color)
        opponent_color_count = node.get_color_count(opponent_color)

        # Mobility score - number of legal moves
        mobility_score = self.calculate_mobility_delta(node, perspective_player)

        # Position score - weighted value of positions
        position_score = self.calculate_position_value_delta(board, perspective_color)

        # Piece difference score
        piece_diff = perspective_color_count - opponent_color_count

        # Combine the scores with appropriate weights
        count = node.get_total_count()
        board_size = SIDE_SIZE *SIDE_SIZE

        if (count < board_size * (1/3) ):
            w_piece = 0.1
            w_mobility = 0.5
            w_position = 0.4

        elif (count < board_size *(2/3) ):
            w_piece = 0.2
            w_mobility = 0.2
            w_position = 0.6
        else:
            w_piece = 0.7
            w_mobility = 0.1
            w_position = 0.2

        position_factor = 0.01
        adjusted_position_score = position_score * position_factor

        total_score = (piece_diff * w_piece) + (mobility_score * w_mobility) + (adjusted_position_score * w_position)

        return total_score

    def calculate_mobility_delta(self, node, perspective_player):

        # Calculate delta of mobility between both players in the current position
        opponent_player = self.transition_model.get_next_player(perspective_player)

        # Create artificial test nodes for each player
        perspective_node = copy.deepcopy(node)
        perspective_node.set_turn(perspective_player)

        opponent_node = copy.deepcopy(node)
        opponent_node.set_turn(opponent_player)

        # Count legal moves for each player in the CURRENT position
        perspective_legal_moves = len(self.transition_model.get_legal_moves(perspective_node))
        opponent_legal_moves = len(self.transition_model.get_legal_moves(opponent_node))

        # The mobility advantage is the difference in available moves
        return perspective_legal_moves - opponent_legal_moves


    def calculate_position_value_delta(self, board, perspective_color):
        #Calculate the delta of pieces based on their positions
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

    def get_transition_model(self):
        return self.transition_model