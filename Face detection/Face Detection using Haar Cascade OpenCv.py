import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# It capture video from computer camera.
cap = cv2.VideoCapture(0)
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    ret, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.2, 2)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        #  cv2.rectangle(image, start_point, end_point, color(B,G,R), thickness)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Display image
    cv2.imshow('img', img)

    # close once q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
