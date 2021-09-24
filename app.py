from skimage.metrics import structural_similarity as compare_ssim
import numpy as np
import cv2

imageA = cv2.imread("1.jpg")
imageB = cv2.imread("2.jpg")

(height_image_1, width_image_1, chanels_image_1) = imageA.shape
(height_image_2, width_image_2, chanels_image_2) = imageB.shape

height = height_image_1 if height_image_1 < height_image_2 else height_image_2
width = width_image_1 if width_image_1 < width_image_2 else width_image_2

image1_resized = cv2.resize(imageA, (width, height), interpolation = cv2.INTER_AREA)
image2_resized = cv2.resize(imageB, (width, height), interpolation = cv2.INTER_AREA)

# # convert the images to grayscale
grayA = cv2.cvtColor(image1_resized, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(image2_resized, cv2.COLOR_BGR2GRAY)

(score, diff) = compare_ssim(grayA, grayB, full=True)

print("SSIM: {:.2f}".format(score*100))