# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 22:34:11 2019

@author: jmbor
"""

import numpy as np 
import cv2
import sys
import imutils
	
imageName = "Image.jpg"

# Initialiation
(h, w) = (None, None)		# initialize frame dimensions tuple
zeros = None				# initialize zeros array


# read image as color
colorimg = cv2.imread(imageName, cv2.IMREAD_COLOR)
grayimg = cv2.imread(imageName, cv2.IMREAD_GRAYSCALE)

# resize the image
colorimg = imutils.resize(colorimg, width=300)
grayimg = imutils.resize(grayimg, width=300)

# store image dimensions
(h, w) = colorimg.shape[:2]

# fill zeros array
zeros = np.zeros((h,w), dtype="uint8")



# split the image into blue, green read color channels
blueimg, greenimg, redimg = cv2.split(colorimg)

# create named windows and position them on screen
cv2.namedWindow('Grayscale')
cv2.moveWindow('Grayscale', 10, 20)
cv2.namedWindow('Red Channel')
cv2.moveWindow('Red Channel', 60+w, 20)
cv2.namedWindow('Green Channel')
cv2.moveWindow('Green Channel', 10, 50+h)
cv2.namedWindow('Blue Channel')
cv2.moveWindow('Blue Channel', 60+w, 50+h)
cv2.namedWindow('Final')
cv2.moveWindow('Final', 2*w+100, 20)

# display channels individually
cv2.imshow('Red Channel', redimg)
cv2.imshow('Green Channel', greenimg)
cv2.imshow('Blue Channel', blueimg)


# merge the channel images into a larger zero filled 3 channel image

redimg   = cv2.merge([zeros, zeros, redimg ])
greenimg = cv2.merge([zeros, greenimg, zeros])
blueimg  = cv2.merge([blueimg, zeros, zeros])

# construct an output image to store all four images
# final image is twice the height, twice the width, 3 color channels
finalimg = np.zeros( (h*2, w*2, 3), dtype="uint8")

# original color image in upper left
finalimg[0:h, 0:w] = colorimg
finalimg[0:h, w:w*2] = redimg           # red image upper right
finalimg[h:h*2, 0:w] = blueimg			# blue image lower left
finalimg[h:h*2, w:w*2] = greenimg 		# green image lower right


# display final image
cv2.imshow('Final', finalimg)

''' waitkey( time in milliseconds)
	function waits for specified milliseconds for a keyboard event. If you
	press any key in that time, the program continues.
	If 0 is passed, it waits indefinitely for a keystroke
'''
print ('press any key to end program')
cv2.waitKey(0)

# free memory
cv2.destroyAllWindows()