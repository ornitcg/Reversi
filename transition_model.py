from constants import *
from node import *
import copy


class Transition_Model:
    def __init__(self):
        pass

    def result(self, new_board, action):

        action.execute(new_board)
        return new_board



    def get_next_player(self, current_player):
        """
        Returns the next player to move

        Parameters:
        - current_player: Current player (MAX or MIN)

        Returns:
        - Next player (MAX or MIN)
        """
        return MIN if current_player == MAX else MAX

    def is_terminal(self, board, current_player):
        """
        Check if the game state is terminal (game over)

        Parameters:
        - board: Current game board
        - current_player: Current player (MAX or MIN)

        Returns:
        - True if terminal state, False otherwise
        """
        # Count empty cells
        empty_cells = sum(row.count(EMPTY) for row in board)

        # If no empty cells, game is over
        if empty_cells == 0:
            return True

        # Check if current player has legal moves
        has_current_player_moves = self.__has_legal_moves(board, current_player)
        if not has_current_player_moves:
            # Check if opponent has legal moves
            opponent = MIN if current_player == MAX else MAX
            has_opponent_moves = self.__has_legal_moves(board, opponent)
            # If neither player has moves, game is over
            return not has_opponent_moves

        return False

    def __has_legal_moves(self, board, player):
        """
        Check if a player has any legal moves

        Parameters:
        - board: Current game board
        - player: Player to check for legal moves

        Returns:
        - True if player has at least one legal move, False otherwise
        """
        from action import Action

        board_size = len(board)
        for x in range(board_size):
            for y in range(board_size):
                if board[x][y] == EMPTY:
                    action = Action(copy.deepcopy(board), player, x, y)
                    if action.is_legal():
                        return True
        return False

    def utility(self, board):
        """
        Calculate the utility of the terminal state
        - Positive: MAX (TURN_RED) wins
        - Negative: MIN (TURN_WHITE) wins
        - 0: Draw

        Parameters:
        - board: Current game board

        Returns:
        - Utility value
        """
        # Count pieces
        max_pieces = sum(row.count(MAX) for row in board)
        min_pieces = sum(row.count(MIN) for row in board)

        if max_pieces > min_pieces:
            return 1  # MAX wins
        elif min_pieces > max_pieces:
            return -1  # MIN wins
        else:
            return 0  # Draw

    def count_pieces(self, board):
        """
        Count the number of pieces for each player

        Parameters:
        - board: Current game board

        Returns:
        - (max_pieces, min_pieces): Tuple with piece counts
        """
        max_pieces = sum(row.count(MAX) for row in board)
        min_pieces = sum(row.count(MIN) for row in board)
        return max_pieces, min_pieces