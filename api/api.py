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
        self.auto.click(x=coord[0], y=coord[1])

    def wait(self, sec):
        time.sleep(sec)

    def press_hotkey(self, key_name):
        keys = key_name.split('_')
        # self.auto.hotkey('ctrl', 'c')  # ctrl-c to copy
        key_one = str(keys[0])
        key_two = str(keys[1])
        self.auto.hotkey(key_one, key_two)
        print(key_one, key_two)

    def type(self, string):
        secs_between_keys = 0.2
        self.auto.typewrite(string, interval=secs_between_keys)

    def press(self, key_name):
        if '_' in key_name:
            self.press_hotkey(key_name)
        else:
            self.auto.keyDown(key_name)
            self.auto.keyUp(key_name)

