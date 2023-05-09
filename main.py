import sys

from functions import *

# game board to hold data
game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]

arg = None
if len(sys.argv)>1:
    arg = sys.argv[1]

if arg == None and not isinstance(arg,str):
    player = "X"
else:
    player = arg
# play game
exitGame=False
while not exitGame:
    exitGame = play_game(game_board,player)
