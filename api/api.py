import pyautogui
import time

pyautogui.PAUSE = 1.5


class AutoGuiWrapper:

    def __init__(self):
        self.auto = pyautogui

    def right_click(self):
        self.auto.click(button='right')

    def double_click(self):
        self.auto.click(clicks=2)

    def click(self, coord):
        self.auto.click(x=coord['x'], y=coord['y'])

    def wait(self, sec):
        time.sleep(sec)

    def press_hotkey(self, key_name):
        keys = key_name.split('_')
        # self.auto.hotkey('ctrl', 'c')  # ctrl-c to copy
        self.auto.hotkey(keys[0], keys[1])

    def type(self, string):
        secs_between_keys = 0.2
        self.auto.typewrite(string, interval=secs_between_keys)

    def press(self, key_name):
        self.auto.keyDown(key_name)
        self.auto.keyUp(key_name)

