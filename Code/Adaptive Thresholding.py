import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('bookpage.jpg',0)

ret,th1 = cv.threshold(img,12,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,1)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,1)

# cv.imshow('original',img)
# cv.imshow('threshold1',th1)
# cv.imshow('threshold2',th2)
# cv.imshow('threshold3',th3)

title = ['original','threshold1','threshold2','threshold3']
images = [img,th1,th2,th3]

for i in range(4):
    plt.title(title[i])
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], 'gray')

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()