from action import *
from constants import *
from state_space import *
from transition_model import *
from node import *
from game_board import *
import time

class Game_Engine:
    def __init__(self,  players , start_node = None):
        self.game_board = Game_Board()
        self.game_board.initialize_GUI()
        self.transition_model = Transition_Model(players)
        self.state_space = State_Space(players, self.transition_model)
        self.player_red = players[0]
        self.player_white = players[1]
        if start_node:
            self.initial_state = start_node
        else:
            self.initial_state = self.state_space.get_initial_state()

    def play(self, max_disks=None):

        current_node = self.initial_state
        current_player = current_node.get_turn()

        skipped_turns = 0  # count of skipped turns. if both players skip, no legal moves exist for anyone and game is over
        while skipped_turns < 2 :

            self.game_board.display_graphic_board(current_node.get_board())
            self.game_board.display_textual_board(current_node.get_board())
            print('\n')
            time.sleep(0.5)  # Delay for 1 second

            legal_moves = self.transition_model.get_legal_moves(current_node)
            self.display_legal_moves( current_node, legal_moves)

            if max_disks is not None:
                if current_node.get_total_count() == max_disks:
                    self.legal_moves_output(current_node, legal_moves)
                    break

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



    def display_legal_moves(self, current_node, legal_moves):
        board_with_legal = self.transition_model.mark_legal_actions(current_node, legal_moves)
        self.game_board.display_graphic_board(board_with_legal, current_node.get_turn())
        # self.game_board.display_textual_board(board_with_legal)
        time.sleep(0.5)  # Delay for 1 second



    def legal_moves_output(self, current_node, legal_moves):
        print("********* Display all actions: ***************")
        print("Player 1 - X (red) , Player 2 - O (white)")

        for action in legal_moves:
            successor_node = self.state_space.get_successor(current_node, action)
            print("\nState number: ", current_node.get_total_count() - NUMBER_OF_INITIAL_DISKS)
            self.game_board.display_textual_board(current_node.get_board())

            print(f"State number: {successor_node.get_total_count() - NUMBER_OF_INITIAL_DISKS}", end=' ')

            print(f"\nPlayer {current_node.get_turn().get_color()} moved, Action ADD{action.get_position()}")
            self.game_board.display_textual_board(successor_node.get_board())
            #print each player's disks
            print(f"Result: Player X:{successor_node.get_red_count()} disks ,Player O: {successor_node.get_white_count()} disks. Total disks = {successor_node.get_total_count()}")