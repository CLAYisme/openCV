import cv2

# slam学习 特征匹配 https://blog.csdn.net/qq_42719217/article/details/125682083
# bf.match一对一匹配
# BF匹配首先对互相匹配的两个特征点创建BFmatcher对象，其原理是在第一幅图像中选择一个关键点然后依次与第二幅图像的每个关键点进行(改变)
# 距离测试，最后返回距离最近的关键点。然后根据匹配的质量对其进行排序。最后绘制前10个最佳匹配。
# 读取图像
img1 = cv2.imread('.\\1\\6.png', 0)
img2 = cv2.imread('.\\1\\7.png', 0)

# 使用sift算法，计算特征向量与特征点
sift = cv2.SIFT_create()  # 创建一个sift算子
kp1, des1 = sift.detectAndCompute(img1, None)  # 计算特征点与特征向量
img4 = cv2.drawKeypoints(img1, kp1, img1)  # 绘制关键点
cv2.imshow("sift.png", img4)
kp2, des2 = sift.detectAndCompute(img2, None)

bf = cv2.BFMatcher(crossCheck=True)
matches = bf.match(des1, des2)
print(matches)  # test13_5 检测完成之后进行坐标定位呢。https://blog.csdn.net/darlingqx/article/details/128263432
print(type(matches))
print("------------------------------")
print(matches[0].distance)
print(matches[0].imgIdx)  # 图片的索引
print(matches[0].queryIdx)  # 匹配模板图片对应的特征点索引
print(matches[0].trainIdx)  # 匹配原图片对应的特征点索引
print("------------------------------")
# 对点的距离的排序
matches = sorted(matches, key=lambda x: x.distance)  # 根据匹配质量排序，选择前n个

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:30], None, flags=2)  # 绘制前10个最佳匹配

# 图片展示
cv2.imshow("pipei.png", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
