from graphics import Window, TKFrame, TKLabel, TKEntry, TKSlider
from gridmanager import GridManager
from dungeonlogic import DungeonManager
import tkinter as tk


def change_grid(value, grid):
    for item in grid.w_list:
        del item
    for line in grid.line_ids:
        grid.window.get_canvas().delete(line)
    grid.size = int(value)
    grid.w_list = grid.grid_spawn_coords()
    grid.line_ids = grid.grid_spawn_lines()


def main():
    winx = 1920
    winy = 1080
    win = Window(winx, winy)
    

    grid = GridManager(winwidth=winx, winheight=winy, size=500, win=win)

    frm1 = TKFrame(winx/4, winy, 0, 0, win, anchor="nw")
    #entry1 = TKEntry(0, 0, text="# of Rooms", font="Helvetica", font_size = 12, frame1=frm1)
    size_slider = TKSlider(0, 3, frame1=frm1, font="Helvetica", font_size = 12, text="Grid Size", from_=400, to=6000, func=change_grid, grid=grid)
    rooms_slider = TKSlider(0, 4, frame1=frm1, font="Helvetica", font_size = 12, text="# of Rooms", from_=1, to=20)

    dungo = DungeonManager(grid, win, 0)
    dungo.create_corridor(1,1, dungo.choose_direction(grid.w_list[1][1]))








    win.wait_for_close()








if __name__ == "__main__":
    main() 