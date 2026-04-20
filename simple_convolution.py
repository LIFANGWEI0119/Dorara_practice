import numpy as np

# 輸入矩陣 3x3
x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Kernel 2x2
kernel = np.array([[1, 0],
                   [0, -1]])

# 取得輸入尺寸
x_h, x_w = x.shape
k_h, k_w = kernel.shape

# 計算輸出尺寸 (步階 stride=1, 不填充 padding)
out_h = x_h - k_h + 1
out_w = x_w - k_w + 1

# 建立輸出矩陣
output = np.zeros((out_h, out_w))

# 逐位置做卷積
for i in range(out_h):
    for j in range(out_w):
        window = x[i:i+k_h, j:j+k_w]   # 取對應的區塊
        output[i, j] = np.sum(window * kernel)  # element-wise 乘法再相加

print("輸入矩陣：\n", x)
print("Kernel：\n", kernel)
print("卷積結果：\n", output)