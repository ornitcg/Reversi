from constants import *
from action import Action
from state_space import State_Space
from transition_model import Transition_Model
from node import Node
from player import *
class Simple_Player(Player):

    def __init__(self, color):
        super().__init__(color)


    def choose_action(self, node, legal_actions, heuristic = None):
        # Choose the first legal action - could also be a skip action.
        if legal_actions:
            return legal_actions[0]
        return None

    def get_color(self):
        return self.color

    def get_opponent_color(self):
        return self.opponent_color



