from graphics import Window, TKFrame, TKLabel, TKEntry, TKSlider
from gridmanager import GridManager
from dungeonlogic import DungeonManager
import tkinter as tk


dungeon_exists = False


def change_grid(value, grid):
    value *= 432
    for item in grid.w_list:
        del item
    for line in grid.line_ids:
        grid.window.get_canvas().delete(line)
    grid.size = int(value)
    grid.w_list = grid.grid_spawn_coords()
    grid.line_ids = grid.grid_spawn_lines()

def spawn_dungeon(grid, num_rooms, win):
    global dungeon_exists
    if dungeon_exists:
        print("Dungeon already exists")
        return
    dungeon_exists = True
    if num_rooms < 1:
        num_rooms = 1
    elif num_rooms > 50:
        num_rooms = 50
    dungeon = DungeonManager(grid=grid, num_rooms=num_rooms, win=win)
    dungeon.room_list = dungeon.create_rooms()
    dungeon.mst = dungeon.min_spanning_tree(dungeon.room_list)
    dungeon.corridors = dungeon.corridor_manager(dungeon.mst)
    return dungeon






def main():
    winx = 1920
    winy = 1080
    win = Window(winx, winy)
    

    grid = GridManager(winwidth=winx, winheight=winy, size=432, win=win)

    frm1 = TKFrame(winx/4, winy, 0, 0, win, anchor="nw")
    #entry1 = TKEntry(0, 0, text="# of Rooms", font="Helvetica", font_size = 12, frame1=frm1)
    size_slider = TKSlider(0, 3, frame1=frm1, font="Helvetica", font_size = 12, text="Grid Size", from_=1, to=15, func=change_grid, grid=grid)
    rooms_slider = TKSlider(0, 4, frame1=frm1, font="Helvetica", font_size = 12, text="# of Rooms", from_=1, to=50, func=None)


    go = tk.Button(frm1.get_root(), text="Generate!", command=lambda: spawn_dungeon(grid=grid, num_rooms=rooms_slider.get(), win=win))
    go.grid(column=0, row=5, columnspan=2, sticky="ew", padx=5, pady=5)








    win.wait_for_close()








if __name__ == "__main__":
    main() 