import cv2 as cv
import numpy as np

def myRgb2Gray(rgb_pic):
    gray_pic=cv.cvtColor(rgb_pic,cv.COLOR_RGB2GRAY)
    return gray_pic

