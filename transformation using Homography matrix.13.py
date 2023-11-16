import cv2
import numpy as np

image1 = cv2.imread(r"C:\Users\Sakam\wp3097245-nancy-jewel-mcdonie-wallpapers.jpg")
image2 = cv2.imread(r"C:\Users\Sakam\wp3097243-nancy-jewel-mcdonie-wallpapers.jpg")
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
points_image1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
points_image2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

homography_matrix, _ = cv2.findHomography(points_image1, points_image2)


transformed_image = cv2.warpPerspective(image1, homography_matrix, (image1.shape[1], image1.shape[0]))


cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Transformed Image 1', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
