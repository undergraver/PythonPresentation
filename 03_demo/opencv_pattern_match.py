#!/usr/bin/env python3

# pip3 install pillow
# pip3 install opencv-python
# pip3 install matplotlib

import PIL.ImageGrab
import numpy as np
import cv2
from matplotlib import pyplot as plt


def grab_screen_image(left=-1,top=-1,right=-1,bottom=-1):
    screen = PIL.ImageGrab.grab()
    if left > -1 and top > -1 and right > -1 and bottom > -1:
        # it cuts part of screen only if all parameters are >= 0
        zone=(left,top,right,bottom)
        screen = screen.crop(zone)
    # transform to opencv the grabbed image
    opencv_image = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    # to debug/test:
    # cv2.imwrite("lulu.jpg",opencv_image)
    return opencv_image

def save_image(img_file,opencv_image):
    cv2.imwrite(img_file,opencv_image)

# load images in grayscale by default
def load_image(img_file_name,flag=cv2.IMREAD_GRAYSCALE):
    return cv2.imread(img_file_name,flag)

def convert_to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# code stolen from here: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html

# note: both images should be grayscale
def get_template_positions(big_img_gray,template_gray):
    w, h = template_gray.shape[::-1]
    res = cv2.matchTemplate(big_img_gray,template_gray,cv2.TM_CCOEFF_NORMED)
    
    # adjust the threshold for your particular case (background noise etc)
    threshold=0.8
    rectangles=[]
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        r = (pt[0],pt[1],pt[0] + w, pt[1] + h)
        rectangles.append(r)
    return rectangles

#############################################################
#############################################################
#############################################################
#############################################################
screen_img_name='screen.png'

big_image = load_image(screen_img_name)

template_images=['pip3_install_template.png','import_template.png']

for name in template_images:
    template = load_image(name)
    print("Analyzing:"+name)
    rectangles = get_template_positions(big_image,template)
    print("Number of matches:"+str(len(rectangles)))
    output_name='output_'+name
    print("Saving result to:"+output_name)
    big_image_with_color=load_image(screen_img_name,cv2.IMREAD_UNCHANGED)
    
    for r in rectangles:
        up_left = (r[0],r[1])
        low_bottom=(r[2],r[3])
        cv2.rectangle(big_image_with_color, up_left, low_bottom, (0,0,255), 2)
        
    save_image(output_name,big_image_with_color)
