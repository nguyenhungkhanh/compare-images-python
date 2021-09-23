import cv2
import numpy as np

dst_size = (256, 512)
screen1 = cv2.resize(cv2.imread(r'image_1.png'), dst_size)
screen2 = cv2.resize(cv2.imread(r'image_2.jpeg'), dst_size)

# diff = abs(screen1.astype(float) - screen2.astype(float)).astype(np.uint8)

err = np.sum((screen1.astype(float) - screen2.astype(float)) ** 2)
err /= float(screen1.shape[0] * screen1.shape[1])

print(err)

# cat_image = np.concatenate([screen1, screen2, diff], axis=1)

# cv2.imwrite('screeen_cat.png', cat_image)