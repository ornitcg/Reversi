from player import *
from constants import *
from action import Action
from state_space import State_Space
from transition_model import Transition_Model
from node import Node


class Smart_Player(Player):
    def __init__(self, heuristic):
        self.score = 0
        self.heuristic = heuristic

    def play(self, game):
        # Implement the logic for the smart player to play their turn
        pass

    def calculate_score(self):
        # Implement the logic to calculate the player's score
        pass

    def __str__(self):
        return f"{self.name} (ID: {self.player_id})"