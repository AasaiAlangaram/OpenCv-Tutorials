import cv2
import numpy as np

video = cv2.VideoCapture(0)

'''
This time we create a VideoWriter object. We should specify the output file name (eg: output.avi).
Then we should specify the FourCC code (details in next paragraph). 
Then number of frames per second (fps) and frame size should be passed. And the last one is the isColor flag. 
If it is True, the encoder expect color frame, otherwise it works with grayscale frame.
'''

#Define the videowriter object and codec
#FourCC is a 4-byte code used to specify the video codec
video_cc = cv2.VideoWriter_fourcc(*'XVID')

#20.0 - Frame per second(fps)
#640,480 - frame size

out = cv2.VideoWriter('output.avi',video_cc,20.0,(640,480))

while True:

    ret, frame = video.read()

    if not ret:
        print('frames not received')
        break

    #flip down
    #frame = cv2.flip(frame,0)

    out.write(frame)
    cv2.imshow('ouput',frame)

    if cv2.waitKey(1) == ord('q'):
        print('Program terminated')
        break

video.release()
out.release()
cv2.destroyAllWindows()