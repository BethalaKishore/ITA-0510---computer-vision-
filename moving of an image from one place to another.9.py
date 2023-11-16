import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Sakam\nancy.jpg")

height, width = image.shape[:2]

tx = 50  
ty = 30  

translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

translated_image = cv2.warpAffine(image, translation_matrix, (width, height))

cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
