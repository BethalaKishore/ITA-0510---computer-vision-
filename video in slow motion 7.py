import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
img = cv2.imread("E:/Computer Vision/computer vision input and output/7.scaling an image.jpeg")
cv2.imshow("original image",img)
cv2.waitKey(0)
img = cv2.resize(img,(600,600))
cv2.imshow(r"C:\Users\Sakam\Don.mp4",img)
cv2.waitKey(0)
