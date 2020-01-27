# OpenCv-Tutorials
`Computer Vision OpenCV Tutorial`

[1.Face Detection Using Haar cascade](https://github.com/AasaiAlangaram/OpenCv-Tutorials/blob/master/Face%20detection/Face%20Detection%20using%20Haar%20Cascade%20OpenCv.py)\
Here You can see [Output Image](https://github.com/AasaiAlangaram/OpenCv-Tutorials/blob/master/Images/Face%20Detection%20Haar%20Cascade.PNG)

**Program Explanation:**\
1.Install OpenCV- >`pip install opencv-python`\
2.[Download Trained classifier XML File]( https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml)\
3.To capture a video, you need to create a VideoCapture object.Its argument can be either the device index or the name of a video file.\
4.cap.read() returns a bool (True/False) and frame. If frame is read correctly, it will be True.\
5.Convert BGR image into Gray Image\
6.cv2.CascadeClassifier.detectMultiScale(image[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize]]]]]) \
`image - input image
scaleafactor - Parameter specifying how much the image size is reduced at each image scale.
minNeighbors : Parameter specifying how many neighbors each candidate rectangle should have to retain it. This parameter will affect the quality of the detected faces: higher value results in less detections but with higher quality.
flags : Parameter with the same meaning for an old cascade as in the function cvHaarDetectObjects. It is not used for a new cascade.
minSize : Minimum possible object size. Objects smaller than that are ignored.
maxSize : Maximum possible object size. Objects larger than that are ignored.
If faces are found, it returns the positions of detected faces as Rect(x,y,w,h).`\
7.cv2.rectangle(image, start_point, end_point, color, thickness)\
8.Program run until key Q is pressed\
9.Destroy all windows\
10.Release cap object.
