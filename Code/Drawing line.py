import cv2 as cv
import numpy as np

image = cv.imread('Lion.jpg')

#draw line
#cv.line(image,(0,0),(150,150),(255,0,0),5)

#draw rectangle
cv.rectangle(image,(100,200),(600,500),(0,255,0),5)

#draw circle
cv.circle(image,(350,350),50,(255,0,0),-1)

#display font in image
font = cv.FONT_HERSHEY_COMPLEX
cv.putText(image,"It'sLion",(0,130),font,1,(0,0,255),2,cv.LINE_AA)

cv.imshow('Output',image)

cv.waitKey(0)

cv.destroyAllWindows()