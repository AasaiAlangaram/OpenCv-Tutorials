#import cv2 module as cv
import cv2 as cv

#import numpy module
# import numpy as np

#cv.imread() function is used for load images
color_image = cv.imread('Lion.jpg',1)
gray_image = cv.imread('Lion.jpg',0)

#cv.imshow() is used for display an image First argument is a window name which is a string.
# second argument is our image
cv.imshow('color_image',color_image)
cv.imshow('gray_image',gray_image)

# wait until user press any key
cv.waitKey(0)

# close all windows
cv.destroyAllWindows()




