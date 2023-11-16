import cv2

image_path = r"C:\Users\Sakam\bhanu.jpg"  
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  

edges = cv2.Canny(image, 100, 200)  
cv2.imshow('Original Image', image)
cv2.imshow('Edge-detected Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
