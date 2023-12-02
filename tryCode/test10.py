# https://zhuanlan.zhihu.com/p/647447851
# 加载预训练模型
# 首先，我们将学习如何加载一个预训练的模型。我们将使用OpenCV中的DNN模块，该模块支持多种深度学习框架，包括TensorFlow、Caffe等。
#
# import cv2
#
# # 加载预训练的模型
# net = cv2.dnn.readNetFromCaffe('bvlc_googlenet.prototxt', 'bvlc_googlenet.caffemodel')
# 图像分类
# 接下来，我们将使用加载的模型进行图像分类。我们将对一个图像进行预处理，然后将其输入到模型中，获取分类结果。
#
# import cv2
# import numpy as np
#
# # 加载预训练的模型
# net = cv2.dnn.readNetFromCaffe('bvlc_googlenet.prototxt', 'bvlc_googlenet.caffemodel')
#
# # 加载标签名
# with open('synset_words.txt', 'r') as f:
#     labels = f.read().strip().split("\n")
#
# # 加载图像，并进行预处理
# image = cv2.imread('image.jpg')
# blob = cv2.dnn.blobFromImage(image, 1, (224, 224), (104, 117, 123))
#
# # 将图像输入到网络中，进行前向传播，得到输出结果
# net.setInput(blob)
# outputs = net.forward()
#
# # 获取预测结果
# class_id = np.argmax(outputs)
# label = labels[class_id]
#
# print('Output class:', label)
# 物体检测
# 此外，我们还可以使用预训练的模型进行物体检测。我们将使用预训练的YOLO模型来检测图像中的物体。
#
# import cv2
# import numpy as np
#
# # 加载预训练的模型
# net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
#
# # 加载图像，并进行预处理
# image = cv2.imread('image.jpg')
# blob = cv2.dnn.blobFromImage(image, 1/255, (416, 416), swapRB=True, crop=False)
#
# # 将图像输入到网络中，进行前向传播，得到输出结果
# net.setInput(blob)
# layer_names = net.getLayerNames()
# output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
# outputs = net.forward(output_layers)
#
# # 处理网络的输出结果
# for output in outputs:
#     for detection in output:
#         scores = detection[5:]
#         class_id = np.argmax(scores)
#         confidence = scores[class_id]
#
#         if confidence > 0.5:
#             # 将检测到的物体在图像上标记出来
#             center_x, center_y, w, h = map(int, detection[0:4] * np.array([image.shape[1], image.shape[0], image.shape[1], image.shape[0]]))
#             x = center_x - w // 2
#             y = center_y - h // 2
#             cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
