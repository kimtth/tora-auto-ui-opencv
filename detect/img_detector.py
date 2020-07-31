'''
Template Matching
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
'''
import tempfile

import cv2
import os
import numpy as np
import pyautogui
from PIL import Image, ImageGrab


# pil_img = ImageGrab.grab(bbox=None)
# opencv_img = np.array(pil_img)

def pil2cv(image):
    new_image = np.array(image, dtype=np.uint8)
    if new_image.ndim == 2:
        pass
    elif new_image.shape[2] == 3:
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)
    elif new_image.shape[2] == 4:
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGBA2BGRA)
    return new_image


def temp_img_to_cv2():
    pil_img = Image.open('C:/Users/IEUser/code/tora/resource/temp/temp_pic.png')
    cv_img = cv2.imread('C:/Users/IEUser/code/tora/resource/temp/temp_pic.png', 0)

    return cv_img

def img_coord_detector_by_target(target_img_path):
    image = pyautogui.screenshot('C:/Users/IEUser/code/tora/resource/temp/temp_pic.png')
    # screen_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    screen_img = temp_img_to_cv2()

    return img_coord_detector(target_img_path, screen_img)


def img_coord_detector_by_target_screen(target_img_path, screen_img_path):
    template = cv2.imread(os.path.abspath(screen_img_path), 0)
    return img_coord_detector(target_img_path, template)


def img_coord_detector(target_img_path, screen_img):
    # target_img_path = "../resource/chrome_icon.PNG"
    # screen_img_path = "../resource/screen.PNG"

    target_img = cv2.imread(os.path.abspath(target_img_path), 0)
    template = screen_img
    # template = cv2.imread(os.path.abspath(screen_img_path), 0)
    w, h = target_img.shape[::-1]

    img = target_img.copy()
    method = eval('cv2.TM_SQDIFF')

    # Apply template Matching
    try:
        res = cv2.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0] + w, top_left[1] + h)
        # cv2.rectangle(img, top_left, bottom_right, 255, 2)

        center_w = (top_left[1] + bottom_right[1]) / 2
        center_h = (top_left[0] + bottom_right[0]) / 2

        print(top_left, bottom_right)
        print(round(center_w, 1), round(center_h, 1))

        center = (round(center_h, 1), round(center_w, 1))

        return center
    except Exception as e:
        print("An exception occurred")
        print(e)

