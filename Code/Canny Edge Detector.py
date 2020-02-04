import cv2 as cv
import numpy as np

img = cv.imread('horse.jpg')

canny = cv.Canny(img,200,300)

cv.imshow('Original',img)
cv.imshow('canny',canny)

cv.waitKey(0)
cv.destroyAllWindows()