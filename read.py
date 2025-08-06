import cv2 as cv

#img read

# img = cv.imread('./Resources\Photos\cat_large.jpg')
# img = cv.imread('./Resources\Photos\cat.jpg')

# cv.imshow('Cat',img)

# cv.waitKey(0)

# reading videos
try:
    capture = cv.VideoCapture('./Resources/Videos/dog.mp4')
    # Check if video opened successfully
    if not capture.isOpened():
        print('Error: Could not open video file.')
        exit()
        
except Exception as err:
    print(f'Error: {err}')
    exit()

while True:
    isTrue, frame = capture.read()
    
    # Check if frame was read successfully
    if not isTrue:
        print('Video ended or failed to read frame.')
        break
        
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()  # Added parentheses to actually call the function
