import csv
import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
input(
    "=这是一个获取io表的软件=\n"
    "=将本exe放到软件Config目录中会获取‘input_params.dat’‘output_params.dat’然后按照卡号分好io名字和针脚=\n"
    "=回车开始字符匹配=")
############################################################################################################
print("------------read-----------------")
try:
    with open('input_params.dat', 'r', encoding="utf-8") as file:
        my_dict_input = file.read()

    with open('output_params.dat', 'r', encoding="utf-8") as file:
        my_dict_output = file.read()

    my_dict_input = eval(my_dict_input)
    my_dict_output = eval(my_dict_output)
    print("------------read end-----------------")

    ############################################################################################################
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
    print("Running successfully, you can see two new files in the current directory, Goodbye!")

except Exception as err:
    print("Sorry for the following error" + str(err))
finally:
    input("=已经结束了=")