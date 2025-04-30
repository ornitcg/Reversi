from action import *
from constants import *
from state_space import *
from transition_model import *
from node import *
from game_board import *
import time

class Game_Engine:
    def __init__(self,  players , start_node = None):
        self.transition_model = Transition_Model(players)
        self.state_space = State_Space(players, self.transition_model)
        self.player_red = players[0]
        self.player_white = players[1]
        if start_node:
            self.initial_state = start_node
        else:
            self.initial_state = self.state_space.get_initial_state()

    def play(self, max_disks=None):
        game_board = Game_Board()
        game_board.initialize_GUI()

        current_node = self.initial_state
        current_player = current_node.get_turn()

        skipped_turns = 0  # count of skipped turns. if both players skip, no legal moves exist for anyone and game is over
        while skipped_turns < 2 :

            game_board.display_graphic_board(current_node.get_board())
            game_board.display_textual_board(current_node.get_board())
            time.sleep(0.5)  # Delay for 1 second

            legal_moves = self.transition_model.get_legal_moves(current_node)
            board_with_legal = self.transition_model.mark_legal_actions(current_node, legal_moves)
            game_board.display_graphic_board(board_with_legal, current_player)
            game_board.display_textual_board(board_with_legal)
            time.sleep(0.5)  # Delay for 1 second

            if current_node.get_total_count() == max_disks:
                time.sleep(5)
                break


            if self.state_space.is_goal_state(current_node):
                print("Game Over")
                break
            legal_moves = self.transition_model.get_legal_moves(current_node)
            if not legal_moves:
                skipped_turns += 1
                action = Action(SKIP)

            else:
                skipped_turns = 0
                action = current_player.choose_action(current_node, legal_moves)

            successor_node = self.transition_model.apply_action(current_node, action)
            current_node = successor_node
            current_player = successor_node.get_turn()



