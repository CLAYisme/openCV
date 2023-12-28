# Opencv中关于特征点匹配定位的问题(二)单目标和多目标定位
# 但是可以通过上一章的方法，利用坐标点来直接定位到目标，而不通过透视变换进行定位。
# 代码如下
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
# 打开两个文件
img = cv2.imread('.\\2\\1.png')
tem = cv2.imread('.\\2\\7.png')

newimg = np.copy(img)
# 创建特征点检测器
orb = cv2.ORB_create()
# 创建BF特征点匹配器
bf = cv2.BFMatcher_create()

# 检测原图特征点
kp1, des1 = orb.detectAndCompute(img, mask=None)
# 检测模板图特征点
kp2, des2 = orb.detectAndCompute(tem, mask=None)
# 进行匹配
res = bf.knnMatch(des1, des2, k=2)

good_res = []
for m, n in res:
    if m.distance < 0.8 * n.distance:
        good_res.append(m)


def get_rect(res, kp1, kp2):
    h, w = tem.shape[0:2]
    rect = []
    for i in res:
        # 获得坐标
        point1 = cv2.KeyPoint_convert(kp1, keypointIndexes=[i.queryIdx])
        point2 = cv2.KeyPoint_convert(kp2, keypointIndexes=[i.trainIdx])
        point1 = [int(np.ravel(point1)[0]), int(np.ravel(point1)[1])]
        point2 = [int(np.ravel(point2)[0]), int(np.ravel(point2)[1])]
        # 获得目标框左上角的坐标
        minx = point1[0] - point2[0]
        miny = point1[1] - point2[1]
        # 消除多余的目标框
        if [minx, miny, w, h] not in rect:
            rect.append([minx, miny, w, h])

    return rect


rect = get_rect(good_res, kp1, kp2)

# 画出目标框
for i in range(len(rect)):
    cv2.rectangle(newimg, rect[i], [255, 0, 0], 4, 16)
# 将最相近的10个点绘画出来
newimg = cv2.drawMatches(newimg, kp1, tem, kp2, good_res, None)
# 绘制原图特征点
img = cv2.drawKeypoints(img, kp1, None, color=[0, 0, 255])
tem = cv2.drawKeypoints(tem, kp2, None, color=[0, 255, 0])
cv2.namedWindow('frams', cv2.WINDOW_NORMAL)
cv2.imshow('frams', newimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
