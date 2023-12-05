# 图像二值化
# 二值化是将图像处理为只有两个颜色的过程，也就是将图像处理为黑白两色。二值化后的图像对于很多图像处理任务（如边缘检测、物体识别等）有很大的帮助，OpenCV中可以使用cv2.threshold()函数来进行二值化操作。

import cv2
import numpy as np

# 载入图像
img = cv2.imread('image.jpg',0)

# 进行二值化操作
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# 显示处理结果
cv2.imshow('binary',thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()