#color image to grey scale image
import numpy as np
import cv2

# Load the color image
img = cv2.imread('img1.jpg')

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_img)

# Wait for a key press and close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()

print(img.shape)
print(img[:,:,0])