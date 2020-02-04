import cv2 as cv
import numpy as np

'''
Usually in image processing, after removing white noise in image using erode use dilute to increase image width
it is very useful in combining broken images.
'''

image = cv.imread('j.png')
image1 = cv.imread('opening.png')
image2 = cv.imread('closing.png')
image3 = cv.imread('gradient.png')

kernel = np.ones((5,5),np.uint8)

dilate = cv.dilate(image,kernel,iterations=2)

#opening is just a another name of erosion followed by dilution. It is useful in removing noise.
opening = cv.morphologyEx(image1,cv.MORPH_OPEN,kernel)
#closing is reverse of opening
closing = cv.morphologyEx(image2,cv.MORPH_CLOSE,kernel)
#it is difference between input and opening of image
gradient = cv.morphologyEx(image3,cv.MORPH_GRADIENT,kernel)

cv.imshow('Original Image',image)
cv.imshow('Dilated image',dilate)
cv.imshow('Opening Image',opening)
cv.imshow('closing image',closing)
cv.imshow('Gradient Image',gradient)

cv.waitKey(0)
cv.destroyAllWindows()