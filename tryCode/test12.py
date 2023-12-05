import cv2
import numpy as np
import matplotlib.pyplot as plt

# 边界矩形
# 有两类边界矩形：直边界矩形和旋转的边界矩形
# 直边界矩形是一个直矩形（就是没有旋转的矩形）。它不会考虑对象是否旋转。 所以边界矩形的面积不是最小的。可以使用函数 cv2.boundingRect() 得到。
img = cv2.imread("1\\5.png", flags=1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度图像
blur = cv2.boxFilter(gray, -1, (5, 5))  # 盒式滤波器，9*9 平滑核
_, binary = cv2.threshold(blur, 205, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)

# 寻找二值化图中的轮廓
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # OpenCV4~
cnts = sorted(contours, key=cv2.contourArea, reverse=True)  # 所有轮廓按面积排序
cnt = cnts[0]
x, y, w, h = cv2.boundingRect(cnt)
img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
'''
参数表示依次为：（图片，长方形框左上角坐标, 长方形框右下角坐标，字体颜色，字体粗细）
'''
cv2.imshow('img1', img)

# 旋转的边界矩形是面积最小的，因为它考虑了对象的旋转。用函数cv2.minAreaRect()。
# 返回的是一个 Box2D 结构，其中包含矩形左上角角点的坐标（x，y），矩形的宽和高（w，h），以及旋转角度。但是要绘制这个矩形需要矩形的 4 个角点，可以通过函数 cv2.boxPoints() 获得。
# 得到最小外接矩形的（中心(x, y), (宽, 高), 旋转角度）
rect = cv2.minAreaRect(cnt)

# 获取最小外接矩形的4个顶点坐标
box = cv2.boxPoints(rect)
print(type(box))
print(type([box]))
print(type(contours))

# 画出来
img = cv2.drawContours(img, contours, 0, (0, 0, 255), 5)
img = cv2.drawContours(img, [box], 0, (0, 0, 255), 5)

cv2.imshow('img2', img)
# plt.imshow(img)
# plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
