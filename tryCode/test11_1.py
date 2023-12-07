import cv2
import numpy as np
import matplotlib.pyplot as plt

# 绘制轮廓
im = cv2.imread('1\\5.png')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# 二值图像
ret, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)

# 找到图像轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(len(contours))
print(len(contours[0]))

'''print (type(contours))
image：二值结果图像
contours：图像轮廓点，list
hierarchy：轮廓结果层级信息
'''

# 尽量进行copy


cv2.imshow('img1', im)

# 绘制图像轮廓
# img = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
im = cv2.drawContours(im, contours, -1, (0, 0, 255), 3)

cv2.imshow('img2', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""Douglas-Peucker算法：
轮廓的不同特征，例如面积，周长，重心，边界框等。
轮廓近似 https://zhuanlan.zhihu.com/p/651610886
https://youcans.blog.csdn.net/article/details/125112487
将轮廓形状近似到另外一种由更少点组成的轮廓形状，新轮廓的点的数目 由我们设定的准确度来决定，使用的Douglas-Peucker算法。
如下图所示，现在可以使用这个函数来近似这个形状。cv2.approxPolyDP()函数的第二个参数叫 epsilon，它是从原始轮廓到近似轮廓的最大距离。它是一个准确度参数。
epsilon = 0.1 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
第二幅图中的绿线是当 epsilon = 10% 时得到的近似轮廓，第三幅 图是当 epsilon = 1% 时得到的近似轮廓。第三个参数设定弧线是否闭合。
"""
#  12.12 轮廓的多边形拟合
img = cv2.imread("1\\5.png", flags=1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度图像
blur = cv2.boxFilter(gray, -1, (5, 5))  # 盒式滤波器，9*9 平滑核
_, binary = cv2.threshold(blur, 205, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)

# 寻找二值化图中的轮廓
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # OpenCV4~
print('len:', len(contours))
# 绘制全部轮廓，contourIdx=-1 绘制全部轮廓
imgCnts = np.zeros(gray.shape[:2], np.uint8)  # 绘制轮廓函数会修改原始图像
imgCnts = cv2.drawContours(imgCnts, contours, -1, (255, 255, 255), thickness=2)  # 绘制全部轮廓

plt.figure(figsize=(9, 6))
plt.subplot(231), plt.axis('off'), plt.title("Origin")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(232), plt.axis('off'), plt.title("Binary")
plt.imshow(binary, 'gray')
plt.subplot(233), plt.axis('off'), plt.title("Contour")
plt.imshow(imgCnts, 'gray')

cnts = sorted(contours, key=cv2.contourArea, reverse=True)  # 所有轮廓按面积排序
cnt = cnts[0]  # 第 0 个轮廓，面积最大的轮廓，(664, 1, 2)
print("shape of max contour:", cnt.shape[0])

eps = [50, 30, 10]
for i in range(len(eps)):
    polyFit = cv2.approxPolyDP(cnt, eps[i], True)
    print("eps={}, shape of fitting polygon:{}".format(eps[i], polyFit.shape[0]))
    fitContour = np.zeros(gray.shape[:2], np.uint8)  # 初始化最大轮廓图像
    cv2.polylines(fitContour, [cnt], True, 205, thickness=2)  # 绘制最大轮廓，多边形曲线
    cv2.polylines(fitContour, [polyFit], True, 255, 3)
    plt.subplot(2, 3, i + 4), plt.axis('off'), plt.title("approxPoly(eps={})".format(eps[i]))
    plt.imshow(fitContour, 'gray')

plt.tight_layout()
plt.show()

'''
(0, 255, 0)：bgr颜色
3：线条宽度
画出来是灰色的因为原来就是灰度图COLOR_BGR2GRAY，所以需要先转换成彩色图片
'''
