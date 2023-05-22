# D:\8th sem\FaceRecognition\Resources\BackgroundImage.jpeg

# this is genrating the output

import cv2

# Read the image
img = cv2.imread("D:\8th sem\FaceRecognition\Resources\BackgroundImage.jpeg")

# Initialize the video capture object for the webcam
cap = cv2.VideoCapture(0)

# Define the region where you want to overlay the webcam frame
y_offset = 44
x_offset = 800

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Resize the frame to match the size of the region where you want to overlay it
    resized_frame = cv2.resize(frame, (img.shape[1] - x_offset, img.shape[0] - y_offset))

    # Overlay the frame onto the image
    img[y_offset:y_offset+resized_frame.shape[0], x_offset:x_offset+resized_frame.shape[1]] = resized_frame

    # Resize the image to half its original size
    resized_img = cv2.resize(img, None, fx=0.5, fy=0.5)

    # Show the resulting image
    cv2.imshow("Output", resized_img)

    # Check if the user has pressed the 'q' key to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
