import unittest
from board import Board


class MyTestCase(unittest.TestCase):
    def test_valid_move(self):
        board = Board()
        print(board)
        self.assertTrue(board.is_valid_move(board.players[0].pieces_left[0], 0, 0, board.players[0]))
        print(board)
        self.assertFalse(board.is_valid_move(board.players[0].pieces_left[0], 0, 0, 1))
        self.assertFalse(board.is_valid_move(board.players[0].pieces_left[0], 0, 0, 2))
        self.assertFalse(board.is_valid_move(board.players[0].pieces_left[0], 0, 0, 3))
        self.assertFalse(board.is_valid_move(board.players[0].pieces_left[0], 0, 0, 4))


if __name__ == '__main__':
    unittest.main()
