import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
blank[200:300,300:400] = 0,255,0
cv.imshow('green',blank)

# 2. Draw a Rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2,),(0,0,255),thickness=1)
cv.imshow('Rectangle', blank)

# 3. Draw A circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2,),50,(255,0,0),thickness=5)
cv.imshow('circle',blank)

# 4. Draw a line
cv.line(blank,(100,200),(blank.shape[1]//2,blank.shape[0]//2,),(255,255,255),thickness=5)
cv.imshow('Line',blank)

# 5. Write text
cv.putText(blank,'Hello I am Vatsal',(100,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text',blank)

cv.waitKey(0)