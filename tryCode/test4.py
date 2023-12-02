import cv2
import numpy as np
# 图像形态学操作
# 形态学操作是基于图像形状的一系列操作，包括腐蚀、膨胀、开运算和闭运算等。OpenCV提供了cv2.erode()、cv2.dilate()、cv2.morphologyEx()等函数来进行形态学操作。
# 载入图像
img = cv2.imread('image.jpg',0)

# 创建一个5x5的结构元素
kernel = np.ones((5,5),np.uint8)

# 进行膨胀操作
dilation = cv2.dilate(img,kernel,iterations = 1)

# 显示处理结果
cv2.imshow('dilation',dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()