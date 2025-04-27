from constants import *
from action import Action
from node import *
import copy


class Transition_Model:
    def __init__(self):
        pass

    def get_neighbor(self, new_board, action):
        action.apply(new_board)
        return new_board


    def get_next_player(self, current_player):
        return MIN if current_player == MAX else MAX


    def is_terminal_state(self, board, current_player):
        # check is any empty cells are left
        empty_cells = sum(row.count(EMPTY) for row in board)
        if empty_cells == 0:
            return True

        # check if current player has legal moves, and if opponent has no legal moves
        has_current_player_moves = self.get_legal_moves(board, current_player)
        if not has_current_player_moves:
            opponent = MIN if current_player == MAX else MAX
            has_opponent_moves = self.get_legal_moves(board, opponent)
            return not has_opponent_moves  #game over if opponent has no moves

        return False



    # creates list of optional moves for a given player
    def get_legal_moves(self, board, player):
        legal_moves = []
        board_size = len(board)
        for x in range(board_size):
            for y in range(board_size):
                if board[x][y] == EMPTY:
                    action = Action( player, x, y)
                    if action.is_legal(board):
                        legal_moves.append(action)
        return legal_moves



    # compares counts of both players and returns the winner
    def utility(self, board):
        max_pieces , min_pieces = self.count_pieces(board)
        if max_pieces > min_pieces:
            return MAX
        elif min_pieces > max_pieces:
            return MIN
        else:
            return TIE


    # checks counts for each player
    def count_pieces(self, board):
        max_pieces = sum(row.count(MAX) for row in board)
        min_pieces = sum(row.count(MIN) for row in board)
        return max_pieces, min_pieces