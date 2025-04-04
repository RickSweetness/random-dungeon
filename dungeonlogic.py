import tkinter as tk
from gridmanager import GridManager
from graphics import Square
import random
import math
import time

class DungeonManager:
    def __init__(self, grid, win, seed=None):
        self.grid = grid
        self.win = win
        if seed == None:
            self.seed = random.seed
        else:
            self.seed = seed
        self.offset = self.grid._full_width//4
        mid_w_list = len(grid.w_list)//2
        mid_l_list = len(grid.w_list[mid_w_list])//2
        self.start = grid.w_list[mid_w_list][mid_l_list]

    def draw_square(self, pos):
        if self.win is None:
            return
        ratio = self.grid.height/self.grid.width
        grid_w = int(math.sqrt(self.grid.size/ratio))
        cell_size = int(self.grid.width//grid_w)
        x1 = (pos[0] * cell_size) + self.offset
        y1 = (pos[1] * cell_size)
        x2 = ((pos[0] + 1) * cell_size) + self.offset
        y2 = ((pos[1] + 1) * cell_size)
        square = Square(self.win, x1, y1, x2, y2)

    def _animate(self):
        self.win.redraw()
        time.sleep(0.015)

    def choose_direction(self, start):
        possible_directions = []

    
    def create_corridor(self, start):
        roll = random.randrange(1, 20)
        if roll == 1:
            #straight 4 squares, continues with corridor
            pass


