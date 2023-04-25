import tkinter as tk
from functions import *



root = tk.Tk()

# game board to hold data

game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]

# know if game over

winner = None




# play game
play_game(game_board)

root.mainloop()