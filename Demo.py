## This Program will show RGB,Grayscale,Threashold variant of given image and will store it in output folder

import cv2
import numpy as np


# Load an image (Insert path to desired image for processing)
img = cv2.imread("Input_Folder/siarhei-palishchuk-hgiby6qxvpc-unsplash.jpg")

# Convert the image from BGR to RGB
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Apply thresholding
_, threshold_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)

# Display the original image
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL) #Create Named Window
cv2.imshow("Original Image", img)  #Display
cv2.setWindowProperty("Original Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) #Make the window fullscreen
cv2.waitKey(0) # Wait until a key is pressed

# Display the RGB image
cv2.namedWindow('RGB Image', cv2.WINDOW_NORMAL)
cv2.imshow("RGB Image", RGB_img)
cv2.setWindowProperty("RGB Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.waitKey(0)

# Display the grayscale image
cv2.namedWindow('Grayscale Image', cv2.WINDOW_NORMAL)
cv2.imshow("Grayscale Image", gray_img)
cv2.setWindowProperty("Grayscale Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.waitKey(0)

# Display the thresholded image
cv2.namedWindow('Thresholded Image', cv2.WINDOW_NORMAL)
cv2.imshow("Thresholded Image", threshold_img)
cv2.setWindowProperty("Thresholded Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.waitKey(0)

# Save the processed image to a file
cv2.imwrite("Output_Folder/RGB_output.jpg", RGB_img)
cv2.imwrite("Output_Folder/Threshold_output.jpg", threshold_img)
cv2.imwrite("Output_Folder/Grayscale_output.jpg", gray_img)

# Destroy all windows
cv2.destroyAllWindows()
