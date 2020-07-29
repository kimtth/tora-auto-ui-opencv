from PIL import Image, ImageDraw, ImageTk
from tkinter import Tk, Button, Frame, mainloop, YES, BOTH, NW

from screenshot import shot_execute


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

def exec():
    print('exec')

if __name__ == '__main__':
    window = Tk()
    window.geometry("300x100+300+300")
    window.configure(bg=_from_rgb((0,0,102)))

    b_frame = Frame(window)
    b_frame.place(x=50, y=50)

    button = Button(b_frame, text="Capture", command=lambda: shot_execute(window))
    button.pack()

    window.mainloop()

