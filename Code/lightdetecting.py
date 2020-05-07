#import packages
import cv2
import imutils as im
import argparse
import numpy as np

'''
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())
# load the image, convert it to grayscale, blur it slightly,
# and threshold it
image = cv2.imread(args["image"])
'''

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	# return the edged image
	return edged


# Read the image file
input = 'drl.jpg'
image = cv2.imread(input)

# Resize the image - change width to 500
newwidth = 500
image = im.resize(image, width=newwidth)

# RGB to Gray scale conversion
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray, 200,255,cv2.THRESH_BINARY)

filter_img = cv2.GaussianBlur(thresh,(9,9),0)

d, sigmaColor, sigmaSpace = 10,15,15
filtered_img = cv2.bilateralFilter(thresh, d, sigmaColor, sigmaSpace)

# Find Edges of the grayscale image
# cannyedged = cv2.Canny(filtered_img, 220, 255)
cannyedged = auto_canny(filtered_img)

kernel = np.ones((2,2),np.uint8)
erosion = cv2.dilate(cannyedged,kernel,iterations = 1)

opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
# Find contours based on Edges
cnts,hir = cv2.findContours(opening.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

print('No of contours found:',len(cnts))

cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
NumberPlateCnt = None
# loop over our contours to find the best possible approximate contour of number plate
count = 0
for c in cnts:
        peri = cv2.arcLength(c, True)
        # print(peri)
        approx = cv2.approxPolyDP(c, 0.01 * peri, True)
        print('-----',peri,len(approx))
        # if len(approx) == 15:  # Select the contour with 4 corners
        #     print(approx)
        #     NumberPlateCnt = approx #This is our approx Number Plate Contour
        #     break

# Display the original image
# cv2.imshow("Input Image", image)
# Display Grayscale image
# cv2.imshow("Gray scale Image", gray)
# Display threshold image
# cv2.imshow("Threshold Image", thresh)
# Display Filtered image
# cv2.imshow("Filtered Image", filter_img)
# Display Bilateral Filtered image
# cv2.imshow("Bilateral Filter",filtered_img)
cv2.imshow("Canny Edged dilated",erosion)
cv2.imshow("Canny Edged opening",opening)
cv2.imshow("Canny Edged ",cannyedged)
cv2.drawContours(image, cnts[0], -1, (0,255,0), 2)
cv2.imshow("Output0", image)
cv2.drawContours(image, cnts[1], -1, (0,255,0), 2)
cv2.imshow("Output1", image)
cv2.drawContours(image, cnts[2], -1, (0,255,0), 2)
cv2.imshow("Output2", image)
cv2.drawContours(image, cnts[3], -1, (0,255,0), 2)
cv2.imshow("Output3", image)
cv2.drawContours(image, cnts[4], -1, (0,255,0), 2)
cv2.imshow("Output4", image)
# Wait until user press any key
cv2.waitKey(0) #Wait for user input before closing the images displayed