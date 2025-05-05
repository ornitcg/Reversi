from constants import *
from node import Node
from action import Action
from transition_model import *
from state_space import *
import copy


class Min_Max:
    def __init__(self, transition_model, state_space, heuristic=None):
        self.state_space = state_space
        self.transition_model = transition_model
        self.heuristic = heuristic


    def min_max(self, node, depth, perspective_player):

        # Base case: if depth is 0 or game is over, return heuristic value# Base case: if we reached the maximum depth or terminal state
        if depth == 0 or self.state_space.is_goal_state(node):
            # Evaluate the board from the perspective of the original player
            return self.heuristic.calculate(node, perspective_player), node.get_action()
        turn = node.get_turn()
        legal_actions = self.transition_model.get_legal_moves(node)
        scored_actions = []
        for action in legal_actions:
            # Create successor node by applying this action
            successor = self.transition_model.apply_action(node, action)
            score , act = self.min_max(successor, depth - 1, perspective_player)
            scored_actions.append((score, action))

        min_score = float('inf')
        min_action = Action(SKIP)
        max_score = float('-inf')
        max_action = Action(SKIP)

        for score, action in scored_actions:
            if score < min_score:
                min_score = score
                min_action = action
            if score > max_score:
                max_score = score
                max_action = action
        if turn == perspective_player:
            return max_score, max_action
        else:
            return min_score, min_action



    def get_transition_model(self):
        return self.transition_model
