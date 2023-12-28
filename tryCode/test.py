import csv
import ast
import json


def str_to_dict1(string):
    # 使用json模块的loads函数将字符串转换为字典
    result = json.loads(string)
    return result


def str_to_dict2(string):
    # 使用ast模块的literal_eval函数将字符串转换为字典
    result = ast.literal_eval(string)
    return result


############################################################################################################
my_dict_input = ""
my_dict_output = ""
print("------------read-----------------")
with open('input_params.dat', 'r', encoding="utf-8") as file:
    my_dict_input = file.read()

with open('output_params.dat', 'r', encoding="utf-8") as file:
    my_dict_output = file.read()

my_dict_input = eval(my_dict_input)
my_dict_output = eval(my_dict_output)



############################################################################################################
#
# my_dict_out = {"三色灯红": {"CardID": 1, "Index": 10, "Name": "三色灯红", "Note": "", "OutputType": 1},
#                "三色灯黄": {"CardID": 1, "Index": 12, "Name": "三色灯黄", "Note": "", "OutputType": 1},
#                "三色灯绿": {"CardID": 1, "Index": 11, "Name": "三色灯绿", "Note": "", "OutputType": 1},
#                "伺服使能1号电箱": {"CardID": 0, "Index": 6, "Name": "伺服使能1号电箱", "Note": "", "OutputType": 1},
#                "照明": {"CardID": 2, "Index": 14, "Name": "照明", "Note": "", "OutputType": 0},
#                "变距升降气缸伸出": {"CardID": 2, "Index": 15, "Name": "变距升降气缸伸出", "Note": "", "OutputType": 1},
#                "变距升降气缸缩回": {"CardID": 1, "Index": 7, "Name": "变距升降气缸缩回", "Note": "", "OutputType": 1},
#                "变距横移气缸伸出": {"CardID": 2, "Index": 13, "Name": "变距横移气缸伸出", "Note": "", "OutputType": 1},
#                "变距横移气缸缩回": {"CardID": 1, "Index": 8, "Name": "变距横移气缸缩回", "Note": "", "OutputType": 1},
#                "扫码真空吸1": {"CardID": 2, "Index": 17, "Name": "扫码真空吸1", "Note": "", "OutputType": 1},
#                "扫码真空吸2": {"CardID": 2, "Index": 18, "Name": "扫码真空吸2", "Note": "", "OutputType": 1},
#                "扫码真空吸3": {"CardID": 2, "Index": 19, "Name": "扫码真空吸3", "Note": "", "OutputType": 1},
#                "扫码真空吸4": {"CardID": 2, "Index": 20, "Name": "扫码真空吸4", "Note": "", "OutputType": 1},
#                "扫码真空吸5": {"CardID": 2, "Index": 21, "Name": "扫码真空吸5", "Note": "", "OutputType": 1},
#                "一号水平扫码气缸": {"CardID": 2, "Index": 16, "Name": "一号水平扫码气缸", "Note": "", "OutputType": 1},
#                "一号垂直扫码气缸": {"CardID": 1, "Index": 9, "Name": "一号垂直扫码气缸", "Note": "", "OutputType": 1},
#                "移栽顶升气缸": {"CardID": 2, "Index": 1, "Name": "移栽顶升气缸", "Note": "", "OutputType": 1},
#                "移栽气缸": {"CardID": 2, "Index": 2, "Name": "移栽气缸", "Note": "", "OutputType": 1},
#                "测试伸缩气缸": {"CardID": 2, "Index": 3, "Name": "测试伸缩气缸", "Note": "", "OutputType": 1},
#                "分选升降气缸1": {"CardID": 2, "Index": 4, "Name": "分选升降气缸1", "Note": "", "OutputType": 1},
#                "分选升降气缸2": {"CardID": 2, "Index": 5, "Name": "分选升降气缸2", "Note": "", "OutputType": 1},
#                "测试通道1": {"CardID": 0, "Index": 8, "Name": "测试通道1", "Note": "", "OutputType": 1},
#                "测试通道2": {"CardID": 0, "Index": 9, "Name": "测试通道2", "Note": "", "OutputType": 1},
#                "测试通道3": {"CardID": 0, "Index": 10, "Name": "测试通道3", "Note": "", "OutputType": 1},
#                "测试通道4": {"CardID": 0, "Index": 11, "Name": "测试通道4", "Note": "", "OutputType": 1},
#                "测试通道5": {"CardID": 0, "Index": 12, "Name": "测试通道5", "Note": "", "OutputType": 1},
#                "取电芯气缸1": {"CardID": 2, "Index": 8, "Name": "取电芯气缸1", "Note": "", "OutputType": 1},
#                "取电芯气缸2": {"CardID": 2, "Index": 9, "Name": "取电芯气缸2", "Note": "", "OutputType": 1},
#                "取电芯气缸3": {"CardID": 2, "Index": 10, "Name": "取电芯气缸3", "Note": "", "OutputType": 1},
#                "取电芯气缸4": {"CardID": 2, "Index": 11, "Name": "取电芯气缸4", "Note": "", "OutputType": 1},
#                "取电芯气缸5": {"CardID": 2, "Index": 12, "Name": "取电芯气缸5", "Note": "", "OutputType": 1},
#                "伺服使能2号电箱": {"CardID": 4, "Index": 11, "Name": "伺服使能2号电箱", "Note": "", "OutputType": 1},
#                "照明2": {"CardID": 4, "Index": 23, "Name": "照明2", "Note": "", "OutputType": 0},
#                "二节1挡收料皮带调速电机": {"CardID": 4, "Index": 7, "Name": "二节1挡收料皮带调速电机", "Note": "",
#                                            "OutputType": 1},
#                "二节2挡收料皮带调速电机": {"CardID": 4, "Index": 8, "Name": "二节2挡收料皮带调速电机", "Note": "",
#                                            "OutputType": 1},
#                "二节3挡收料皮带调速电机": {"CardID": 4, "Index": 9, "Name": "二节3挡收料皮带调速电机", "Note": "",
#                                            "OutputType": 1},
#                "二节4挡收料皮带调速电机": {"CardID": 4, "Index": 10, "Name": "二节4挡收料皮带调速电机", "Note": "",
#                                            "OutputType": 1},
#                "二节1挡扫码位移栽顶升气缸": {"CardID": 3, "Index": 11, "Name": "二节1挡扫码位移栽顶升气缸", "Note": "",
#                                              "OutputType": 1},
#                "二节1挡扫码位移栽气缸": {"CardID": 3, "Index": 12, "Name": "二节1挡扫码位移栽气缸", "Note": "",
#                                          "OutputType": 1},
#                "二节2挡扫码位移栽顶升气缸": {"CardID": 4, "Index": 1, "Name": "二节2挡扫码位移栽顶升气缸", "Note": "",
#                                              "OutputType": 1},
#                "二节2挡扫码位移栽气缸": {"CardID": 4, "Index": 2, "Name": "二节2挡扫码位移栽气缸", "Note": "",
#                                          "OutputType": 1},
#                "二节3挡扫码位移栽顶升气缸": {"CardID": 4, "Index": 3, "Name": "二节3挡扫码位移栽顶升气缸", "Note": "",
#                                              "OutputType": 1},
#                "二节3挡扫码位移栽气缸": {"CardID": 4, "Index": 4, "Name": "二节3挡扫码位移栽气缸", "Note": "",
#                                          "OutputType": 1},
#                "二节4挡扫码位移栽顶升气缸": {"CardID": 4, "Index": 5, "Name": "二节4挡扫码位移栽顶升气缸", "Note": "",
#                                              "OutputType": 1},
#                "二节4挡扫码位移栽气缸": {"CardID": 4, "Index": 6, "Name": "二节4挡扫码位移栽气缸", "Note": "",
#                                          "OutputType": 1},
#                "二节1挡拦截气缸1": {"CardID": 3, "Index": 13, "Name": "二节1挡拦截气缸1", "Note": "", "OutputType": 1},
#                "二节1挡拦截气缸2": {"CardID": 3, "Index": 14, "Name": "二节1挡拦截气缸2", "Note": "", "OutputType": 1},
#                "二节2挡拦截气缸1": {"CardID": 3, "Index": 18, "Name": "二节2挡拦截气缸1", "Note": "", "OutputType": 1},
#                "二节2挡拦截气缸2": {"CardID": 3, "Index": 19, "Name": "二节2挡拦截气缸2", "Note": "", "OutputType": 1},
#                "二节3挡拦截气缸1": {"CardID": 3, "Index": 23, "Name": "二节3挡拦截气缸1", "Note": "", "OutputType": 1},
#                "二节3挡拦截气缸2": {"CardID": 3, "Index": 24, "Name": "二节3挡拦截气缸2", "Note": "", "OutputType": 1},
#                "二节4挡拦截气缸1": {"CardID": 4, "Index": 17, "Name": "二节4挡拦截气缸1", "Note": "", "OutputType": 1},
#                "二节4挡拦截气缸2": {"CardID": 4, "Index": 18, "Name": "二节4挡拦截气缸2", "Note": "", "OutputType": 1},
#                "二节取NG电芯真空吸1": {"CardID": 3, "Index": 5, "Name": "二节取NG电芯真空吸1", "Note": "",
#                                        "OutputType": 1},
#                "二节取NG电芯真空吸2": {"CardID": 3, "Index": 6, "Name": "二节取NG电芯真空吸2", "Note": "",
#                                        "OutputType": 1},
#                "二节取NG电芯真空吸3": {"CardID": 3, "Index": 7, "Name": "二节取NG电芯真空吸3", "Note": "",
#                                        "OutputType": 1},
#                "二节抓NG料升降气缸": {"CardID": 3, "Index": 10, "Name": "二节抓NG料升降气缸", "Note": "",
#                                       "OutputType": 1},
#                "三节1挡收料皮带调速电机": {"CardID": 3, "Index": 4, "Name": "三节1挡收料皮带调速电机", "Note": "",
#                                            "OutputType": 1},
#                "三节2挡收料皮带调速电机": {"CardID": 3, "Index": 3, "Name": "三节2挡收料皮带调速电机", "Note": "",
#                                            "OutputType": 1},
#                "三节3挡收料皮带调速电机": {"CardID": 3, "Index": 1, "Name": "三节3挡收料皮带调速电机", "Note": "",
#                                            "OutputType": 1},
#                "三节4挡收料皮带调速电机": {"CardID": 3, "Index": 2, "Name": "三节4挡收料皮带调速电机", "Note": "",
#                                            "OutputType": 1},
#                "第三节1挡够数指示": {"CardID": 4, "Index": 13, "Name": "第三节1挡够数指示", "Note": "",
#                                      "OutputType": 1},
#                "第三节2挡够数指示": {"CardID": 4, "Index": 14, "Name": "第三节2挡够数指示", "Note": "",
#                                      "OutputType": 1},
#                "第三节3挡够数指示": {"CardID": 4, "Index": 15, "Name": "第三节3挡够数指示", "Note": "",
#                                      "OutputType": 1},
#                "第三节4挡够数指示": {"CardID": 4, "Index": 16, "Name": "第三节4挡够数指示", "Note": "",
#                                      "OutputType": 1},
#                "未定义": {"CardID": 2, "Index": 16, "Name": "未定义", "Note": "", "OutputType": 1}}

C1 = list()
C2 = list()
C3 = list()
C4 = list()
C5 = list()

for key, value in my_dict_output.items():
    CardID = value['CardID']
    Index = value['Index']
    if (CardID == 0):
        C1.append([key, Index])
    elif (CardID == 1):
        C2.append([key, Index])
    elif (CardID == 2):
        C3.append([key, Index])
    elif (CardID == 3):
        C4.append([key, Index])
    elif (CardID == 4):
        C5.append([key, Index])
    # print(key, CardID, Index)

print("-------------1----------------")
print(C1)
print("--------------2---------------")
print(C2)
print("-------------3----------------")
print(C3)
print("--------------4---------------")
print(C4)
print("------------5-----------------")
print(C5)

# data = [C1, C2, C3, C4, C5]
# print(data)
with open('output.csv', 'a+', newline='') as file:
    writer = csv.writer(file)
    writer.writerows([["板卡1"]])
    writer.writerows(C1)
    writer.writerows([["板卡2"]])
    writer.writerows(C2)
    writer.writerows([["板卡3"]])
    writer.writerows(C3)
    writer.writerows([["板卡4"]])
    writer.writerows(C4)
    writer.writerows([["板卡5"]])
    writer.writerows(C5)

############################################################################################################
#
# my_dict_input = {"启动按钮": {"CardID": 0, "Index": 1, "Name": "启动按钮", "InputType": 1, "Note": ""},
#                  "停止按钮": {"CardID": 0, "Index": 2, "Name": "停止按钮", "InputType": 1, "Note": ""},
#                  "急停按钮": {"CardID": 0, "Index": 3, "Name": "急停按钮", "InputType": 0, "Note": ""},
#                  "清报警按钮": {"CardID": 0, "Index": 4, "Name": "清报警按钮", "InputType": 1, "Note": ""},
#                  "气压检测": {"CardID": 0, "Index": 16, "Name": "气压检测", "InputType": 1, "Note": ""},
#                  "青稞纸缺料感应": {"CardID": 2, "Index": 32, "Name": "青稞纸缺料感应", "InputType": 1, "Note": ""},
#                  "下料皮带满料": {"CardID": 1, "Index": 1, "Name": "下料皮带满料", "InputType": 1, "Note": ""},
#                  "冲切前光纤感应1": {"CardID": 1, "Index": 2, "Name": "冲切前光纤感应1", "InputType": 1, "Note": ""},
#                  "冲切前光纤感应2": {"CardID": 1, "Index": 3, "Name": "冲切前光纤感应2", "InputType": 1, "Note": ""},
#                  "冲切前光纤感应3": {"CardID": 1, "Index": 4, "Name": "冲切前光纤感应3", "InputType": 1, "Note": ""},
#                  "冲切前光纤感应4": {"CardID": 2, "Index": 1, "Name": "冲切前光纤感应4", "InputType": 1, "Note": ""},
#                  "冲切前光纤感应5": {"CardID": 2, "Index": 2, "Name": "冲切前光纤感应5", "InputType": 1, "Note": ""},
#                  "冲切气缸缩回": {"CardID": 1, "Index": 10, "Name": "冲切气缸缩回", "InputType": 1, "Note": ""},
#                  "变距升降气缸缩回": {"CardID": 0, "Index": 11, "Name": "变距升降气缸缩回", "InputType": 1, "Note": ""},
#                  "变距升降气缸伸出": {"CardID": 0, "Index": 7, "Name": "变距升降气缸伸出", "InputType": 1, "Note": ""},
#                  "扫码真空吸感应1": {"CardID": 0, "Index": 14, "Name": "扫码真空吸感应1", "InputType": 1, "Note": ""},
#                  "扫码真空吸感应2": {"CardID": 1, "Index": 9, "Name": "扫码真空吸感应2", "InputType": 1, "Note": ""},
#                  "扫码真空吸感应3": {"CardID": 1, "Index": 5, "Name": "扫码真空吸感应3", "InputType": 1, "Note": ""},
#                  "扫码真空吸感应4": {"CardID": 1, "Index": 6, "Name": "扫码真空吸感应4", "InputType": 1, "Note": ""},
#                  "扫码真空吸感应5": {"CardID": 0, "Index": 15, "Name": "扫码真空吸感应5", "InputType": 1, "Note": ""},
#                  "变距横移气缸伸出": {"CardID": 0, "Index": 5, "Name": "变距横移气缸伸出", "InputType": 1, "Note": ""},
#                  "变距横移气缸缩回": {"CardID": 0, "Index": 6, "Name": "变距横移气缸缩回", "InputType": 1, "Note": ""},
#                  "一号水平扫码气缸缩回": {"CardID": 0, "Index": 12, "Name": "一号水平扫码气缸缩回", "InputType": 1,
#                                           "Note": ""},
#                  "一号水平扫码气缸伸出": {"CardID": 0, "Index": 13, "Name": "一号水平扫码气缸伸出", "InputType": 1,
#                                           "Note": ""},
#                  "一号垂直扫码气缸缩回": {"CardID": 1, "Index": 16, "Name": "一号垂直扫码气缸缩回", "InputType": 1,
#                                           "Note": ""},
#                  "一号垂直扫码气缸伸出": {"CardID": 1, "Index": 15, "Name": "一号垂直扫码气缸伸出", "InputType": 1,
#                                           "Note": ""},
#                  "移栽顶升气缸伸出": {"CardID": 2, "Index": 10, "Name": "移栽顶升气缸伸出", "InputType": 1, "Note": ""},
#                  "移栽顶升气缸缩回": {"CardID": 2, "Index": 11, "Name": "移栽顶升气缸缩回", "InputType": 1, "Note": ""},
#                  "测试移栽气缸伸出": {"CardID": 2, "Index": 6, "Name": "测试移栽气缸伸出", "InputType": 1, "Note": ""},
#                  "测试移栽气缸缩回": {"CardID": 2, "Index": 5, "Name": "测试移栽气缸缩回", "InputType": 1, "Note": ""},
#                  "测试伸缩气缸伸出": {"CardID": 2, "Index": 8, "Name": "测试伸缩气缸伸出", "InputType": 1, "Note": ""},
#                  "测试伸缩气缸缩回": {"CardID": 2, "Index": 9, "Name": "测试伸缩气缸缩回", "InputType": 1, "Note": ""},
#                  "分选升降气缸1伸出": {"CardID": 0, "Index": 10, "Name": "分选升降气缸1伸出", "InputType": 1,
#                                        "Note": ""},
#                  "分选升降气缸1缩回": {"CardID": 0, "Index": 9, "Name": "分选升降气缸1缩回", "InputType": 1,
#                                        "Note": ""},
#                  "分选升降气缸2伸出": {"CardID": 2, "Index": 15, "Name": "分选升降气缸2伸出", "InputType": 1,
#                                        "Note": ""},
#                  "分选升降气缸2缩回": {"CardID": 2, "Index": 14, "Name": "分选升降气缸2缩回", "InputType": 1,
#                                        "Note": ""},
#                  "一档料道感应1光电开关": {"CardID": 2, "Index": 12, "Name": "一档料道感应1光电开关", "InputType": 1,
#                                            "Note": ""},
#                  "二档料道感应1光电开关": {"CardID": 2, "Index": 18, "Name": "二档料道感应1光电开关", "InputType": 1,
#                                            "Note": ""},
#                  "二档料道感应2光电开关": {"CardID": 2, "Index": 19, "Name": "二档料道感应2光电开关", "InputType": 1,
#                                            "Note": ""},
#                  "三档料道感应1光电开关": {"CardID": 2, "Index": 23, "Name": "三档料道感应1光电开关", "InputType": 1,
#                                            "Note": ""},
#                  "三档料道感应2光电开关": {"CardID": 2, "Index": 24, "Name": "三档料道感应2光电开关", "InputType": 1,
#                                            "Note": ""},
#                  "四档料道感应1光电开关": {"CardID": 2, "Index": 28, "Name": "四档料道感应1光电开关", "InputType": 1,
#                                            "Note": ""},
#                  "四档料道感应2光电开关": {"CardID": 2, "Index": 29, "Name": "四档料道感应2光电开关", "InputType": 1,
#                                            "Note": ""},
#                  "一号机NG感应光电开关": {"CardID": 2, "Index": 7, "Name": "一号机NG感应光电开关", "InputType": 1,
#                                           "Note": ""},
#                  "二节1挡有料感应": {"CardID": 3, "Index": 15, "Name": "二节1挡有料感应", "InputType": 1, "Note": ""},
#                  "二节1挡满料感应": {"CardID": 3, "Index": 16, "Name": "二节1挡满料感应", "InputType": 1, "Note": ""},
#                  "二节2挡有料感应": {"CardID": 3, "Index": 13, "Name": "二节2挡有料感应", "InputType": 1, "Note": ""},
#                  "二节2挡满料感应": {"CardID": 3, "Index": 14, "Name": "二节2挡满料感应", "InputType": 1, "Note": ""},
#                  "二节3挡有料感应": {"CardID": 3, "Index": 11, "Name": "二节3挡有料感应", "InputType": 1, "Note": ""},
#                  "二节3挡满料感应": {"CardID": 3, "Index": 12, "Name": "二节3挡满料感应", "InputType": 1, "Note": ""},
#                  "二节4挡有料感应": {"CardID": 3, "Index": 9, "Name": "二节4挡有料感应", "InputType": 1, "Note": ""},
#                  "二节4挡满料感应": {"CardID": 3, "Index": 10, "Name": "二节4挡满料感应", "InputType": 1, "Note": ""},
#                  "二节1挡扫码位移栽顶升气缸伸出": {"CardID": 3, "Index": 3, "Name": "二节1挡扫码位移栽顶升气缸伸出",
#                                                    "InputType": 1, "Note": ""},
#                  "二节1挡扫码位移栽顶升气缸缩回": {"CardID": 3, "Index": 4, "Name": "二节1挡扫码位移栽顶升气缸缩回",
#                                                    "InputType": 1, "Note": ""},
#                  "二节1挡扫码位移栽气缸伸出": {"CardID": 3, "Index": 5, "Name": "二节1挡扫码位移栽气缸伸出",
#                                                "InputType": 1, "Note": ""},
#                  "二节1挡扫码位移栽气缸缩回": {"CardID": 3, "Index": 6, "Name": "二节1挡扫码位移栽气缸缩回",
#                                                "InputType": 1, "Note": ""},
#                  "二节2挡扫码位移栽顶升气缸伸出": {"CardID": 4, "Index": 1, "Name": "二节2挡扫码位移栽顶升气缸伸出",
#                                                    "InputType": 1, "Note": ""},
#                  "二节2挡扫码位移栽顶升气缸缩回": {"CardID": 4, "Index": 2, "Name": "二节2挡扫码位移栽顶升气缸缩回",
#                                                    "InputType": 1, "Note": ""},
#                  "二节2挡扫码位移栽气缸伸出": {"CardID": 4, "Index": 3, "Name": "二节2挡扫码位移栽气缸伸出",
#                                                "InputType": 1, "Note": ""},
#                  "二节2挡扫码位移栽气缸缩回": {"CardID": 4, "Index": 4, "Name": "二节2挡扫码位移栽气缸缩回",
#                                                "InputType": 1, "Note": ""},
#                  "二节3挡扫码位移栽顶升气缸伸出": {"CardID": 4, "Index": 5, "Name": "二节3挡扫码位移栽顶升气缸伸出",
#                                                    "InputType": 1, "Note": ""},
#                  "二节3挡扫码位移栽顶升气缸缩回": {"CardID": 4, "Index": 6, "Name": "二节3挡扫码位移栽顶升气缸缩回",
#                                                    "InputType": 1, "Note": ""},
#                  "二节3挡扫码位移栽气缸伸出": {"CardID": 4, "Index": 7, "Name": "二节3挡扫码位移栽气缸伸出",
#                                                "InputType": 1, "Note": ""},
#                  "二节3挡扫码位移栽气缸缩回": {"CardID": 4, "Index": 8, "Name": "二节3挡扫码位移栽气缸缩回",
#                                                "InputType": 1, "Note": ""},
#                  "二节4挡扫码位移栽顶升气缸伸出": {"CardID": 4, "Index": 9, "Name": "二节4挡扫码位移栽顶升气缸伸出",
#                                                    "InputType": 1, "Note": ""},
#                  "二节4挡扫码位移栽顶升气缸缩回": {"CardID": 4, "Index": 10, "Name": "二节4挡扫码位移栽顶升气缸缩回",
#                                                    "InputType": 1, "Note": ""},
#                  "二节4挡扫码位移栽气缸伸出": {"CardID": 4, "Index": 11, "Name": "二节4挡扫码位移栽气缸伸出",
#                                                "InputType": 1, "Note": ""},
#                  "二节4挡扫码位移栽气缸缩回": {"CardID": 4, "Index": 12, "Name": "二节4挡扫码位移栽气缸缩回",
#                                                "InputType": 1, "Note": ""},
#                  "二节抓NG料升降气缸伸出": {"CardID": 3, "Index": 8, "Name": "二节抓NG料升降气缸伸出", "InputType": 1,
#                                             "Note": ""},
#                  "二节抓NG料升降气缸缩回": {"CardID": 3, "Index": 7, "Name": "二节抓NG料升降气缸缩回", "InputType": 1,
#                                             "Note": ""},
#                  "分选取料吸紧感应1": {"CardID": 2, "Index": 26, "Name": "分选取料吸紧感应1", "InputType": 1,
#                                        "Note": ""},
#                  "分选取料吸紧感应2": {"CardID": 2, "Index": 25, "Name": "分选取料吸紧感应2", "InputType": 1,
#                                        "Note": ""},
#                  "分选取料吸紧感应3": {"CardID": 2, "Index": 22, "Name": "分选取料吸紧感应3", "InputType": 1,
#                                        "Note": ""},
#                  "分选取料吸紧感应4": {"CardID": 2, "Index": 21, "Name": "分选取料吸紧感应4", "InputType": 1,
#                                        "Note": ""},
#                  "分选取料吸紧感应5": {"CardID": 2, "Index": 20, "Name": "分选取料吸紧感应5", "InputType": 1,
#                                        "Note": ""},
#                  "NG取料吸紧感应1": {"CardID": 4, "Index": 23, "Name": "NG取料吸紧感应1", "InputType": 1, "Note": ""},
#                  "NG取料吸紧感应2": {"CardID": 4, "Index": 24, "Name": "NG取料吸紧感应2", "InputType": 1, "Note": ""},
#                  "NG取料吸紧感应3": {"CardID": 4, "Index": 25, "Name": "NG取料吸紧感应3", "InputType": 1, "Note": ""},
#                  "第三节左急停按钮": {"CardID": 4, "Index": 17, "Name": "第三节左急停按钮", "InputType": 1, "Note": ""},
#                  "第三节右急停按钮": {"CardID": 4, "Index": 18, "Name": "第三节右急停按钮", "InputType": 1, "Note": ""},
#                  "第三节1挡启动": {"CardID": 4, "Index": 22, "Name": "第三节1挡启动", "InputType": 1, "Note": ""},
#                  "第三节2挡启动": {"CardID": 4, "Index": 21, "Name": "第三节2挡启动", "InputType": 1, "Note": ""},
#                  "第三节3挡启动": {"CardID": 4, "Index": 20, "Name": "第三节3挡启动", "InputType": 1, "Note": ""},
#                  "第三节4挡启动": {"CardID": 4, "Index": 19, "Name": "第三节4挡启动", "InputType": 1, "Note": ""},
#                  "三节1挡收料皮带尾有料": {"CardID": 4, "Index": 16, "Name": "三节1挡收料皮带尾有料", "InputType": 1,
#                                            "Note": ""},
#                  "三节2挡收料皮带尾有料": {"CardID": 4, "Index": 15, "Name": "三节2挡收料皮带尾有料", "InputType": 1,
#                                            "Note": ""},
#                  "三节3挡收料皮带尾有料": {"CardID": 4, "Index": 14, "Name": "三节3挡收料皮带尾有料", "InputType": 1,
#                                            "Note": ""},
#                  "三节4挡收料皮带尾有料": {"CardID": 4, "Index": 13, "Name": "三节4挡收料皮带尾有料", "InputType": 1,
#                                            "Note": ""},
#                  "未定义": {"CardID": 2, "Index": 13, "Name": "未定义", "InputType": 1, "Note": ""}}

C1 = list()
C2 = list()
C3 = list()
C4 = list()
C5 = list()

for key, value in my_dict_input.items():
    CardID = value['CardID']
    Index = value['Index']
    if (CardID == 0):
        C1.append([key, Index])
    elif (CardID == 1):
        C2.append([key, Index])
    elif (CardID == 2):
        C3.append([key, Index])
    elif (CardID == 3):
        C4.append([key, Index])
    elif (CardID == 4):
        C5.append([key, Index])
    # print(key, CardID, Index)

print("-------------1----------------")
print(C1)
print("--------------2---------------")
print(C2)
print("-------------3----------------")
print(C3)
print("--------------4---------------")
print(C4)
print("------------5-----------------")
print(C5)

# data = [C1, C2, C3, C4, C5]
# print(data)
with open('input.csv', 'a+', newline='') as file:
    writer = csv.writer(file)
    writer.writerows([["板卡1"]])
    writer.writerows(C1)
    writer.writerows([["板卡2"]])
    writer.writerows(C2)
    writer.writerows([["板卡3"]])
    writer.writerows(C3)
    writer.writerows([["板卡4"]])
    writer.writerows(C4)
    writer.writerows([["板卡5"]])
    writer.writerows(C5)
