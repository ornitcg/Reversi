from constants import *


class Player:
    def __init__(self, color):
        self.color = color
        self.opponent_color = WHITE if color == RED else RED

    def choose_action(self, node, legal_actions):
        pass

    def get_color(self):
        pass

    def get_opponent_color(self):
        pass