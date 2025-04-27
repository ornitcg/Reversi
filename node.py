


class Node:
    def __init__(self, board, parent=None, action=None):

        self.board = board
        self.parent = parent
        self.action = action  # That led to this state
        self.children = []  # list of  nodes
        self.value = None  # For minimax evaluation
        self.type = None  # MAX or MIN

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