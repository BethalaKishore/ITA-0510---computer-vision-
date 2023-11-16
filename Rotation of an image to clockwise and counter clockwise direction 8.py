import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Sakam\nancy.jpg")

height, width = image.shape[:2]

angle = -90
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow('Original Image', image)
cv2.imshow('Clockwise Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
