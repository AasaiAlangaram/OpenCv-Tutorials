import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

fig = cv.imread('chess.jpg')

gray = cv.cvtColor(fig,cv.COLOR_BGR2GRAY)

gray = np.float32(gray)

dst = cv.cornerHarris(gray,2,3,0.04)

# print(dst)

#DILATE IS USED TO INCREASE THE IMAGE WIDTH
dst = cv.dilate(dst,None)

# print(dst)

# https://stackoverflow.com/questions/54720646/what-does-ksize-and-k-mean-in-cornerharris

fig[dst>0.01*dst.max()] = [0,0,255]

cv.imshow('dst',fig)

cv.waitKey(0)

cv.destroyAllWindows()