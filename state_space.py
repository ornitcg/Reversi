class State_Space:
    def __init__(self, game_board):
        self.initial_state = game_board


    def get_initial_state(self):
        return self.initial_state

    def get_legal_actions(self, board, turn):
        pass