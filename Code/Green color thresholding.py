import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# blue = np.uint8([[[255,0,0 ]]])
# hsv_green = cv.cvtColor(blue,cv.COLOR_BGR2HSV)
# print( hsv_green )

img = cv.imread('rgb.jpg')

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([50,50,50])
upper_blue = np.array([255,255,255])

# Threshold the HSV image to get only blue colors
mask = cv.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv.bitwise_and(img,img, mask= mask)

# th3 = cv.adaptiveThreshold(mask,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,1)
# ret,th1 = cv.threshold(img,130,255,cv.THRESH_BINARY)

# cv.imshow('hsv image',hsv)
# cv.imshow('mask image',mask)
# cv.imshow('res',res)
# cv.imshow(' original image',img)
# cv.imshow('Adaptive Threshold',th1)

images = [img,hsv,mask,res]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], 'gray')

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()