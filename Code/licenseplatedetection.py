import cv2
import imutils as im

# Read the image file
input = 'car5.jpg'
image = cv2.imread(input)

# Resize the image - change width to 500
newwidth = 500
image = im.resize(image, width=newwidth)

# RGB to Gray scale conversion
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Noise removal with iterative bilateral filter(removes noise while preserving edges)
d, sigmaColor, sigmaSpace = 10,15,15
filtered_img = cv2.bilateralFilter(gray, d, sigmaColor, sigmaSpace)

# Find Edges of the grayscale image
edged = cv2.Canny(filtered_img, 170, 200)

# Find contours based on Edges
cnts,hir = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
NumberPlateCnt = None
# print('counts:{}'.format(cnts))
print(len(cnts))
# cnts = im.grab_contours(cnts)

# loop over our contours to find the best possible approximate contour of number plate
count = 0
for c in cnts:
        peri = cv2.arcLength(c, True)
        # print(peri)
        approx = cv2.approxPolyDP(c, 0.01 * peri, True)
        # print('-----',approx)
        if len(approx) == 5:  # Select the contour with 4 corners
            print(approx)
            NumberPlateCnt = approx #This is our approx Number Plate Contour
            break

# Display the original image
# cv2.imshow("Input Image", image)
# Display Grayscale image
# cv2.imshow("Gray scale Image", gray)
# Display Filtered image
# cv2.imshow("After Applying Bilateral Filter", filtered_img)
# Display Canny Image
# cv2.imshow("After Canny Edges", edged)
# Drawing the selected contour on the original image
cv2.drawContours(image, cnts[0], -1, (0,255,0), 3)
cv2.imshow("Output0", image)
cv2.drawContours(image, cnts[1], -1, (0,255,0), 3)
cv2.imshow("Output1", image)
cv2.drawContours(image, cnts[2], -1, (0,255,0), 3)
cv2.imshow("Output2", image)
cv2.drawContours(image, cnts[3], -1, (0,255,0), 3)
cv2.imshow("Output3", image)
cv2.drawContours(image, cnts[4], -1, (0,255,0), 3)
cv2.imshow("Output4", image)

cv2.waitKey(0) #Wait for user input before closing the images displayed