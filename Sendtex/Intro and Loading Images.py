import cv2
import numpy as np
import matplotlib.pyplot as plt

#Read Image and convert into GrayScale Image
lion = cv2.imread('Lion.jpg',cv2.IMREAD_GRAYSCALE)

#output image
cv2.imshow('Singam',lion)

#Wait until some key press
cv2.waitKey(0)
cv2.destroyAllWindows()