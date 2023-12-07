# bf.knnmatch一对多匹配
# knnmatch匹配的参数k，表示每个关键点保留的最佳即最短距离匹配的最大数量。下例取k=2，即每个查询关键点有两个最佳匹配。
#
# 次近邻的距离乘以一个小于1的值，获得的值称为阈值，只有当距离分值小于阈值时，则称之为“好点”。最近邻和次近邻大小差不多的点，更容易出现错误的匹配，即“坏点”。这种方法时比率检验。
#
# 应用比率检验，下例代码将阈值设置为次优匹配距离分值的0.75倍，如果knnmatch不满足次优匹配，则该点为“坏点”，舍弃。

import cv2

# 读取图像
img1 = cv2.imread('.\\1\\6.png', 0)
img2 = cv2.imread('.\\1\\7.png', 0)

# 使用sift算法，计算特征向量与特征点
sift = cv2.SIFT_create()  # 创建一个sift算子
kp1, des1 = sift.detectAndCompute(img1, None)  # 计算特征点与特征向量
kp2, des2 = sift.detectAndCompute(img2, None)

bf = cv2.BFMatcher()
# 添加knn算法
matches = bf.knnMatch(des1, des2, k=2)
print(matches)  # test13_5
print(type(matches))
good = []
for m, n in matches:
    if m.distance < 0.50 * n.distance:
        good.append([m])
# img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
# 显示前10个点：
img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good[:10], None, flags=2)

# 图片展示
cv2.imshow("pipei.png", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
