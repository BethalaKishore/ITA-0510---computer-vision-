import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Sakam\bhanu.jpg")

height, width = image.shape[:2]


original_points = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])
transformed_points = np.float32([[50, 50], [width - 100, 100], [50, height - 50]])

affine_matrix = cv2.getAffineTransform(original_points, transformed_points)

affine_transformed_image = cv2.warpAffine(image, affine_matrix, (width, height))

cv2.imshow('Original Image', image)
cv2.imshow('Affine Transformed Image', affine_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
