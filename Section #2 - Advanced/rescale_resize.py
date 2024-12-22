#pylint:disable=no-member

import cv2 as cv

# img = cv.imread('../Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    # Live video
    capture.set(3,width)    # doubt-only works for live videos - so photos/video files ko is method se resize nai kar sakte
    capture.set(4,height)
    
# Reading Videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# Now, we usually resize and rescale video files and images to prevent computational strain
enerally, it's always best practice to downscale or
change the width and height of your video files to a smaller value than the original
dimensions. The reason for this is because while most cameras your webcam included, do
not support going higher than its maximum capability. So for example, if a camera shoots
in 720 P, chances are it's not going to be able to shoot in 1080 P or higher. So to rescale
