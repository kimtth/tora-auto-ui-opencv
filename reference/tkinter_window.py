from tkinter import Tk, Button, Frame

from screenshot.grab_screenshot import shot_execute


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


def exec(workspace_path, qt):
    window = Tk()
    window.geometry("50x25+300+300")
    window.resizable(0, 0)
    window.configure(bg=_from_rgb((0,0,102)))

    b_frame = Frame(window)
    b_frame.place(x=0, y=0)

    button = Button(b_frame, text="Capture", command=lambda: shot_execute(window, qt, workspace_path))
    button.pack()

    window.mainloop()

