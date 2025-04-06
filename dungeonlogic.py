import tkinter as tk
from gridmanager import GridManager
from graphics import Square
import random
import math
import time
from scipy.spatial import Delaunay
import numpy as np


class DungeonManager:
    def __init__(self, grid, win, num_rooms=5, seed=None):
        self.grid = grid
        self.win = win
        self.num_rooms = num_rooms
        if seed == None:
            self.seed = random.seed
        else:
            self.seed = seed
        self.offset = self.grid._full_width//4
        mid_w_list = len(grid.w_list)//2
        mid_l_list = len(grid.w_list[mid_w_list])//2
        self.start = grid.w_list[mid_w_list][mid_l_list]
        self.room_list = self.create_rooms()
        mst = self.min_spanning_tree(self.room_list)

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
        self.grid.w_list[pos[0]][pos[1]][2] = True #change to True to show the square is being used
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.015)

    def are_squares_used(self, squares):
        for cell in squares:
            square = self.grid.w_list[cell[0]][cell[1]]
            print(square)
            if cell[0] < 0 or cell[1] < 0 or cell[0] >= len(self.grid.w_list) -1 or cell[1] >= len(self.grid.w_list[0]) -1:
                print("Cell out of bounds")
                return True 
            if square[2]:
                print("squares are used")
                return True
        print("squares are unused")
        return False
    
    def create_rooms(self):
        # Create rooms in the grid
        rooms = 0
        attempts = 0
        room_list = []
        blocked_rooms = 0
        while rooms < self.num_rooms:
            if attempts >= 10000:
                print("Too many attempts to place rooms.")
                break
            attempts += 1
            blocked = False
            # Create a random size room 
            width_roll = random.randint(1, 20)
            length_roll = random.randint(1, 20)
            match width_roll:
                case 1:
                    width = 2
                case 2 | 3 | 4 | 5 | 6:
                    width = 3
                case 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14:
                    width = 4
                case 15 | 16 | 17 | 18 | 19 | 20:
                    width = 5
            match length_roll:
                case 1:
                    length = 2
                case 2 | 3 | 4 | 5 | 6:
                    length = 3
                case 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14:
                    length = 4
                case 15 | 16 | 17 | 18 | 19 | 20:
                    length = 5
            # Randomly select a position in the grid
            i = random.randint(0, len(self.grid.w_list) - 1 - width)
            j = random.randint(0, len(self.grid.w_list[i]) - 1 - length)

            # Check if the room can fit in the grid
            if i + width >= len(self.grid.w_list) or j + length >= len(self.grid.w_list[i]):
                continue               
            # Check if the room overlaps with existing rooms
            for x in range(width+2):
                for y in range(length+2):
                    if self.grid.w_list[i+x-1][j+y-1][2]:
                        blocked = True
            if blocked:
                # If the room is blocked, increment the blocked_rooms counter
                # and continue to the next attempt
                blocked_rooms += 1
            if not blocked:
                # Draw the room
                for x in range(width):
                    for y in range(length):
                        self.draw_square((i+x, j+y))
                rooms += 1
                room_list.append(((i + width // 2), (j + length // 2)))
        sorted_rooms = sorted(room_list, key=lambda p: (p[0], p[1]))
        return sorted_rooms

   
    def min_spanning_tree(self, points):
        # Create a graph from the Delaunay triangulation
        tess = Delaunay(points)
        edges = []
        for simplex in tess.simplices:
            for i in range(len(simplex)):
                for j in range(i + 1, len(simplex)):
                    edges.append((int(simplex[i]), int(simplex[j])))
        # Create a minimum spanning tree using Prim's algorithm
        mst = []
        visited = set()
        visited.add(0)
        attempts = 0
        while len(mst) < len(points) - 1:
            if attempts >= 10000:
                print("Too many attempts to create MST.")
                break
            attempts += 1
            # Find the minimum edge connecting the visited nodes to the unvisited nodes
            min_edge = None
            min_weight = float("inf")
            p = None
            for edge in edges:
                if edge not in mst:
                    if edge[0] in visited and edge[1] not in visited:
                        # Calculate the weight of the edge
                        weight = np.linalg.norm(np.array(points[edge[0]]) - np.array(points[edge[1]]))
                        if weight <= min_weight:
                            min_weight = weight
                            min_edge = edge
                            p = 1    
                    if edge[1] in visited and edge[0] not in visited:
                        # Calculate the weight of the edge
                        weight = np.linalg.norm(np.array(points[edge[1]]) - np.array(points[edge[0]]))
                        if weight <= min_weight:
                            min_weight = weight
                            min_edge = edge
                            p = 0    
            if min_edge is not None:
                mst.append(min_edge)
                visited.add(min_edge[p])
        print("MST Edges:")
        for edge in mst:
            print(edge)
        # Randomly select edges to add to the MST
        for edge in edges:
            if edge not in mst:
                temp = random.randint(1, 8)
                if temp == 1:
                    mst.append(edge)
        print("MST Edges:")
        for edge in mst:
            print(edge)
        return mst














    # def coord_lister(self, i, j, length, direction, check=False):
    #     coord_list = []

    #     if direction == "r":
    #         for x in range(length):
    #             coord_list.append((i + x, j))  # Add rightward cells
    #             if check:
    #                 coord_list.extend([(i + x, j + 1), (i + x, j - 1)])

    #     elif direction == "l":
    #         for x in range(length):
    #             coord_list.append((i - x, j))  # Add leftward cells
    #             if check:
    #                 coord_list.extend([(i - x, j + 1), (i - x, j - 1)])

    #     elif direction == "u":
    #         for x in range(length):
    #             coord_list.append((i, j - x))  # Add upward cells
    #             if check:
    #                 coord_list.extend([(i + 1, j - x), (i - 1, j - x)])

    #     elif direction == "d":
    #         for x in range(length):
    #             coord_list.append((i, j + x))  # Add downward cells
    #             if check:
    #                 coord_list.extend([(i + 1, j + x), (i - 1, j + x)])
    #     if check:
    #         coord_list = [coord for coord in coord_list if coord != (i, j) and coord not in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]]
    #     return coord_list

    # def choose_direction(self, start, r=False):
    #     grid_wlen = len(self.grid.w_list)  # number of columns
    #     grid_llen = len(self.grid.w_list[0])  # number of rows
    #     w = start[0]  # column
    #     l = start[1]  # row

    #     # Possible directions
    #     directions = ["u", "d", "l", "r"]

    #     # Exclude invalid directions based on position
    #     if "l" in directions:
    #         if w <= 1:  # Can't move left if you're at the left edge
    #             directions.remove("l")
    #     if "r" in directions:
    #         if w == grid_wlen - 1:  # Can't move right if you're at the right edge
    #             directions.remove("r")
    #     if "u" in directions:
    #         if l == 0:  # Can't move up if you're at the top edge
    #             directions.remove("u")
    #     if "d" in directions:
    #         if l == grid_llen - 1:  # Can't move down if you're at the bottom edge
    #             directions.remove("d")
    #     return directions


    # def create_corridor(self, i, j, directions, attempts=0):
    #     if attempts >= 30:
    #         return 
    #     start = self.grid.w_list[i][j]
    #     if len(directions) == 0 and False in directions:
    #         directions = self.choose_direction(start, r=True)
    #     if len(directions) == 0 and True in directions:
    #         directions = self.choose_direction(start)
    #     roll = random.randrange(1, 21)
    #     if roll >= 1:
    #         if len(directions) > 0:
    #             d = directions.pop(random.randrange(0, len(directions)))
    #             if d == "r":
    #                 print("trying right")
    #                 if self.are_squares_used(self.coord_lister(i, j, 4, "r", True)):
    #                     return self.create_corridor(i, j, directions, attempts+1)
    #                 else:
    #                     coords = self.coord_lister(i, j, 4, "r")
    #                     for coord in coords:
    #                         self.draw_square(self.grid.w_list[coord[0]][coord[1]])
    #                 return self.create_corridor(i+4, j, self.choose_direction(self.grid.w_list[i+4][j]))
    #             if d == "d":
    #                 print("trying down")
    #                 if self.are_squares_used(self.coord_lister(i, j, 4, "d", True)):
    #                     return self.create_corridor(i, j, directions, attempts+1)
    #                 else:
    #                     coords = self.coord_lister(i, j, 4, "d")
    #                     for coord in coords:
    #                         self.draw_square(self.grid.w_list[coord[0]][coord[1]])
    #                 return self.create_corridor(i, j+4, self.choose_direction(self.grid.w_list[i][j+4]))
    #             if d == "u":
    #                 print("trying up")
    #                 if self.are_squares_used(self.coord_lister(i, j, 4, "u", True)):
    #                     return self.create_corridor(i, j, directions, attempts+1)
    #                 else:
    #                     coords = self.coord_lister(i, j, 4, "u")
    #                     for coord in coords:
    #                         self.draw_square(self.grid.w_list[coord[0]][coord[1]])
    #                 return self.create_corridor(i, j-4, self.choose_direction(self.grid.w_list[i][j-4]))
    #             if d == "l":
    #                 print("trying left")
    #                 if self.are_squares_used(self.coord_lister(i, j, 4, "l", True)):
    #                     return self.create_corridor(i, j, directions, attempts+1)
    #                 else:
    #                     coords = self.coord_lister(i, j, 4, "l")
    #                     for coord in coords:
    #                         self.draw_square(self.grid.w_list[coord[0]][coord[1]])
    #                 return self.create_corridor(i-4, j, self.choose_direction(self.grid.w_list[i-4][j]))


