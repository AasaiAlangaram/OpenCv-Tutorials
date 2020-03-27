import cv2

# To use a image file as input
img_path = 'C:\\Users\\aasai\\Desktop\\TheHobbyists - Opencv Tutorials\\27-03-2020\\aasai.jpeg'

# load our image and convert it to grayscale
image = cv2.imread(img_path)

print(image.shape)
image = cv2.resize(image,(450,600))
# print('row,column,no.of.channels',image.shape)

#convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load the face detector and detect faces in the image
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

rects = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=8)
print(rects)
print("[INFO] detected {} faces".format(len(rects)))

# loop over the bounding boxes and draw a rectangle around each face
for (x, y, w, h) in rects:
	cv2.rectangle(image, (x, y), (x + w, y + h), (0,255,0), 2)

# show the detected faces
cv2.imshow("Faces", image)
cv2.waitKey(0)
