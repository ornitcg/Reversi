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


    # def calculate(self, node, legal_actions, origin_player):
    #     turn = node.get_turn()
    #     max_score = -float('inf')
    #     chosen_action = Action(SKIP)
    #
    #     for action in legal_actions:
    #         # Create successor node by applying this action
    #         successor = self.transition_model.apply_action(node, action)
    #
    #         # Calculate the minimax value for this move
    #         score = self.minimax(successor, self.depth - 1, origin_player  )
    #
    #         # Update best action if we found a better score
    #         if score > max_score:
    #             max_score = score
    #             chosen_action = action
    #
    #     return chosen_action

    def min_max(self, node, depth, perspective_player):

        # Base case: if depth is 0 or game is over, return heuristic value# Base case: if we reached the maximum depth or terminal state
        if depth == 0 or self.state_space.is_goal_state(node):
            # Evaluate the board from the perspective of the original player
            return self.heuristic.calculate(node, perspective_player), None
        ### get legal actions from tm
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
        #### loop on it and get score for each by minmax




        #### collect to list all sscores calced by minmax fo all successors


    def get_transition_model(self):
        return self.transition_model
