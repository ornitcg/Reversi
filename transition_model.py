from constants import *
from action import Action
from node import *
import copy


class Transition_Model:
    def __init__(self, players):
        self.players = players
        self.player1 = players[0]
        self.player2 = players[1]


    def apply_action(self, node , action):
        if action.get_type() == SKIP:
            return self.skip_turn(node)

        elif action.get_type() == ADD:
            board = copy.deepcopy(node.get_board())
            y,x  = action.get_position()
            current_player = node.get_turn()
            board[y][x] = current_player.get_color()    # place the new piece
            pieces_to_flip = self.check_all_directions(node, action)
            self.__flip(board, current_player , pieces_to_flip)
            value = len(pieces_to_flip) + 1  # +1 for the new piece
            successor = Node(board, node, action, self.get_next_player(current_player), value)  #parent is the current node, action is the action taken to get to this state, and turn is the next player
            return  successor

    def skip_turn(self, node):
        current_player = node.get_turn()
        new_board = copy.deepcopy(node.get_board())
        successor = Node(new_board, node, None, self.get_next_player(current_player), 0)
        return successor



    def is_legal(self, node, action):
        found_to_flip = self.check_all_directions(node, action)
        if found_to_flip:
           return True
        return False

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
        current_player = node.get_turn()
        current_player_color = current_player.get_color()
        board = node.get_board()
        pieces_to_flip = []
        sandwich = False
        row += vertical_direction
        col += horizontal_direction
        while row >= 0 and col >= 0 and row < SIDE_SIZE and col < SIDE_SIZE:
            if board[row][col] == EMPTY:
                break
            if board[row][col] is not current_player_color:
                pieces_to_flip.append((row, col))
            if board[row][col] == current_player_color:
                if len(pieces_to_flip) > 0:
                    sandwich = True
                break

            row += vertical_direction
            col += horizontal_direction

        if sandwich:
            return pieces_to_flip
        else:
            return []



    def __flip(self, board, current_player, pieces_to_flip):
        for i in pieces_to_flip:
            board[i[0]][i[1]] = current_player.get_color()






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
        return self.player1 if current_player == self.player2 else self.player2

    def skip_turn(self, node, player):
        current_player = node.get_turn()
        new_board = copy.deepcopy(node.get_board())
        successor = Node(new_board, node, None, self.get_next_player(current_player), 0)
        return successor

    def get_legal_moves(self, node):
        legal_actions = []  #list of action objects
        board = node.get_board()
        board_size = len(board)

        # Check each empty cell for a legal move
        for row in range(board_size):
            for col in range(board_size):
                if board[row][col] == EMPTY:
                    action = Action(ADD, col, row)
                    is_legal = self.is_legal(node, action)
                    if is_legal:
                        legal_actions.append(action)
        return legal_actions


    def get_score(self, node, action):
        # Calculate the score based on the number of pieces flipped
        pieces_to_flip = self.check_all_directions(node, action)
        return len(pieces_to_flip) + 1


    def mark_legal_actions(self, node, legal_moves):
        board = copy.deepcopy(node.get_board())
        for action in legal_moves:
            row, col = action.get_position()
            board[row][col] = LEGAL
        return board