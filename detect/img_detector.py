'''
Template Matching
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
'''
import cv2
import os
import numpy as np
from PIL import ImageGrab


# pil_img = ImageGrab.grab(bbox=None)
# opencv_img = np.array(pil_img)

target_img_path = "../resource/chrome_icon.PNG"
screen_img_path = "../resource/screen.PNG"

target_img = cv2.imread(os.path.abspath(target_img_path), 0)
to_find = target_img.copy()
template = cv2.imread(os.path.abspath(screen_img_path), 0)
w, h = to_find.shape[::-1]

img = to_find.copy()
method = eval('cv2.TM_SQDIFF')

# Apply template Matching
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

