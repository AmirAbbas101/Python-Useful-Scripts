import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

# Function to display an image using matplotlib
def display_image(image, title, cmap=None):
    plt.figure()
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.axis('off') # Hide axes
    plt.show()

# Read the JPG image
input_image = cv2.imread('inputImage.jpg') # Replace with your image filename

# Display the original image
display_image(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB), 'Original Image')

# Convert the image to grayscale
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
display_image(gray_image, 'Grayscale Image', cmap='gray')

# Convert the grayscale image to a binary image using a fixed threshold
threshold = 0.6 * 255  # Adjust this value if needed, scale from 0-255
_, bw_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)

# Alternatively, use Otsu's method to determine the threshold automatically
_, bw_image_otsu = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display the black and white (binary) image with fixed threshold
display_image(bw_image, 'Black and White Image (Fixed Threshold)', cmap='gray')

# Display the black and white (binary) image with Otsu's method
display_image(bw_image_otsu, 'Black and White Image (Otsu\'s Method)', cmap='gray')
