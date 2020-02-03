import cv2 as cv
import numpy as np

img1 = cv.imread('Lion.jpg')
# img2 = cv.imread('chair.jpg')
img3 = cv.imread('python.png')

# print(img1.shape)
# print(img2.shape)

# add = img1+img2

row,cols,channels = img3.shape
roi = img1[0:row,0:cols]
im32gray = cv.cvtColor(img3,cv.COLOR_BGR2GRAY)

print(img3.shape)
print(roi.shape)

#anything above 23~255 is black because it's threshold binary inversion
ret,mask = cv.threshold(im32gray,230,255,cv.THRESH_BINARY_INV)

#inverse mask black->white & white->black
mask_inv = cv.bitwise_not(mask)

img1_bg = cv.bitwise_and(roi,roi,mask=mask_inv)
img3_fg = cv.bitwise_and(img3,img3,mask = mask )


dst = cv.add(img1_bg,img3_fg)
img1[0:row,0:cols] = dst

cv.imshow('res',img1)

'''
If anyone is having trouble finding images of equivalent size, you can just use the line   
resized = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA) to choose sizes for your images
'''
# cv.imshow('grayimage',im32gray)
cv.imshow('dst',dst)
cv.imshow('img1_bg',img1_bg)
cv.imshow('img3_fg',img3_fg)
cv.imshow('mask',mask)
cv.imshow('mask_inv',mask_inv)
cv.imshow('roi',roi)
cv.imshow('original img3',img3)

# cv.imshow('img1',img1)
# cv.imshow('img2',img2)
# cv.imshow('Added Image',add)

cv.waitKey(0)
cv.destroyAllWindows()