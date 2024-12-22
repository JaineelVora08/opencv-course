#pylint:disable=no-member

import cv2 as cv

# Read in an image
img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur - This reduces the high-frequency noise and detail in the image, resulting in a smoother image with softened edges.
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# The lower threshold is used to identify weak edges in the image. If a pixel’s gradient value is greater than this threshold, the pixel is considered to be part of an edge, but it’s not necessarily a strong edge. These weak edges will only be kept if they are connected to strong edges.
# The upper threshold is used to identify strong edges. If a pixel’s gradient value is greater than the upper threshold, it is immediately considered a strong edge. These strong edges will be kept, regardless of their connectivity to other pixels.

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)
'''
Dilation is a morphological transformation that enlarges the white regions (foreground) in a binary or grayscale image. It is particularly useful for tasks like:
Increasing the number of iterations will dilate the image further, expanding the white regions.
The kernel slides over each pixel in the image. For each position of the kernel:

The kernel's center is aligned with a pixel in the image.
The pixel in the output image at the center of the kernel is determined by the maximum value of all pixels under the kernel.
In the case of a binary image, the pixel value in the center of the output image becomes 1 if at least one of the pixels in the kernel region is 1 (foreground or white pixel), otherwise, it remains 0.
Effect on Image:

Expansion of white regions: The white areas (foreground) in the image get expanded because the kernel looks for the maximum pixel value in the area it covers.
Filling gaps: Small gaps between objects that are surrounded by white pixels will get filled.
Growth of boundaries: The boundaries of white regions will grow, effectively enlarging objects.

blur karne se edge detection kam??
'''

# Eroding - apply an erosion operation to an image that has already been dilated. 
# so same factor-kernel,iterations se back to original image?? 
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)
'''
While dilation enlarges bright areas in a binary or grayscale image, erosion shrinks bright areas (foreground) and expands dark areas (background). It works by sliding a kernel over the image and replacing the pixel value at the kernel's center with the minimum pixel value in the region covered by the kernel.
In binary images, if the kernel is a 3x3 matrix, a pixel in the output will be 1 if all the pixels in the kernel region are 1, and 0 otherwise. This effectively removes small details or noise from the foreground.

Effect of Erosion on a Dilated Image:
Dilated Image: The dilated image has enlarged white regions (foreground) and potentially filled gaps between white regions. Dilation would have expanded boundaries.
After Erosion: Applying erosion to this dilated image shrinks the white regions back. The boundaries of the foreground objects will be reduced, and small objects or noise introduced by dilation may be removed or reduced in size.
Iterations: With iterations=3, the foreground shrinks more dramatically with each pass, which can lead to a significant reduction in the size of the objects.
'''


# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
