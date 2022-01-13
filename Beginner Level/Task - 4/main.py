# LetsGrowMore
# Task 4: Image to Pencil Sketch with Python
# Done By: Yash Rai
# Importing the libraries: cv2 and matplotlib

import cv2
import matplotlib.pyplot as plt

# Reading the image
img = cv2.imread('Spidey.jpg')

# Displaying the image
plt.imshow(img)

# Converting the image to grayscale image
gray_scale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Inverting the grayscale image
inverted_gray_scale_img = cv2.bitwise_not(gray_scale_img)

# Blurring the inverted grayscale image
blurred_img = cv2.GaussianBlur(inverted_gray_scale_img, (21, 21), 0)

# Inverting the blurred image
inverted_blurred_img = cv2.bitwise_not(blurred_img)

# Converting the image to pencil sketch
sketch = cv2.divide(gray_scale_img, inverted_blurred_img, scale=256.0)
cv2.imwrite("Sketch_Spidey.png", sketch)
