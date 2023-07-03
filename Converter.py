## This Program will convert all images of Input_Folder into RGB,Grayscale,Threashold variant and will store it in Output_Folder

import os
import cv2
import numpy as np

for i in os.listdir('Input_Folder'):
    if i.endswith((".jpg", ".jpeg", ".png")):
        file_path = os.path.join('Input_Folder', i)
        # Load an image 
    else:
        print('invalid image format found in Input_Folder')
        break
    img = cv2.imread(file_path)

    # Convert the image from BGR to RGB
    RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Apply thresholding
    _, threshold_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)

    # Save the processed image to a file
    cv2.imwrite(f"Output_Folder/RGB_{i}.jpg", RGB_img)
    cv2.imwrite(f"Output_Folder/Black_White_{i}.jpg", threshold_img)
    cv2.imwrite(f"Output_Folder/Grayscale_{i}.jpg", gray_img)

    # Destroy all windows
    cv2.destroyAllWindows()
