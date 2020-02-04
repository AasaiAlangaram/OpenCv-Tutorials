import cv2 as cv
import numpy as np

image = cv.imread('calender.png')

laplacian = cv.Laplacian(image,cv.CV_64F)
#horizontal
sobelx = cv.Sobel(image,cv.CV_64F,1,0,ksize=5)
#vertical
sobely = cv.Sobel(image,cv.CV_64F,0,1,ksize=5)

cv.imshow('Original',image)
cv.imshow('laplacian',laplacian)
cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)

cv.waitKey(0)
cv.destroyAllWindows()
