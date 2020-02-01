import cv2

#capture frames from your webcam
video = cv2.VideoCapture(0)

#load example
# cap = cv.VideoCapture('vtest.avi')

if not video.isOpened():
    print('Cannot Open Camera')
    exit()


while True:

    ret , frame = video.read()

    #if frame is read correctly ret is true
    if not ret:
        print("Can't Receive Frame...Exiting")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    hls = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

    cv2.imshow('BGR Image',frame)
    cv2.imshow('Gray Image',gray)
    cv2.imshow('HSV Image',hsv)
    cv2.imshow('HLS Image',hls)
    cv2.imshow('LAB Image', lab)

    # to stop the infinite loop press 'q'
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    if cv2.waitKey(1) == ord('q'):
        break

video.release()

cv2.destroyAllWindows()