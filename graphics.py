import tkinter as tk

class Window:
    def __init__(self, width, height, colour="#1f1e1d"):
        self.__root = tk.Tk()
        self.__root.title("Dungo Rando")
        self.__canvas = tk.Canvas(self.__root, width=width, height=height, bg=colour)
        self.__canvas.grid()
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas.grid_columnconfigure(0, minsize=width/8)
        self.__canvas.grid_columnconfigure(1, minsize=width/8)
        self.width = width
    
    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def close(self):
        self.__is_running = False

    def get_canvas(self):
        return self.__canvas
    
    def get_root(self):
        return self.__root
            
class TKFrame:
    def __init__(self, width, height, x, y, win, colour="#353432", anchor="center"):
        self.canvas = win.get_canvas()
        self.__root = tk.Frame(win.get_root(), height=height, width=width, bg=colour)
        self.canvas.create_window(x, y, anchor=anchor, height=height, width=width, window=self.__root)
        self.__root.grid_columnconfigure(0, minsize=win.width/8)
        self.__root.grid_columnconfigure(1, minsize=win.width/8)

    def get_root(self):
        return self.__root

class TKLabel:
    def __init__(self, x, y, text, font, frame, colour="#2a2927", font_colour="#f1f0ec", anchor="center"):
        frame_root = frame.get_root()
        self.__root = tk.Label(frame_root, text=text, bg=colour, anchor=anchor, font=font, fg=font_colour)
        self.__root.grid(column=x, row=y, sticky="ew", padx=5, pady=5)

class TKEntry:
    def __init__(self, x, y, frame1, font, font_size, text, colour="#f1f0ec", font_colour="#2a2927"):
        frame1_root = frame1.get_root()
        self.__root = tk.Entry(frame1_root, font=(font, font_size), bg=colour, fg=font_colour)
        self.__lbl = TKLabel(x, y, text, font=(font, font_size), frame=frame1)
        self.__root.grid(column=x+1, row=y, sticky="ew", padx=5, pady=5)

class TKSlider:
    def __init__(self, x, y, frame1, font, font_size, text, from_=0, to=10, colour="#f1f0ec", font_colour="#2a2927", func=None, grid=None):
        frame1_root = frame1.get_root()
        self.__root = tk.Scale(frame1_root, font=(font, font_size), bg=colour, fg=font_colour, from_=from_, to=to, orient="horizontal", length=200, command=self.ret)
        self.__lbl = TKLabel(x=x, y=y, text=text, font=(font, font_size), frame=frame1)
        self.__root.grid(column=x+1, row=y, sticky="ew", padx=5, pady=5)
        self.grid = grid
        self.func = func

    def ret(self, value):
        value = int(value)
        return self.func(value, self.grid)

            
class Square:
    def __init__(self, win, x0, y0, x1, y1, colour="#f1f0ec"):
        canvas = win.get_canvas()
        canvas.create_rectangle(x0, y0, x1, y1, fill=colour)

class Wall:
    def __init__(self, win, x0, y0, x1, y1, colour="#353432"):
        canvas = win.get_canvas()
        canvas.create_rectangle(x0, y0, x1, y1, fill=colour)
