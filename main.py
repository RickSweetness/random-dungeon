from graphics import Window, TKFrame, TKLabel, TKEntry, TKSlider
import tkinter as tk

class DungeonLogic:
    def __init__(self):
        pass

def set_rooms(number):
    print(number)
    return number

def main():
    num_rooms = 0
    win = Window(1600, 900)

    frm1 = TKFrame(400, 900, 0, 0, win, anchor="nw")
    entry1 = TKEntry(0, 1, text="# of Rooms", font="Helvetica", font_size = 12, frame1=frm1)
    slider = TKSlider(0, 2, frame1=frm1, font="Helvetica", font_size = 12, text="# of Rooms")
    entry2 = TKEntry(0, 3, text="# of Rooms", font="Helvetica", font_size = 12, frame1=frm1)
    slider2 = TKSlider(0, 4, frame1=frm1, font="Helvetica", font_size = 12, text="# of Rooms")
    slider3 = TKSlider(0, 5, frame1=frm1, font="Helvetica", font_size = 12, text="# of Rooms")
    slider4 = TKSlider(0, 6, frame1=frm1, font="Helvetica", font_size = 12, text="# of Rooms")
    slider5 = TKSlider(0, 0, frame1=frm1, font="Helvetica", font_size = 12, text="# of Rooms")








    win.wait_for_close()








if __name__ == "__main__":
    main() 