from constants import *
from action import Action
from node import *
import copy


class Transition_Model:

    def is_legal(self, node, action):
        to_flip_list = self.check_all_directions(node, action)
        if len(to_flip_list) > 0:
           return True
        return False

    def apply_action(self, node , action):
        board = copy.deepcopy(node.get_board())
        y,x  = action.get_position()
        turn = action.get_turn()
        board[y][x] = turn    # place the new piece
        pieces_to_flip = self.check_all_directions(node, action)
        self.__flip(board,turn, pieces_to_flip)
        value = len(pieces_to_flip) + 1  # +1 for the new piece
        successor = Node(board, node, action, self.get_next_player(turn), value)  #parent is the current node, action is the action taken to get to this state, and turn is the next player
        return  successor

    def skip_turn(self, node):
        turn = node.get_turn()
        new_board = copy.deepcopy(node.get_board())
        successor = Node(new_board, node, None, self.get_next_player(turn), 0)
        return successor

    def check_all_directions(self, node, action):
        pieces_to_flip = []
        directions = [(LEFT,STAY),
                      (RIGHT,STAY),
                      (STAY,UP),
                      (STAY,DOWN),
                      (RIGHT,UP),
                      (LEFT,DOWN),
                      (LEFT,UP),
                      (RIGHT,DOWN)]

        for direction in directions:
            horizontal_direction = direction[0]
            vertical_direction = direction[1]
            pieces_to_flip.extend(self.check_a_direction(node, action, horizontal_direction, vertical_direction))
        return pieces_to_flip





    def check_a_direction(self, node, action, horizontal_direction, vertical_direction):
        row, col = action.get_position()
        turn = node.get_turn()
        board = node.get_board()
        opponent = MIN if turn == MAX else MAX
        pieces_to_flip = []
        sandwich = False
        row += vertical_direction
        col += horizontal_direction
        while row >= 0 and col >= 0 and row < SIDE_SIZE and col < SIDE_SIZE:
            if board[row][col] == EMPTY:
                break
            if board[row][col] == opponent:
                pieces_to_flip.append((row, col))
            if board[row][col] == turn:
                if len(pieces_to_flip) > 0:
                    sandwich = True
                else:
                    break
            row += vertical_direction
            col += horizontal_direction

        if sandwich:
            return pieces_to_flip
        else:
            return []



    def __flip(self, board, turn, pieces_to_flip):
        for i in pieces_to_flip:
            board[i[0]][i[1]] = turn






    def expand_node(self, node):
        board = node.get_board()
        current_player = node.get_type()
        legal_moves = self.get_legal_moves(board, current_player)
        children = []
        for action, score in legal_moves:
            new_board = copy.deepcopy(board)
            new_board = self.get_neighbor(new_board, action)
            child_node = Node(new_board, node, action, self.get_next_player(current_player))
            children.append(child_node)
        return children


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
                        score = action.get_score(board)
                        legal_moves.append((action,score))  #tuple of action and score
        return legal_moves






