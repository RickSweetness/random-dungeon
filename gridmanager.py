from graphics import Square
from graphics import Window
import tkinter as tk
import math

class GridManager:
    def __init__(self, winwidth, winheight, size, win):
        self.size = size
        self._full_width = winwidth
        self.width = winwidth * .75
        self.height = winheight
        self.window = win
        self.w_list = self.grid_spawn_coords()
        self.line_ids = self.grid_spawn_lines()

    def grid_spawn_coords(self):
        ratio = self.height/self.width
        grid_w = int(math.sqrt(self.size/ratio))
        grid_h = int(grid_w * ratio)
        w_list = []
        for i in range(grid_w):
            l_list = []
            w_list.append(l_list)
            for j in range (grid_h):
                l_list.append([i,j,False]) #turns false when the square gets painted
        return w_list
       
    def grid_spawn_lines(self):
        ratio = self.height/self.width
        grid_w = int(math.sqrt(self.size/ratio))
        grid_h = int(grid_w * ratio)
        cell_size = self.width/grid_w
        line_list = []
        for i in range(grid_w+2):
            j = (i * cell_size) + (self._full_width//4)
            line_id = self.window.get_canvas().create_line(j, 0, j, (grid_h+1)*cell_size, fill="#353432", width=1)
            line_list.append(line_id)
        for i in range(grid_h+2):
            j = ((i + 1) * cell_size)
            line_id = self.window.get_canvas().create_line(self._full_width/4, j, self._full_width, j, fill="#353432", width=1)
            line_list.append(line_id)
        return line_list