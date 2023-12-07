# 轮廓拟合
# 拟合是指将平面上的一系列点，用一条光滑的曲线连接在一起。
import cv2

shape2 = cv2.imread('1\\5.png')
gray = cv2.cvtColor(shape2, cv2.COLOR_BGR2GRAY)  # 转换为单通道灰度图像
t, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  # 转换为二值图像
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  # 判断图像边缘，cv2.CHAIN_APPROX_SIMPLE
print(type(contours[0]))
print(contours[0])
print("--------------------")
# import numpy as np
# 下面这个arr可以替代contours[0]
# # 定义一个ndarray数组
# arr = np.array([[[63, 283],], [[63, 408]], [[191, 408]], [[191, 284]], [[190, 283]]])
# print("--------------------")


x, y, w, h = cv2.boundingRect(contours[0])  # 获取第一个轮廓最小矩形边框，记录了坐标，宽和高
cv2.rectangle(shape2, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 绘制矩形

cv2.imshow("shape2", shape2)

cv2.waitKey()
cv2.destroyAllWindows()

# +++++++++++++++


