# import necessary modules
import cv2

# create a VideoCapture object
webcam_port = 0
cap = cv2.VideoCapture(webcam_port)

while(True):
    # Capture frame-by-frame
    ret_bool, frame = cap.read()

    # Our operations on the frame come here
    rgbcolor = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('Gray frame',gray)
    cv2.imshow('RGB frame', rgbcolor)
    cv2.imshow('BGR frame', frame)

    # Press Q on keyboard to  exit
    if cv2.waitKey(1) == ord('q'):
        print('Streaming Stopped because of key pressed event')
        break

# When everything done, release the capture
cap.release()
# Closes all the frames
cv2.destroyAllWindows()