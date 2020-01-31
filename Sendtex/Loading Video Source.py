import cv2

#capture frames from your webcam
video = cv2.VideoCapture(0)

while True:

    ret , frame = video.read()

    cv2.imshow('Live Streaming',frame)

    # to stop the infinite loop press 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

video.release()

cv2.destroyAllWindows()