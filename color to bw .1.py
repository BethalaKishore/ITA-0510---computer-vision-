import cv2
path=r"C:\Users\Sakam\nancy.jpg"
img=cv2.imread(path)
cv2.imshow("original",img)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale",imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()
