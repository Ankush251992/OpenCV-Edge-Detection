# Code Depot Edge Detector
# Author: Ankush
# Patreon: https://www.patreon.com/CodeDepot

# This script demonstrates the use of the Canny edge detection algorithm using OpenCV.

# =================== Import Dependencies ===================
# USAGE
# python edge_detector_with_comments.py

# Import standard libraries
import argparse
import cv2


# =================== Preprocessing ===================
# Load the image, convert it to grayscale, and apply Gaussian blur for noise reduction 
image = cv2.imread("images/Canadian_1_and_2_dollar_coins.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# =================== Display Images ===================
# Show the original and blurred images for comparison
cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)

# =================== Edge Detection ===================
# Compute edge maps with varying thresholds ('wide', 'mid-range', 'tight') using the Canny algorithm
# using the Canny edge detector
wide = cv2.Canny(blurred, 10, 200)
mid = cv2.Canny(blurred, 30, 150)
tight = cv2.Canny(blurred, 240, 250)

# =================== Display Edge Maps ===================
# Show the computed edge maps
cv2.imshow("Wide Edge Map", wide)
cv2.imshow("Mid Edge Map", mid)
cv2.imshow("Tight Edge Map", tight)
cv2.waitKey(0)