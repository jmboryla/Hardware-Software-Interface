# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:13:58 2019

@author: jmbor
"""

#Inport libraries for use in the program
import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

#Import video writing resources
fourcc =  cv2.VideoWriter_fourcc(*'XVID')
original = cv2.VideoWriter('jonathan_boryla_lab4.avi',fourcc, 30.0, (1280,960))

while(1):
    ret, frame = cap.read()
    #While there are frames to read, the loop continues
    if ret == True: 
        (h, w) = frame.shape[:2]
        zeros = np.zeros((h,w), dtype="uint8")
        
        #Convert image to Canny edge detection image
        cannyimg= np.zeros((h,w,3), dtype="uint8")
        canny = cv2.Canny(frame,100,150)
        cannyimg  = cv2.merge([canny, canny, canny])
        
        #Convert image to gray
        grayimg=np.zeros((h,w,3), dtype="uint8")
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        grayimg = cv2.merge([gray,gray,gray])
        
        #Convert image to RGB image
        RGBimg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        #Create empty array to fill with converted images
        finalimg = np.zeros( (h*2, w*2, 3), dtype="uint8")
        
        #Write text to individual frames
        cv2.putText(frame,"Original", (360,150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255))
        cv2.putText(grayimg,"Gray", (400,150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255))
        cv2.putText(cannyimg,"Canny", (360,150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255))
        cv2.putText(RGBimg,"RGB", (400,150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255))
        

        #Fill final image with seperate frames of the original image
        finalimg[0:h, 0:w] = frame          # upper left
        finalimg[0:h, w:w*2] = cannyimg      # upper right
        finalimg[h:h*2, 0:w] = RGBimg		# lower left
        finalimg[h:h*2, w:w*2] = grayimg     # Lower right

        #Display final image
        original.write(finalimg)
        cv2.imshow('frame', finalimg)
        
        #Wait for user to press "Esc" key ot exit
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break
#Realease camera resources
cap.release()
original.release()
cv2.destroyAllWindows()

#Unnecessary section of image writing
image = cv2.VideoCapture(0)
s, im = image.read() 


graypic = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
graypic = cv2.merge([graypic,graypic,graypic])
cv2.putText(graypic,"Gray", (400,150), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255))
cv2.imwrite("gray.jpg", graypic)

cannypic = cv2.Canny(im, 10,250)
cannypic  = cv2.merge([cannypic, cannypic, cannypic])
cv2.putText(cannypic,"Canny", (360,150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255))
cv2.imwrite("canny.jpg", cannypic)

rgbpic = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
cv2.putText(rgbpic,"RGB", (400,150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255))
cv2.imwrite("rgb.jpg", rgbpic)

#cv2.putText(im,"Original", (360,150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255))
cv2.imwrite("Image.jpg", im)


finalpic = np.zeros( (h*2, w*2, 3), dtype="uint8")
finalpic[0:h, 0:w] = im          # upper left
finalpic[0:h, w:w*2] = cannypic      # upper right
finalpic[h:h*2, 0:w] = rgbpic		# lower left
finalpic[h:h*2, w:w*2] = graypic     # Lower right
cv2.imwrite("final.jpg", finalpic)
image.release()