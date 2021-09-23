import cv2
import numpy as np

img1 = cv2.imread('image_1.png', 0)
img2 = cv2.imread('image_2.jpeg', 0)

#--- take the absolute difference of the images ---
res = cv2.absdiff(img1, img2)

#--- convert the result to integer type ---
res = res.astype(np.uint8)

#--- find percentage difference based on number of pixels that are not zero ---
percentage = (np.count_nonzero(res) * 100)/ res.size

print(percentage)