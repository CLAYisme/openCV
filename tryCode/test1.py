import cv2
import numpy as np
# 图像阈值化
# 图像阈值化是将图像从灰度转换为二值化图像的过程，OpenCV提供了cv2.threshold()函数来进行这项操作。
# 载入图像并转为灰度图
img = cv2.imread('image.jpg',0)

# 阈值化处理
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# 显示处理结果
cv2.imshow('threshold',thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()