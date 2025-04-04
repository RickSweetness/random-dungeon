import tkinter as tk
from gridmanager import GridManager
from graphics import Square
import random

class DungeonManager:
    def __init__(self, grid, win, seed=None):
        self.grid = grid
        self.win = win
        if seed == None:
            self.seed = random.seed
        else:
            self.seed = seed
        mid_w_list = len(grid.w_list)//2
        mid_l_list = len(grid.w_list[mid_w_list])//2
        self.start = grid.w_list[mid_w_list][mid_l_list]
    
    def create_corridor(self, start):
        roll = random.randrange(1, 20)
        if roll == 1:
            #straight 4 squares

