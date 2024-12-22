#pylint:disable=no-member

# Now contours are basically the boundaries of objects, the line or curve that joins the
# continuous points along the boundary of an object. Now from a mathematical point of view, 
# they're not the same as edges.

import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)
# another method to draw contour
# The cv.threshold() function is used to apply a threshold to an image, converting it into a binary image where pixel values are either 0 (black) or 255 (white) based on a specified threshold value. It's typically used for image segmentation, where objects of interest (based on intensity or color) are separated from the background.

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)



# A contour is a curve joining all the continuous points along a boundary that have the same color or intensity.
'''
cv.RETR_LIST:
This is the contour retrieval mode. There are several options, and cv.RETR_LIST retrieves all contours in the image without establishing any hierarchical relationships (i.e., no parent-child relationships between contours).
cv.RETR_EXTERNAL: Retrieves only the outermost contours (ignores nested contours).
cv.RETR_LIST: Retrieves all contours without establishing any hierarchy.
cv.RETR_TREE: Retrieves all contours and creates a full hierarchy of nested contours.
cv.RETR_CC: Retrieves all contours and organizes them into a connected component tree.

cv.CHAIN_APPROX_SIMPLE:
This is the contour approximation method. It simplifies the contour by removing points that are not necessary, retaining only the end points of straight lines. This reduces the number of points in the contour representation.
cv.CHAIN_APPROX_SIMPLE: Only stores the end points of the contour segments (saves memory and reduces the number of points).
cv.CHAIN_APPROX_NONE: Stores all points along the contour (more points, but higher accuracy).
'''
                                                           
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
