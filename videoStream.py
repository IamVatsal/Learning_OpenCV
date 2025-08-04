import cv2

# Open the default camera (usually camera 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # If frame is not read correctly, break
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Display the frame in a window
    cv2.imshow('Camera Feed', frame)

    # Break loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
# End of videoStream.py