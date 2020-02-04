import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

'''
The basic idea of erosion is just like soil erosion only, it erodes away the boundaries of foreground object (Always try to keep foreground in white). 
So what it does? The kernel slides through the image (as in 2D convolution). 
A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).
'''

img = cv.imread('eight.png')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
kernel = np.ones((5,5),np.uint8)
erode = cv.erode(gray,kernel,iterations=1)

cv.imshow('Gray image',gray)
cv.imshow('After apply kernel',erode)

cv.waitKey(0)
cv.destroyAllWindows()

