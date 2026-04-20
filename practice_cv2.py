import cv2
img = cv2.imread(r"D:\IMG_1385.PNG")
# cv2.imshow("image", img)

# cv2.waitKey(0)
# cv2.destroyWindow

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

_, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
cv2.imshow("image", gray)

cv2.waitKey(0)
cv2.destroyWindow