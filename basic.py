import cv2 as cv

# img read

# img = cv.imread('./Resources\Photos\cat_large.jpg')
img = cv.imread('./Resources\Photos\park.jpg')
cv.imshow('Park',img)

# grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Park Gray',gray)

# blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Park Blur',blur)

# edge canny
canny = cv.Canny(img, 125, 175)
cv.imshow('canny', canny)

blurCanny = cv.Canny(blur, 125, 175)
cv.imshow('Blur Canny',blurCanny)

# dilate
dilate = cv.dilate(blurCanny, (5,5), iterations=3)
cv.imshow('Dilate',dilate)

# erode
eroded = cv.erode(dilate,(5,5), iterations=3)
cv.imshow('Erode', eroded)

# resize
resize = cv.resize(img, (500,500))
cv.imshow('Resize', resize)

# cropped
cropped = img[100:300,100:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)
