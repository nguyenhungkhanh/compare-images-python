from skimage.metrics import structural_similarity as compare_ssim
import numpy as np
import cv2

# # load the two input images
# imageA = cv2.imread("200x200_(30).png")
# imageB = cv2.imread("12056.png")

imageA = cv2.imread("1.jpg")
imageB = cv2.imread("2.jpg")

(height_image_1, with_image_1, chanels_image_1) = imageA.shape
(height_image_2, width_image_2, chanels_image_2) = imageB.shape

resized = cv2.resize(imageA, (width_image_2, height_image_2), interpolation = cv2.INTER_AREA)
resized.show()

# # convert the images to grayscale
# grayA = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
# grayB = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# (score, diff) = compare_ssim(grayA, grayB, full=True)

# print("SSIM: {:.2f}".format(score*100))