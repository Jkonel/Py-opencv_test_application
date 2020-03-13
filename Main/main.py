#Test python main file
import numpy as np
import cv2 as cv
from func import myRgb2Gray

print('Python-opencv test program') 
# Load an color image in grayscale
# 使用灰度图方式加载一张彩色照片
img = cv.imread(r'C:\Users\Jkonel.000\Desktop\GitTest\Py-opencv_test_application\Figures\daofeng.jpg')
if img is None:
    print('Image read false!')
    exit(-1)

high = img.shape[0]
width=img.shape[1]
dim=(int(width/2),int(high/2))

img2 = cv.resize(img,dim)
img3 = myRgb2Gray(img2)

cv.namedWindow('daofeng')
cv.imshow('daofeng',img3)

while 1:
    if cv.waitKey(200)==ord('q'):
        break
cv.destroyAllWindows()

