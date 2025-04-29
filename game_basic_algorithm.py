from action import *
from constants import *
from state_space import *
from transition_model import *
from node import *
from game_board import *
import time

class Game_Basic_Algorithm:
    def __init__(self, state_space, start_node):
        self.state_space = state_space
        self.initial_state = start_node.get_board()
        self.turn = start_node.get_turn()


    def play(self, current_node = None, turn = None):
        game_board = Game_Board()
        game_board.initialize_GUI()

        if current_node is None:
            current_node = self.initial_state
        board = current_node.get_board()
        if turn is None:
            turn = current_node.get_turn()

        skipped_turns = 0  # count of skipped turns. if both players skip, no legal moves exist for anyone and game is over
        while skipped_turns < 2 :

            game_board.display_GUI_board(current_node.get_board())
            game_board.display_textual_board(current_node.get_board())
            time.sleep(1)  # Delay for 1 second

            if self.state_space.is_goal_state(current_node):
                print("Game Over")
                break
            legal_moves = self.state_space.get_legal_actions(current_node, current_node.get_turn())
            if not legal_moves:
                skipped_turns += 1
                turn = self.state_space.__transition_model.get_next_player()
                continue
            
            else:
                skipped_turns = 0
                action = legal_moves[0]  #for now, just pick the first legal move
                successor_node = self.state_space.get_successor(current_node, action)
                current_node = successor_node



