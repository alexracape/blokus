import numpy as np
from player import Player


# Currently riddled with bugs
# out of bounds index for corner and adjacent checking
# rows and cols might be flipped somewhere in this stack
# Placing p2 move isn't working
# Check that start condition works for pieces placed off of the edge, gui would make this much more intuitive
# Gui is a total mess, but the boiler plate from chat gpt may be close, probably need to scrap
class Board:
    def __init__(self, num_players=4, num_rows=20, num_cols=20):
        self.num_players = num_players
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.start_spaces = [(0, 0), (0, num_cols - 1), (num_rows - 1, 0), (num_rows - 1, num_cols - 1)]
        self.players = [Player(i+1, self.start_spaces[i]) for i in range(num_players)]
        self.current_player = self.players[0]
        self.board = np.zeros((num_rows, num_cols))

    def make_move(self, piece, row, col, player):
        # Piece is 'placed' at top left corner of bounding box

        # Check if move is valid
        if not self.is_valid_move(piece, row, col, player):
            return False

        # Make the move
        for i in range(piece.height):
            for j in range(piece.width):
                if piece.shape[i][j] == 1:
                    self.board[row+i][col+j] = player.number

        # Update player
        piece_inventory = player.pieces_left
        player.pieves_left = np.delete(piece_inventory, np.where(piece_inventory == piece))
        if len(piece_inventory) == 0:
            player.is_done = True
        self.current_player = self.players[self.current_player.number % self.num_players]
        return True

    def check_adjacent(self, row, col, player):
        # Helper to check if there is a friendly piece touching a corner
        hits_corner = False
        hits_self = False
        hits_start = False
        color = player.number

        if self.board[row+1][col+1] == color \
                or self.board[row+1][col-1] == color \
                or self.board[row-1][col+1] == color \
                or self.board[row-1][col-1] == color:
            hits_corner = True

        if self.board[row+1][col] == color \
                or self.board[row-1][col] == color \
                or self.board[row][col+1] == color \
                or self.board[row][col-1] == color:
            hits_self = True

        # Start condition after checking edge of board
        if (row, col) == player.start_space and self.board[row][col] == 0:
            hits_start = True

        return hits_corner, hits_self, hits_start

    def is_valid_move(self, piece, row, col, player):

        # Iterate through piece shape
        corner = False
        for i in range(piece.height):
            for j in range(piece.width):

                # Check for any overlap, check back for off by one bounds of board
                if piece.shape[i][j] == 1 and row+i < self.num_rows and col+j < self.num_cols and self.board[row+i][col+j] != 0:
                    return False

                # Check if it hits a corner
                hits_corner, hits_self, hits_start = self.check_adjacent(row, col, player)
                if hits_self:
                    return False
                if hits_corner:
                    corner = True
                if hits_start:
                    return True

        return corner

    def is_game_over(self):
        for player in self.players:
            if not player.is_done:
                return False
        return True


    def __repr__(self):
        rep = ""
        for row in range(self.num_rows):
            rep += f"{self.board[row]}\n"
        return rep


if __name__ == "__main__":

    board = Board()
    print(board)
    while True:

        current_player = board.current_player
        print("Current player: ", current_player.number)

        for piece in current_player.pieces_left:
            print(f"{np.where(current_player.pieces_left == piece)[0]}: \n{piece}")
        piece_num = input("Enter piece: ")

        piece = current_player.pieces_left[int(piece_num)]
        x = input("Enter row number: ")
        y = input("Enter col number: ")
        result = board.make_move(piece, int(x), int(y), current_player)
        if result:
            print("Move successful")
            print(board)
        else:
            print("Move failed")

        if board.is_game_over():
            print("Game over")
            break

        quite = input("Quit? (y/n): ")
        if quite == "y":
            break

