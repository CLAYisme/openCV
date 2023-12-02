# 图像拼接
# 图像拼接是将两个或多个图像在一定的几何和光度条件下拼接在一起，形成一个包含了所有输入图像视场的大视场图像。以下实战案例将展示如何使用OpenCV进行图像拼接。

import cv2
import numpy as np

# 读取两个图像
img1 = cv2.imread('road1.jpg')
img2 = cv2.imread('road2.jpg')

# 将两个图像拼接成一个图像
stitcher = cv2.Stitcher.create()
result, pano = stitcher.stitch([img1, img2])

if result == cv2.Stitcher_OK:
    cv2.imshow('Panorama', pano)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("Error during stitching.")