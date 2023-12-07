# pencv中关于特征点匹配定位的问题(一)DMatch解析 https://blog.csdn.net/darlingqx/article/details/128263432
# 那么问题来了，如何对检测完成之后进行坐标定位呢。
# 首先我们要看bf.match生成的结果：

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
img = cv2.imread('.\\1\\6.png')
tem = cv2.imread('.\\1\\7.png')

# 创建特征点检测器
orb = cv2.ORB_create()
# 创建BF特征点匹配器
bf = cv2.BFMatcher_create()

# 检测原图特征点
kp1, des1 = orb.detectAndCompute(img, mask=None)
# 检测模板图特征点
kp2, des2 = orb.detectAndCompute(tem, mask=None)
# 进行匹配
res = bf.match(des1, des2)

# 将匹配点按照距离排序
res = sorted(res, key=lambda x: x.distance)


def get_rect(res, kp, idx=0):
    point_img = []
    # 获得前十res个对应的点
    for i in res[:10]:
        if idx == 0:
            center = cv2.KeyPoint_convert(kp, keypointIndexes=[i.queryIdx])
        elif idx == 1:
            center = cv2.KeyPoint_convert(kp, keypointIndexes=[i.trainIdx])
        center = [int(np.ravel(center)[0]), int(np.ravel(center)[1])]
        point_img.append(center)
    print("``````````")
    print(point_img)
    print(type(point_img))
    print(type(point_img[0]))

    print("``````````")
    # 获得框的左上角点和右下角点
    minres = np.argmin(point_img, axis=0)
    maxres = np.argmax(point_img, axis=0)
    minpoint = [point_img[minres[0]][0], point_img[minres[1]][1]]
    maxpoint = [point_img[maxres[0]][0], point_img[maxres[1]][1]]
    return minpoint, maxpoint


min1, max2 = get_rect(res, kp1, 0)
min3, max4 = get_rect(res, kp2, 1)

cv2.rectangle(tem, min3, max4, [255, 0, 0], 4, 16)
cv2.rectangle(img, min1, max2, [255, 0, 0], 4, 16)

# 将最相近的10个点绘画出来
newimg = cv2.drawMatches(img, kp1, tem, kp2, res[:10], None)
# 绘制原图特征点
img = cv2.drawKeypoints(img, kp1, None, color=[0, 0, 255])
tem = cv2.drawKeypoints(tem, kp2, None, color=[0, 255, 0])


# 显示图片
def imshow(img, axis, title=None):
    axis = str(axis[0]) + str(axis[1])
    for i in range(len(img)):
        plt.subplot(int(axis + str(i + 1)))
        if title:
            plt.title(title[i])
        i = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)
        plt.imshow(i)
    plt.show()


all_img = [img, tem, newimg]
all_title = ['img', 'tem', 'newimg']
imshow(all_img, [2, 2], all_title)
