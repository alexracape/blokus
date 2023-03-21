from blokus import pieces


class Player:

    def __init__(self, num, starting_space=(0, 0)):
        self.number = num
        self.pieces_left = pieces.DEFAULT_PIECES.copy()
        self.is_done = False
        self.start_space = starting_space

    def get_score(self):
        return sum([piece.get_value() for piece in self.pieces_left])

    def __str__(self):
        return f"Player {self.number}; Score: {self.score}; Pieces Left: {self.pieces_left}"
