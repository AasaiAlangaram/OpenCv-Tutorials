import cv2 as cv
import numpy as np

img = cv.imread('Lion.jpg')

#print(img)
print(img.shape)

img[50:100,150:200] = [0,0,0]

#Access image pixel value
pixel = img[100,200]
print('pixel value',pixel)

#acess img data type
print(img.dtype)

#access red pixel value from 10 row and 10 column
print(img.item(10,10,2))


#ROI
eye = img[200:400,300:500]
img[0:200,0:200] = eye


#Seperate image channels
blue = img[:,:,0]
green = img[:,:,1]
Red = img[:,:,2]

cv.imshow('Blue Lion',blue)
cv.imshow('Green Lion',green)
cv.imshow('Red Lion',Red)

cv.imshow('Lion',img)
cv.waitKey(0)
cv.destroyAllWindows()
