# 实时人脸检测
# 接下来，我们来实现一个实时的人脸检测程序。这个程序可以实时地从摄像头捕获视频，并检测视频中的人脸。

import cv2

# 加载预训练的人脸级联分类器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取一帧
    ret, frame = cap.read()

    # 将帧转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 使用级联分类器检测人脸
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 为每个检测到的人脸绘制一个矩形
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 显示结果
    cv2.imshow('Faces found', frame)

    # 按'q'退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头
cap.release()

# 关闭所有窗口
cv2.destroyAllWindows()