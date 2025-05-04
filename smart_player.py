from simple_player import *
from constants import *
from action import Action
from state_space import State_Space
from transition_model import Transition_Model
from node import Node


class Smart_Player(Simple_Player):
    def __init__(self, color):
        super().__init__(color)

    def choose_action(self, node, legal_actions, heuristic = None):
        max_score = 0
        chosen_action = Action(SKIP)
        # Choose the first legal action - could also be a skip action.
        if heuristic is not None:
            for action in legal_actions:
                if action.get_type() == ADD:
                    # Check if the action is legal
                    score = heuristic.calculate(node, self)
                    if score > max_score:
                        max_score = score
                        chosen_action = action
        return chosen_action
