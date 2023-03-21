from board import Board

# create a gui for the board with the pieces for each player
# each player has a different color for their pieces, and they can rotate or flip the pieces before playing them
# the pieces are numbered, and the player can choose which piece to play
# the players can choose where to place the piece, and it will only let them place it if it is a valid move
# the game should also keep track of the scores for each player
# the game should also have a 'back' button so that a player can undo a move
# the game should also have a 'forward' button so that a player can redo a move
# the game should also have a 'restart' button so that a player can restart the game
# the game should also have a 'quit' button so that a player can quit the game
# the game should also have a 'save' button so that a player can save the game
# the game should also have a 'load' button so that a player can load a game

import tkinter as tk


class BlokusGUI(Board):
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.root.title("Blokus Bot")
        self.moves = []
        self.undone_moves = []
        self.canvas = None
        self.create_widgets()

    def restart_game(self):
        self.__init__()

    def save_game(self):
        pass

    def load_game(self):
        pass

    def undo_move(self):
        pass

    def redo_move(self):
        pass

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack()
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.canvas.create_rectangle(100 * i, 100 * j, 100 * (i + 1), 100 * (j + 1))

        self.player1_pieces = self.players[0].pieces_left
        self.player2_pieces = self.players[1].pieces_left
        self.canvas.create_oval(10, 310, 30, 330, fill='red', tags='player1_piece1')
        self.canvas.create_oval(40, 310, 60, 330, fill='red', tags='player1_piece2')
        self.canvas.create_oval(70, 310, 90, 330, fill='red', tags='player1_piece3')
        self.canvas.create_oval(200, 310, 220, 330, fill='blue', tags='player2_piece1')
        self.canvas.create_oval(230, 310, 250, 330, fill='blue', tags='player2_piece2')
        self.canvas.create_oval(260, 310, 280, 330, fill='blue', tags='player2_piece3')

        # self.rotate_button = tk.Button(self.root, text="Rotate", command=None)
        # self.rotate_button.pack(side='left')
        # self.flip_button = tk.Button(self.root, text="Flip", command=None)
        # self.flip_button.pack(side='left')

        piece_choices = list(range(1, 4))
        self.piece_var = tk.StringVar()
        self.piece_var.set(piece_choices[0])
        self.piece_menu = tk.OptionMenu(self.root, self.piece_var, *piece_choices)
        self.piece_menu.pack(side='left')

        self.coords_entry = tk.Entry(self.root, width=5)
        self.coords_entry.pack(side='left')
        self.coords_entry.insert(0, '0, 0')
        # vcmd = (self.root.register(self.validate_coords), '%P')
        # self.coords_entry.config(validate='key', validatecommand=vcmd)

        self.play_button = tk.Button(self.root, text="Play", command=self.place_piece)
        self.play_button.pack(side='left')

        self.back_button = tk.Button(self.root, text="Back", command=self.undo_move)
        self.back_button.pack(side='left')
        self.forward_button = tk.Button(self.root, text="Forward", command=self.redo_move)
        self.forward_button.pack(side='left')

        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
        self.restart_button.pack(side='left')
        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy)
        self.quit_button.pack(side='left')
        self.save_button = tk.Button(self.root, text="Save", command=self.save_game)
        self.save_button.pack(side='left')
        self.load_button = tk.Button(self.root, text="Load", command=self.load_game)
        self.load_button.pack(side='left')




if __name__ == '__main__':
    my_gui = BlokusGUI()
    my_gui.root.mainloop()
