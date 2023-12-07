# 下面图像特征检测选择SIFT算法，图像匹配算法选择FLANN算法，：用此图像2.png与下图1.png进行匹配
# 看起来效果很差
# FLANN(Fast_Library_for_Approximate_Nearest_Neighbors)快速最近邻搜索，是一个对大数据集和高维特征进行最近邻搜索的算法的集合，比蛮力匹配更快。
# Flann要用两个字典作为参数设置，第一个是index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5) 。trees指定待处理核密度树的数量（理想的数量在1-16）。对于SIFT算法，FLANN_INDEX_KDTREE = 1
# 第二个是search_params = dict(checks=50)，是递归次数，值越大效果越好，消耗时间越长。
# 代码取5kd-trees和50checks，其总能取得合理精度，而且短时间完成。舍弃距离大于0.7的点，可以避免90%的错误匹配，但是好的匹配结果也会很少。

import cv2

img1 = cv2.imread('.\\1\\6.png')
img2 = cv2.imread('.\\1\\7.png')
# 使用SIFT算法获取图像特征的关键点和描述符
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# 定义FLANN匹配器
indexParams = dict(algorithm=0, trees=5)
searchParams = dict(checks=50)
flann = cv2.FlannBasedMatcher(indexParams, searchParams)
# 使用KNN算法实现图像匹配，并对匹配结果排序
matches = flann.knnMatch(des1, des2, k=2)
matches = sorted(matches, key=lambda x: x[0].distance)

# 去除错误匹配，0.5是系数，系数大小不同，匹配的结果页不同
goodMatches = []
for m, n in matches:
    if m.distance < 0.50 * n.distance:
        goodMatches.append(m)

# 获取某个点的坐标位置
# index是获取匹配结果的中位数
index = int(len(goodMatches) / 2)
# queryIdx是目标图像的描述符索引
x, y = kp1[goodMatches[index].queryIdx].pt

# 拟合是指将平面上的一系列点，用一条光滑的曲线连接在一起。矩形包围框
# x, y, w, h = cv2.boundingRect(array) # x，y是矩阵左上点的坐标，w，h是矩阵的宽和高；array：轮廓数组；
# 将坐标位置勾画在2.png图片上，并显示轮廓拟合
# cv2.rectangle(img, pt1, pt2, color, thickness, lineType, shift ) #img：底图；pt1：矩形的左上角坐标；pt2：矩形的右下角坐标；color：线条的颜色，BGR；thickness：线的粗细，数值越大线越粗；
cv2.rectangle(img1, (int(x), int(y)), (int(x) + 10, int(y) + 10), (0, 255, 0), 1)


cv2.imshow('baofeng', img1)
cv2.waitKey()
