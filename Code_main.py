import cv2
import numpy as np

# Open the webcam
capture = cv2.VideoCapture(0)

# Set the width and height of the frames in the video stream
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Create a window to display the ASCII characters
cv2.namedWindow("ASCII")

while True:
    # Capture frame-by-frame
    ret, frame = capture.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Resize the frame to fit the width of the console
    small = cv2.resize(gray, (80, 60))

    # Create an empty image with the same size as the frame
    ascii_img = np.zeros((60*12, 80*8, 3), np.uint8)

    # Iterate over each pixel in the frame and convert it to an ASCII character
    for i in range(60):
        for j in range(80):
            # Get the pixel value (0-255)
            pixel = small[i][j]

            # Select an ASCII character based on the pixel value
            if pixel > 240:
                char = "@"
            elif pixel > 220:
                char = "X"
            elif pixel > 200:
                char = "$"
            elif pixel > 180:
                char = "&"
            elif pixel > 160:
                char = "#"
            elif pixel > 140:
                char = "+"
            elif pixel > 120:
                char = "*"
            elif pixel > 100:
                char = "o"
            elif pixel > 80:
                char = ";"
            elif pixel > 60:
                char = ":"
            elif pixel > 40:
                char = ","
            elif pixel > 20:
                char = "."
            else:
                char = " "

            # Put the ASCII character on the image
            cv2.putText(ascii_img, char, (j*8, i*12), cv2.FONT_HERSHEY_SIMPLEX, 0.33, (255, 255, 255), 1, cv2.LINE_AA)

    # Display the image with the ASCII characters
    cv2.imshow("ASCII", ascii_img)

    # Wait for the user to press a key
    key = cv2.waitKey(1)
    if key == 27: # Escape key
        break

# Release the webcam
capture.release()

# Destroy the window
cv2.destroyWindow("ASCII")
