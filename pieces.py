import numpy as np


class Piece:

    def __init__(self):
        self.width = 0
        self.height = 0
        self.shape = np.zeros((self.width, self.height))
        self.x = None
        self.y = None

    def rotate(self):
        self.shape = np.rot90(self.shape)
        self.width, self.height = self.height, self.width

    def flip(self):
        self.shape = np.flip(self.shape, 1)

    def get_value(self):
        return np.sum(self.shape)

    def __repr__(self):
        rep = ""
        for row in range(self.height):
            rep += f"{self.shape[row]}\n"
        return rep


# Make a subclass of Piece with a name for each element in pieces
class One(Piece):
    def __init__(self):
        super().__init__()
        self.width = 1
        self.height = 1
        self.shape = np.array([[1]])


class Two(Piece):

    def __init__(self):
        super().__init__()
        self.width = 2
        self.height = 1
        self.shape = np.array([[1, 1]])


class Right(Piece):

    def __init__(self):
        super().__init__()
        self.width = 2
        self.height = 2
        self.shape = np.array([[1, 0],
                               [1, 1]])


class ThreeStraight(Piece):

    def __init__(self):
        super().__init__()
        self.width = 3
        self.height = 1
        self.shape = np.array([[1, 1, 1]])


class FourStraight(Piece):

    def __init__(self):
        super().__init__()
        self.width = 4
        self.height = 1
        self.shape = np.array([[1, 1, 1, 1]])


class L(Piece):

    def __init__(self):
        super().__init__()
        self.width = 2
        self.height = 3
        self.shape = np.array([[1, 0],
                               [1, 0],
                               [1, 1]])


class Triangle(Piece):

    def __init__(self):
        super().__init__()
        self.width = 3
        self.height = 2
        self.shape = np.array([[0, 1, 0],
                               [1, 1, 1]])


class Square(Piece):

    def __init__(self):
        super().__init__()
        self.width = 2
        self.height = 2
        self.shape = np.array([[1, 1],
                               [1, 1]])


class Step(Piece):

    def __init__(self):
        super().__init__()
        self.width = 2
        self.height = 3
        self.shape = np.array([[1, 0],
                               [1, 1],
                               [0, 1]])


class FiveStraight(Piece):

    def __init__(self):
        super().__init__()
        self.width = 1
        self.height = 5
        self.shape = np.array([[1], [1], [1], [1], [1]])


class LongL(Piece):

    def __init__(self):
        super().__init__()
        self.width = 4
        self.height = 2
        self.shape = np.array([[1, 1, 1, 1],
                               [0, 0, 0, 1]])


class LongStep(Piece):

    def __init__(self):
        super().__init__()
        self.width = 4
        self.height = 2
        self.shape = np.array([[1, 1, 0, 0],
                               [0, 1, 1, 1]])


class SquarePlus(Piece):

    def __init__(self):
        super().__init__()
        self.width = 2
        self.height = 3
        self.shape = np.array([[1, 1],
                               [1, 1],
                               [1, 0]])


class LongRight(Piece):

    def __init__(self):
        super().__init__()
        self.width = 3
        self.height = 3
        self.shape = np.array([[1, 0, 0],
                               [1, 0, 0],
                               [1, 1, 1]])


class Steps(Piece):

    def __init__(self):
        super().__init__()
        self.width = 3
        self.height = 3
        self.shape = np.array([[1, 0, 0],
                               [1, 1, 0],
                               [0, 1, 1]])


class Z(Piece):

    def __init__(self):
        super().__init__()
        self.width = 3
        self.height = 3
        self.shape = np.array([[1, 1, 0],
                               [0, 1, 0],
                               [0, 1, 1]])


class Hump(Piece):

    def __init__(self):
        super().__init__()
        self.width = 2
        self.height = 3
        self.shape = np.array([[1, 1],
                               [0, 1],
                               [1, 1]])


class LongWithSide(Piece):

    def __init__(self):
        super().__init__()
        self.width = 4
        self.height = 2
        self.shape = np.array([[0, 1, 0, 0],
                               [1, 1, 1, 1]])


class Plus(Piece):

    def __init__(self):
        super().__init__()
        self.width = 3
        self.height = 3
        self.shape = np.array([[0, 1, 0],
                               [1, 1, 1],
                               [0, 1, 0]])


class Crazy(Piece):

    def __init__(self):
        super().__init__()
        self.width = 3
        self.height = 3
        self.shape = np.array([[0, 1, 0],
                               [0, 1, 1],
                               [1, 1, 0]])


class T(Piece):

    def __init__(self):
        super().__init__()
        self.width = 3
        self.height = 3
        self.shape = np.array([[1, 1, 1],
                               [0, 1, 0],
                               [0, 1, 0]])


pieces = [One(),
          Two(),
          Right(), ThreeStraight(), FourStraight(), L(), Triangle(), Square(), Step(),
          FiveStraight(), LongL(), LongStep(), SquarePlus(), LongRight(), Steps(), Z(),
          Hump(), LongWithSide(), Plus(), Crazy(), T()]
DEFAULT_PIECES = np.array(pieces)
NUM_PIECES = len(pieces)


if __name__ == "__main__":

    # Test shapes of the pieces
    for piece in pieces:
        print(f"{piece.__class__}: \n{piece}")
