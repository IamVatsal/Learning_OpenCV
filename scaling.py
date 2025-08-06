from turtle import width
import cv2 as cv


def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dim = (width,height)
    if scale < 1:
        return cv.resize(frame,dim,interpolation=cv.INTER_AREA)
    elif(scale < 1.5):
        return cv.resize(frame,dim,interpolation=cv.INTER_LINEAR)
    else:
        return cv.resize(frame,dim,interpolation=cv.INTER_CUBIC)
    

def changeRes(width,height):
    # only works for live video
    capture.set(3,width)
    capture.set(4,height)

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
        
    frame_resize = rescaleFrame(frame)
    # frame_resize = rescaleFrame(frame,1.3)
    cv.imshow('Video', frame)
    cv.imshow('Video_resize', frame_resize)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()