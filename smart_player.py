from simple_player import *
from constants import *
from action import Action
from heuristic import *
from state_space import State_Space
from transition_model import Transition_Model
from node import Node


class Smart_Player(Simple_Player):
    def __init__(self, color):
        super().__init__(color)

    def choose_action(self, node, legal_actions, heuristic: Heuristic = None, tree=None):
        max_score = -float('inf')
        chosen_action = Action(SKIP)
        tm = heuristic.get_transition_model()
        # Choose the first legal action - could also be a skip action.
        if heuristic is not None:
            for action in legal_actions:
                if action.get_type() == ADD:
                    # Check if the action is legal
                    successor_node = tm.apply_action(node, action) #artificial node
                    score = heuristic.calculate(successor_node, self)
                    if score > max_score:
                        max_score = score
                        chosen_action = action
        return chosen_action

