#pylint:disable=no-member

import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')
# capture is instance of videocap class

while True:
    isTrue, frame = capture.read()
    
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

# videowriter was to store, sirf display ke liye itna hi

capture.release()
cv.destroyAllWindows()

# after vid is over a negative 215 assertion failed error. Now if you ever get
# an error like this negative 215 assertion failed. This would mean in almost all cases
# is that open CV could not find a media file at that particular location that you specified.
# 1. video khatam so no more frames found
# 2. no such file exists
