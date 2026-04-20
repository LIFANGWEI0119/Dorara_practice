#%%
import cv2 #Open Source Computer Vision Library

path = 'C:/Users/Dorara/Desktop/fire_fly.png'
# 最常用的 flag 有以下三種：
# cv2.IMREAD_UNCHANGED: 讀取圖片中的所有 channel，包括透明度
# cv2.IMREAD_GRAYSCALE: 以灰階格式讀取
# cv2.IMREAD_COLOR: 以 RGB 格式讀取，為預設值
img = cv2.imread(path)
cv2.imshow("windows", img)
key = cv2.waitKey()
if key == ord("q"):
   print("exit")
cv2.destroyWindow("windows")

# %%
import matplotlib.pyplot as plt
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
# %%
