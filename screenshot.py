import logging
import struct
import io
import os
from datetime import datetime
import zlib
from collections import namedtuple
from mss import mss
from PIL import Image

try:
    import Tkinter as tk
except ModuleNotFoundError:
    import tkinter as tk


'''
This code is a part of the Grab-Screen.
Simplifying the code for offline use.
https://github.com/andrei-shabanski/grab-screen
'''
__title__ = "demo"
logger = logging.getLogger(__title__)

Image_Container = namedtuple('Image', ('stream', 'format'))
Coords = namedtuple('Coords', ('top', 'left', 'right', 'bottom'))


class Grabber(tk.Tk):
    WINDOW_COLOR = '#ffffff'
    WINDOW_ALPHA = 0.2

    RECTANGLE_COLOR = '#000000'

    @classmethod
    def select_area(cls):
        logger.info("Selecting an area.")

        # run TK app to select an area
        scope = {'coords': None}

        def set_coords(_coords):
            scope['coords'] = _coords
            grabber.exit()  # close the window

        grabber = cls(on_selected=set_coords) #, root_win=root)
        print('grabber')
        try:
            grabber.mainloop()
        except KeyboardInterrupt:
            grabber.exit()

        coords = scope['coords']
        print("aaa" + str(coords))
        if not coords:
            pass

        # normalize coords
        coords = tuple(map(int, coords))
        left, right = sorted(coords[0::2])
        top, bottom = sorted(coords[1::2])

        print("abb" + str(coords))
        logger.debug("Selected area %s.", coords)
        return Coords(top, left, right, bottom)

    def __init__(self, on_selected, root_win):
        tk.Tk.__init__(self)

        self.title(__title__)

        self._on_selected = on_selected

        self._coords = None
        self._rect_id = None
        self._is_drawing = False

        self._canvas = None
        self._root_win = root_win

        self.initialize_geometry()
        self.initialize_controls()

    def initialize_geometry(self):
        self.wait_visibility()
        self.attributes('-topmost', True)
        self.attributes('-fullscreen', True)
        self.attributes('-alpha', self.WINDOW_ALPHA)

    def initialize_controls(self):
        self._canvas = tk.Canvas(self, bg=self.WINDOW_COLOR, cursor='crosshair')
        self._canvas.pack(fill=tk.BOTH, expand=1)

        self._canvas.bind('<Button-1>', self.start_drawing)
        self._canvas.bind('<Button-3>', self.exit)
        self._canvas.bind('<ButtonRelease-1>', self.stop_drawing)
        self._canvas.bind('<Motion>', self.draw_rectangle)

    def start_drawing(self, event):
        logger.debug("Selecting screen area.")
        self._is_drawing = True

        x = self._canvas.canvasx(event.x)
        y = self._canvas.canvasy(event.y)

        self._coords = [x, y, x, y]
        self._rect_id = self._canvas.create_rectangle(*self._coords, fill=self.RECTANGLE_COLOR)

    def draw_rectangle(self, event):
        if not self._is_drawing:
            return

        self._coords[2] = self._canvas.canvasx(event.x)
        self._coords[3] = self._canvas.canvasy(event.y)
        self._canvas.coords(self._rect_id, *self._coords)

    def stop_drawing(self, event):
        logger.debug("Screen area has been selected. Coords: %s", self._coords)
        self._is_drawing = False
        self._canvas.delete(self._rect_id)
        print(self._coords)
        self._on_selected(self._coords)

    def exit(self, event=None):
        self.attributes('-alpha', 0)
        self.destroy()
        self._root_win.deiconify()
        print('call exit')

    def __del__(self):
        print('del class')


def capture_image(coords):
    """Take a screenshot."""
    logger.info("Capturing a screen.")
    screen = mss()
    mss_image = screen.grab({
        'top': coords.top,
        'left': coords.left,
        'width': coords.right - coords.left + 1,
        'height': coords.bottom - coords.top + 1,
    })

    stream = to_png(mss_image.rgb, mss_image.size)

    return Image_Container(stream, 'png')


def to_png(data, size):
    """
    Dump data to a PNG file.

    This code is a part of the MSS library.
    Source: https://github.com/BoboTiG/python-mss/blob/d740fa774cae4b8ccaddf980cbf417ebe33117e7/mss/tools.py#L10
    MSS License: MIT
    2017-07-18

    :param bytes data: RGBRGB...RGB data.
    :param tuple size: The (width, height) pair.
    """

    width, height = size
    line = width * 3
    png_filter = struct.pack('>B', 0)
    scanlines = b''.join(
        [png_filter + data[y * line:y * line + line]
         for y in range(height)])

    magic = struct.pack('>8B', 137, 80, 78, 71, 13, 10, 26, 10)

    # Header: size, marker, data, CRC32
    ihdr = [b'', b'IHDR', b'', b'']
    ihdr[2] = struct.pack('>2I5B', width, height, 8, 2, 0, 0, 0)
    ihdr[3] = struct.pack('>I', zlib.crc32(b''.join(ihdr[1:3])) & 0xffffffff)
    ihdr[0] = struct.pack('>I', len(ihdr[2]))

    # Data: size, marker, data, CRC32
    idat = [b'', b'IDAT', zlib.compress(scanlines), b'']
    idat[3] = struct.pack('>I', zlib.crc32(b''.join(idat[1:3])) & 0xffffffff)
    idat[0] = struct.pack('>I', len(idat[2]))

    # Footer: size, marker, None, CRC32
    iend = [b'', b'IEND', b'', b'']
    iend[3] = struct.pack('>I', zlib.crc32(iend[1]) & 0xffffffff)
    iend[0] = struct.pack('>I', len(iend[2]))

    # store data in memory
    fileh = io.BytesIO()
    fileh.write(magic)
    fileh.write(b''.join(ihdr))
    fileh.write(b''.join(idat))
    fileh.write(b''.join(iend))
    fileh.seek(0)

    return fileh


def save_image(image):
    logger.info('Uploading an image to CloudApp.')
    now = datetime.now()
    dir_name = 'tmp\\'
    filename = 'capture-%s.%s' % (now.strftime('%Y-%m-%d-%H%M%S'), image.format)
    file_path = dir_name + filename

    byteImg = Image.open(image.stream)
    byteImg.show()

    ans_file_path = os.path.abspath(file_path)
    byteImg.save(ans_file_path, 'PNG')


def shot_execute(window):
    window.withdraw()

    #coords = Grabber.select_area(window)
    #image = capture_image(coords)
    #save_image(image)


if __name__ == '__main__':
    coords = Grabber.select_area()
    image = capture_image(coords)

    save_image(image)

