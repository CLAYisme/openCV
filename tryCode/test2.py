import cv2
import numpy as np

# 边缘检测
# 边缘检测是计算机视觉中的常见任务，它可以用来识别图像中的物体。Canny边缘检测是一种常用的边缘检测算法，OpenCV中可以使用cv2.Canny()函数来进行Canny边缘检测。
# https://zhuanlan.zhihu.com/p/651610886
# 载入图像
img = cv2.imread('2\\1.png', 0)

# 进行Canny边缘检测
edges = cv2.Canny(img, 100, 200)

# 显示处理结果
cv2.imshow('edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
