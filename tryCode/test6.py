# 人脸检测
# 首先，我们来实现一个简单的人脸检测程序。这个程序可以读取一个图像，然后使用预训练的Haar级联分类器检测图像中的人脸。

import cv2

# 加载预训练的人脸级联分类器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 读取图像
img = cv2.imread('face.jpg')

# 将图像转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 使用级联分类器检测人脸
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 为每个检测到的人脸绘制一个矩形
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 显示结果
cv2.imshow('Faces found', img)
cv2.waitKey(0)