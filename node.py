


class Node:
    def __init__(self, board, parent=None, action=None, type=None):

        self.board = board
        self.parent = parent
        self.action = action  # That led to this state
        self.children = []  # list of  nodes
        self.value = None  # For minimax evaluation
        self.type = type  # MAX or MIN
        self.red_count = 0
        self.white_count = 0


    def expand(self):
        """Generate all possible child nodes from current state"""
        valid_moves = self.game_board.get_valid_moves()

        for move in valid_moves:
            # Create a deep copy of the game board
            new_board = self.game_board.copy()

            # Execute the move
            row, col = move
            new_board.make_move(row, col)

            # Create child node
            child_node = Node(new_board, self, move)
            self.children.append(child_node)

        return self.children

    def is_terminal(self):
        """Check if this node is a terminal state"""
        return self.game_board.game_over




    #getters
    def get_board(self):
        return self.board

    def get_parent(self):
        return self.parent

    def get_action(self):
        return self.action

    def get_children(self):
        return self.children

    def get_value(self):
        return self.value

    def get_type(self):
        return self.type

    def get_red_count(self):
        return self.red_count

    def get_white_count(self):
        return self.white_count

    def get_total_count(self):
        return self.red_count + self.white_count