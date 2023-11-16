import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Sakam\wp3097243-nancy-jewel-mcdonie-wallpapers.jpg")

height, width = image.shape[:2]

original_points = np.float32([[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]])
transformed_points = np.float32([[50, 50], [width - 100, 100], [10, height - 150], [width - 50, height - 50]])


perspective_matrix = cv2.getPerspectiveTransform(original_points, transformed_points)

perspective_transformed_image = cv2.warpPerspective(image, perspective_matrix, (width, height))

cv2.imshow('Original Image', image)
cv2.imshow('Perspective Transformed Image', perspective_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
