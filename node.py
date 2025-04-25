


class Node:
    def __init__(self, game_board, parent=None, action=None):
        self.game_board = game_board  # Current game state
        self.parent = parent  # Parent node
        self.action = action  # Action that led to this state
        self.children = []  # Child nodes
        self.value = None  # For minimax evaluation

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