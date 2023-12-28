# Opencv中关于特征点匹配定位的问题(二)单目标和多目标定位
# 单目标定位 https://blog.csdn.net/darlingqx/article/details/128275018
# 在opencv官方提供了一种定位的思路，就是通过匹配的点来获取透视变换矩阵，然后经过透视变换后就能够获得对应的目标的坐标了。
# 不知道为什么效果非常差
import cv2
import numpy as np

# 打开两个文件
img1 = cv2.imread('.\\2\\1.png')
img2 = cv2.imread('.\\2\\7.png')

# 灰度化
g1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
g2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 他建ORB特征检测
orb = cv2.ORB_create()

# 计算描述子与特征点
kp1, des1 = orb.detectAndCompute(g1, None)
kp2, des2 = orb.detectAndCompute(g2, None)

# bf创建匹配器
bf = cv2.BFMatcher_create()

# 对描述子进行匹配计算 https://blog.csdn.net/weixin_44072651/article/details/89262277
matchs = bf.knnMatch(des1, des2, k=2)

good = []
for i, (m, n) in enumerate(matchs):
    if m.distance < 0.80 * n.distance:
        good.append(m)

if len(good) >= 4:
    srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    # 查找单应性矩阵
    H, mask = cv2.findHomography(dstPts, srcPts, cv2.RANSAC, 5)

    h, w = img2.shape[:2]
    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
    dst = cv2.perspectiveTransform(pts, H)
    cv2.polylines(img1, [np.int32(dst)], True, (0, 0, 255), 4, 16)
else:
    print('the number of good is less than 4.')
    exit()

ret = cv2.drawMatchesKnn(img1, kp1, img2, kp2, [good], None)

# 问题： 在使用cv2.imshow()显示图片时，只能显示图片的部分内容，无法完全显示图片内容。原文链接：https://blog.csdn.net/qq_42482078/article/details/123319439
# 原因： 查看cv2.imshow()函数说明可知，opencv在使用cv2.imshow()显示图片时，是在指定窗口中显示图片，若在调用cv2.imshow()函数之前，没有调用创建窗口的函数，则默认使用cv2.WINDOW_AUTOSIZE标记创建默认窗口，如果需要显示大于屏幕分辨率的图像，则需要在使用cv2.imshow()之前调用cv2.namedWindow("", cv2.WINDOW_NORMAL)
# 版权声明：本文为CSDN博主「北溪入江流」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。

cv2.namedWindow('result', cv2.WINDOW_NORMAL)
cv2.imshow('result', ret)
cv2.waitKey(0)
cv2.destroyAllWindows()
