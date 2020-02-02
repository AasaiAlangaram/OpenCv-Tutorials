import cv2 as cv
import numpy as np

img = cv.imread('bookpage.jpg')
grayimg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

ret,threshold = cv.threshold(img,12,255,cv.THRESH_BINARY)
print(ret)
ret2,threshold2 = cv.threshold(grayimg,20,255,cv.THRESH_BINARY)
print(ret2)
gaus = cv.adaptiveThreshold(grayimg,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,155,1)

cv.imshow('Gaus',gaus)
cv.imshow('Threshold-gray-image',threshold2)
cv.imshow('Threshold-color-image',threshold)
cv.imshow('Gray Image',grayimg)
cv.imshow('Bookpage',img)
cv.waitKey(0)
cv.destroyAllWindows()