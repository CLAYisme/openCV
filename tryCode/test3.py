# 图像滤波
# 图像滤波是计算机视觉中常见的图像预处理方法，OpenCV提供了各种滤波函数，如cv2.filter2D()、cv2.blur()、cv2.GaussianBlur()等。
import cv2
import numpy as np

# 载入图像
img = cv2.imread('image.jpg')

# 使用高斯滤波进行图像平滑处理
blur = cv2.GaussianBlur(img,(5,5),0)

# 显示处理结果
cv2.imshow('blur',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
