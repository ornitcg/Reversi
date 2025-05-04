from action import *
from constants import *
from state_space import *
from transition_model import *
from node import *
from game_output import *
import time



class Game_Engine:
    def __init__(self, transition_model, state_space,  start_node = None, heuristic = None):
        self.transition_model = transition_model
        self.heuristic = heuristic
        self.players = self.transition_model.get_players()
        self.state_space = state_space
        self.game_output = Game_Output(self.state_space)
        self.game_output.initialize_GUI()
        self.player_red = self.players[0]
        self.player_white = self.players[1]
        if start_node:
            self.initial_state = start_node
        else:
            self.initial_state = self.state_space.get_initial_state()

    def play(self,steps = None, max_disks=None, mode = None):

        current_node = self.initial_state
        current_player = current_node.get_turn()
        if mode == METHODICAL:
            self.game_output.display_methodical_title()

        skipped_turns = 0  # count of skipped turns. if both players skip, no legal moves exist for anyone and game is over
        while skipped_turns < 2 :
            if mode == METHODICAL:
                steps_count = current_node.get_total_count() - NUMBER_OF_INITIAL_DISKS
                if steps_count <= steps or self.state_space.is_goal_state(current_node):
                    self.game_output.methodical_output(current_node, steps_count)
            else:
                self.game_output.display_textual_board(current_node.get_board())
            self.game_output.display_graphic_board(current_node.get_board())  # UNCOMMENT THIS , TO SEE THE GAME PROCCESS
            legal_moves = self.transition_model.get_legal_moves(current_node)
            self.display_legal_moves( current_node, legal_moves)  # UNCOMMENT THIS , TO SEE THE GAME PROCCESS

            if mode == DISPLAY_ALL_ACTIONS:
                if current_node.get_total_count() == max_disks:
                    self.game_output.legal_moves_output(current_node, legal_moves)
                    break

            if self.state_space.is_goal_state(current_node):
                break
            legal_moves = self.transition_model.get_legal_moves(current_node)
            if not legal_moves:
                skipped_turns += 1
                action = Action(SKIP)

            else:
                skipped_turns = 0
                action = current_player.choose_action(current_node, legal_moves, self.heuristic)

            successor_node = self.transition_model.apply_action(current_node, action)
            current_node = successor_node
            current_player = successor_node.get_turn()



    def display_legal_moves(self, current_node, legal_moves):
        board_with_legal = self.transition_model.mark_legal_actions(current_node, legal_moves)
        self.game_output.display_graphic_board(board_with_legal, current_node.get_turn())
        # time.sleep(0.1)  # Delay for 1 second



