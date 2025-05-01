



class Heuristic:
    def __init__(self):
        self.weights = {
            'corner': 1000,
            'edge': 100,
            'mobility': 10,
            'stability': 5,
            'parity': 1
        }
        self.corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
        self.edges = [(0, i) for i in range(1, 7)] + [(7, i) for i in range(1, 7)] + [(i, 0) for i in range(1, 7)] + [(i, 7) for i in range(1, 7)]