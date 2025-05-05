

from smart_player import *
from constants import *
from action import Action
from heuristic import *
from state_space import State_Space
from transition_model import Transition_Model
from node import Node


class Min_Max_Player(Smart_Player):
    def __init__(self, color):
        super().__init__(color)

    def choose_action(self, node, legal_actions, heuristic: Heuristic = None, min_max=None, depth = None):
        chosen_action = None
        # Choose the first legal action - could also be a skip action.
        if min_max:
            score, chosen_action = min_max.min_max(node, depth, node.get_turn())
        return chosen_action

