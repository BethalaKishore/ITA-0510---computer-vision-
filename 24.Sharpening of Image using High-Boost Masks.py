import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Sakam\wp3097243-nancy-jewel-mcdonie-wallpapers.jpg")


kernel_size = 3  
sigma = 1.0      
gaussian_kernel = cv2.getGaussianKernel(kernel_size, sigma)
gaussian_kernel_2d = np.outer(gaussian_kernel, gaussian_kernel.transpose())


blurred = cv2.filter2D(image, -1, gaussian_kernel_2d)


boost_factor = 1.5  
high_boost_mask = image - blurred * boost_factor


sharpened = image + high_boost_mask


cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
