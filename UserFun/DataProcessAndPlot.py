# -*- coding: gbk -*-
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
my_font = FontProperties(fname='C:\\Windows\\Fonts\\simsun.ttc', size=10)


class DataProcessAndPlot:
    @staticmethod  # 使用主机1 主机2的数据完成 image1和image2 两张图像
    def plot_data1():
        plt.style.use("seaborn-whitegrid")
        path1 = r'D:\greenhouse_control\data\image\image{}.png'.format("1")
        path2 = r'D:\greenhouse_control\data\image\image{}.png'.format("2")
        name1 = "./data/主机1_40184157.json"
        name2 = "./data/主机2_40184180.json"
        with open(name1, "r") as f1:
            w1 = json.load(f1)
        with open(name2, "r") as f2:
            w2 = json.load(f2)
        time_ = list(w1["温度1"][1])
        timeH = []
        for i in range(len(time_)):
            ss = time_[i]
            timeH.append(ss[11:13])
        # useNames = ["温度5", "温度26", "温度22", "温度23"]
        # 空气温度曲线1---温度5(主机1)，温度23(主机2)，温度26(主机1)，温度22(主机2)，
        d1 = np.array(list(map(float, w1["温度5"][0])))
        d2 = np.array(list(map(float, w1["温度26"][0])))
        d3 = np.array(list(map(float, w2["温度22"][0])))
        d4 = np.array(list(map(float, w2["温度23"][0])))
        value_Temp1 = mean_value(d1, d2, d3, d4)
        # 空气温度曲线2---温度1(主机1)，温度6(主机2)，温度17(主机1)，温度2(主机2)，
        d1 = np.array(list(map(float, w1["温度1"][0])))
        d2 = np.array(list(map(float, w2["温度6"][0])))
        d3 = np.array(list(map(float, w1["温度17"][0])))
        d4 = np.array(list(map(float, w2["温度2"][0])))
        value_Temp2 = mean_value(d1, d2, d3, d4)
        # 空气温度曲线3---温度23(主机1)，温度10(主机2)，温度31(主机1)，温度9(主机2)，
        d1 = np.array(list(map(float, w1["温度23"][0])))
        d2 = np.array(list(map(float, w2["温度10"][0])))
        d3 = np.array(list(map(float, w1["温度31"][0])))
        d4 = np.array(list(map(float, w2["温度9"][0])))
        value_Temp3 = mean_value(d1, d2, d3, d4)
        # 空气温度曲线4---温度15(主机1)，温度15(主机2)，温度3(主机1)，温度14(主机2)，
        d1 = np.array(list(map(float, w1["温度15"][0])))
        d2 = np.array(list(map(float, w2["温度15"][0])))
        d3 = np.array(list(map(float, w1["温度3"][0])))
        d4 = np.array(list(map(float, w2["温度14"][0])))
        value_Temp4 = mean_value(d1, d2, d3, d4)

        # 空气湿度曲线1---湿度5(主机1)，湿度23(主机2)，湿度26(主机1)，湿度22(主机2)，
        d1 = np.array(list(map(float, w1["湿度5"][0])))
        d2 = np.array(list(map(float, w1["湿度26"][0])))
        d3 = np.array(list(map(float, w2["湿度22"][0])))
        d4 = np.array(list(map(float, w2["湿度23"][0])))
        value_Humi1 = mean_value(d1, d2, d3, d4)
        # 空气湿度曲线2---湿度1(主机1)，湿度6(主机2)，湿度17(主机1)，湿度2(主机2)，
        d1 = np.array(list(map(float, w1["湿度1"][0])))
        d2 = np.array(list(map(float, w2["湿度6"][0])))
        d3 = np.array(list(map(float, w1["湿度17"][0])))
        d4 = np.array(list(map(float, w2["湿度2"][0])))
        value_Humi2 = mean_value(d1, d2, d3, d4)
        # 空气湿度曲线3---湿度23(主机1)，湿度10(主机2)，湿度31(主机1)，湿温度9(主机2)，
        d1 = np.array(list(map(float, w1["湿度23"][0])))
        d2 = np.array(list(map(float, w2["湿度10"][0])))
        d3 = np.array(list(map(float, w1["湿度31"][0])))
        d4 = np.array(list(map(float, w2["湿度9"][0])))
        value_Humi3 = mean_value(d1, d2, d3, d4)
        # 空气湿度曲线4---湿度15(主机1)，湿度15(主机2)，湿度3(主机1)，湿度14(主机2)，
        d1 = np.array(list(map(float, w1["湿度15"][0])))
        d2 = np.array(list(map(float, w2["湿度15"][0])))
        d3 = np.array(list(map(float, w1["湿度3"][0])))
        d4 = np.array(list(map(float, w2["湿度14"][0])))
        value_Humi4 = mean_value(d1, d2, d3, d4)
        # 绘制空气温度曲线
        y = [value_Temp1, value_Temp2, value_Temp3, value_Temp4]
        x = list(range(1, len(time_)+1))
        colors = ["blue", "g", "r", "pink", "yellow"]
        labels = ["0m ", "1m", "2m", "3m"]
        plt.figure()
        for i in range(4):
            plt.plot(x, y[i], color=colors[i], label=labels[i])
        plt.legend(frameon=True, fontsize=10)
        plt.ylabel("air temperature  $^\circ$C", fontsize=15)
        plt.xlabel("time /h ", fontsize=15)
        plt.xticks(x[::12], timeH[::12], rotation=45)
        plt.ylim(0, 60)
        # plt.show()
        plt.savefig(path1)
        plt.close()

        # 绘制 空气湿度曲线
        y = [value_Humi1, value_Humi2, value_Humi3, value_Humi4]
        x = list(range(1, len(time_) + 1))
        colors = ["blue", "g", "r", "pink", "yellow"]
        labels = ["0m ", "1m", "2m", "3m"]
        plt.figure()
        for i in range(4):
            plt.plot(x, y[i], color=colors[i], label=labels[i])
        plt.legend(frameon=True, fontsize=10)
        plt.ylabel("air humidness  %", fontsize=15)
        plt.xlabel("time /h ", fontsize=15)
        plt.xticks(x[::12], timeH[::12], rotation=45)
        plt.ylim(0, 100)
        plt.savefig(path2)
        plt.close()
        # plt.show()
        print("te test")

    @staticmethod  # 使用土壤北1、土壤北2 、土壤南1 和土壤南2 数据完成 image3和image4 两张图像
    def plot_data2():
        plt.style.use("seaborn-whitegrid")
        path3 = r'D:\greenhouse_control\data\image\image{}.png'.format("4")
        path4 = r'D:\greenhouse_control\data\image\image{}.png'.format("5")

        name1 = "./data/北部土壤传感器1_21043747.json"
        name2 = "./data/北部土壤传感器2_21043782.json"
        name3 = "./data/南部土壤传感器1_21043765.json"
        name4 = "./data/南部土壤传感器2_21043786.json"
        with open(name1, "r") as f1:
            n1 = json.load(f1)
        with open(name2, "r") as f2:
            n2 = json.load(f2)
        with open(name3, "r") as f1:
            s1 = json.load(f1)
        with open(name4, "r") as f2:
            s2 = json.load(f2)

        time_ = list(n1["温度1"][1])
        timeH = []
        for i in range(len(time_)):
            ss = time_[i]
            timeH.append(ss[11:13])  # 取出小时作为x轴坐标用
        # useNames = ["温度5", "温度26", "温度22", "温度23"]
        # 空气温度曲线1---温度1(北土1)，温度1(北土2)，温度1(南土1)，温度1(南土1)
        d1 = np.array(list(map(float, n1["温度1"][0])))
        d2 = np.array(list(map(float, n2["温度1"][0])))
        d3 = np.array(list(map(float, s1["温度1"][0])))
        d4 = np.array(list(map(float, s2["温度1"][0])))
        value_Temp1 = mean_value(d1, d2, d3, d4)
        # 空气温度曲线2---温度2(北土1)，温度2(北土2)，温度2(南土1)，温度2(南土1)，
        d1 = np.array(list(map(float, n1["温度2"][0])))
        d2 = np.array(list(map(float, n2["温度2"][0])))
        d3 = np.array(list(map(float, s1["温度2"][0])))
        d4 = np.array(list(map(float, s2["温度2"][0])))
        value_Temp2 = mean_value(d1, d2, d3, d4)
        # 空气温度曲线3---温度3(北土1)，温度3(北土2)，温度3(南土1)，温度3(南土1)，
        d1 = np.array(list(map(float, n1["温度3"][0])))
        d2 = np.array(list(map(float, n2["温度3"][0])))
        d3 = np.array(list(map(float, s1["温度3"][0])))
        d4 = np.array(list(map(float, s2["温度3"][0])))
        value_Temp3 = mean_value(d1, d2, d3, d4)
        # 空气温度曲线4---温度1(北土1)，温度1(北土2)，温度1(南土1)，温度1(南土1)，
        d1 = np.array(list(map(float, n1["温度4"][0])))
        d2 = np.array(list(map(float, n2["温度4"][0])))
        d3 = np.array(list(map(float, s1["温度4"][0])))
        d4 = np.array(list(map(float, s2["温度4"][0])))
        value_Temp4 = mean_value(d1, d2, d3, d4)

        # 空气温度曲线5---温度5(北土1)，温度5(北土2)，温度5(南土1)，温度5(南土1)，
        d1 = np.array(list(map(float, n1["温度5"][0])))
        d2 = np.array(list(map(float, n2["温度5"][0])))
        d3 = np.array(list(map(float, s1["温度5"][0])))
        d4 = np.array(list(map(float, s2["温度5"][0])))
        value_Temp5 = mean_value(d1, d2, d3, d4)

        # 空气湿度曲线1---湿度1(北土1)，湿度1(北土2)，湿度1(南土1)，湿度1(南土1)，
        d1 = np.array(list(map(float, n1["湿度1"][0])))
        d2 = np.array(list(map(float, n1["湿度1"][0])))
        d3 = np.array(list(map(float, s2["湿度1"][0])))
        d4 = np.array(list(map(float, s2["湿度1"][0])))
        value_Humi1 = mean_value(d1, d2, d3, d4)
        # 空气湿度曲线2---湿度2(北土1)，湿度2(北土2)，湿度2(南土1)，湿度2(南土1)，
        d1 = np.array(list(map(float, n1["湿度2"][0])))
        d2 = np.array(list(map(float, n2["湿度2"][0])))
        d3 = np.array(list(map(float, s1["湿度2"][0])))
        d4 = np.array(list(map(float, s2["湿度2"][0])))
        value_Humi2 = mean_value(d1, d2, d3, d4)
        # 空气湿度曲线3---湿度3(北土1)，湿度3(北土2)，湿度3(南土1)，湿度3(南土1)，
        d1 = np.array(list(map(float, n1["湿度3"][0])))
        d2 = np.array(list(map(float, n2["湿度3"][0])))
        d3 = np.array(list(map(float, s1["湿度3"][0])))
        d4 = np.array(list(map(float, s2["湿度3"][0])))
        value_Humi3 = mean_value(d1, d2, d3, d4)
        # 空气湿度曲线4---湿度4(北土1)，湿度4(北土2)，湿度4(南土1)，湿度4(南土1)，
        d1 = np.array(list(map(float, n1["湿度4"][0])))
        d2 = np.array(list(map(float, n2["湿度4"][0])))
        d3 = np.array(list(map(float, s1["湿度4"][0])))
        d4 = np.array(list(map(float, s2["湿度4"][0])))
        value_Humi4 = mean_value(d1, d2, d3, d4)
        # 空气湿度曲线5---湿度5(北土1)，湿度5(北土2)，湿度5(南土1)，湿度5(南土1)，
        d1 = np.array(list(map(float, n1["湿度5"][0])))
        d2 = np.array(list(map(float, n2["湿度5"][0])))
        d3 = np.array(list(map(float, s1["湿度5"][0])))
        d4 = np.array(list(map(float, s2["湿度5"][0])))
        value_Humi5 = mean_value(d1, d2, d3, d4)
        # 绘制空气温度曲线
        y = [value_Temp1, value_Temp2, value_Temp3, value_Temp4, value_Temp5]
        x = list(range(1, len(time_)+1))
        colors = ["blue", "g", "r", "pink", "yellow", "blank"]
        labels = ["1  ", "2", "3", "4", "5"]
        plt.figure()
        for i in range(5):
            plt.plot(x, y[i], color=colors[i], label=labels[i])
        plt.legend(frameon=True, fontsize=10)
        plt.ylabel("air temperature  $^\circ$C", fontsize=15)
        plt.xlabel("time /h ", fontsize=15)
        plt.xticks(x[::12], timeH[::12], rotation=45)
        plt.ylim(0, 60)
        plt.savefig(path3)
        plt.close()
    
        # 绘制 空气湿度曲线
        y = [value_Humi1, value_Humi2, value_Humi3, value_Humi4, value_Humi5]
        x = list(range(1, len(time_) + 1))
        colors = ["blue", "g", "r", "pink", "yellow"]
        labels = ["0 ", "1", "2", "3", "3"]
        plt.figure()
        for i in range(5):
            plt.plot(x, y[i], color=colors[i], label=labels[i])
        plt.legend(frameon=True, fontsize=10)
        plt.ylabel("air humidness  %", fontsize=15)
        plt.xlabel("time /h ", fontsize=15)
        plt.xticks(x[::12], timeH[::12], rotation=45)
        plt.ylim(0, 100)
        plt.savefig(path4)
        plt.close()

    @staticmethod  # 集中器数据完成 image5-image6 两张图像
    def plot_data3():
        plt.style.use("seaborn-whitegrid")
        path7 = r'D:\greenhouse_control\data\image\image{}.png'.format("3")
        path8 = r'D:\greenhouse_control\data\image\image{}.png'.format("6")

        name1 = "./data/集中器_20009680.json"

        with open(name1, "r") as f1:
            j = json.load(f1)
        time_ = list(j["CO2"][1])
        timeH = []
        for i in range(len(time_)):
            ss = time_[i]
            timeH.append(ss[11:13])  # 取出小时作为x轴坐标用
        x = list(range(1, len(time_) + 1))
        d1 = np.array(list(map(float, j["CO2"][0])))
        d2 = np.array(list(map(float, j["水箱1"][0])))
        d3 = np.array(list(map(float, j["水箱2"][0])))
        d4 = np.array(list(map(float, j["水箱3"][0])))
        d1 = np.flip(d1)
        d2 = np.flip(d2)
        d3 = np.flip(d3)
        d4 = np.flip(d4)
        timeH = np.flip(timeH)
        colors = ["blue", "g", "r", "pink", "yellow"]
        labels = ["0 ", "1", "2", "3", "3"]
        # CO2浓度曲线
        plt.figure()
        plt.plot(x, d1, color=colors[0], label=labels[1])
        plt.ylabel("CO2  /ppm", fontsize=15)
        plt.xlabel("time /h  ", fontsize=15)
        plt.xticks(x[::12], timeH[::12], rotation=60)
        plt.savefig(path7)
        plt.close()
        # 北墙恒温水箱温度曲线
        plt.figure()
        plt.plot(x, d2, color=colors[0], label=labels[1])
        plt.plot(x, d3, color=colors[1], label=labels[2])
        plt.plot(x, d4, color=colors[2], label=labels[3])
        plt.ylabel("Water tank temperature   $^\circ$C", fontsize=15)
        plt.xlabel("time /h ", fontsize=15)
        plt.xticks(x[::12], timeH[::12], rotation=45)
        plt.savefig(path8)
        plt.close()
        print(" -----------")

    @staticmethod  # 气象站数据完成 image7-image10 四张图像
    def plot_data4():
        plt.style.use("seaborn-whitegrid")
        path7 = r'D:\greenhouse_control\data\image\image{}.png'.format("7")
        path8 = r'D:\greenhouse_control\data\image\image{}.png'.format("8")
        path9 = r'D:\greenhouse_control\data\image\image{}.png'.format("9")
        path10 = r'D:\greenhouse_control\data\image\image{}.png'.format("10")
    
        name1 = "./data/气象站_40133062.json"
    
        with open(name1, "r") as f1:
            q1 = json.load(f1)
        time_ = list(q1["光照"][1])
        timeH = []
        for i in range(len(time_)):
            ss = time_[i]
            timeH.append(ss[11:16])  # 取出小时作为x轴坐标用
        x = list(range(1, len(time_) + 1))
        d1 = np.array(list(map(float, q1["光照"][0])))
        d2 = np.array(list(map(float, q1["空气温度"][0])))
        d3 = np.array(list(map(float, q1["空气湿度"][0])))
        d4 = np.array(list(map(float, q1["风速"][0])))
        d1 = np.flip(d1)
        d2 = np.flip(d2)
        d3 = np.flip(d3)
        d4 = np.flip(d4)
        timeH = np.flip(timeH)
        colors = ["blue", "g", "r", "pink", "yellow"]
        labels = ["0 ", "1", "2", "3", "3"]
        # 光照强度曲线
        plt.figure()
        plt.plot(x, d1, color=colors[0], label=labels[1])
        plt.ylabel("light intensity /LUX", fontsize=15)
        plt.xlabel("time /h  ", fontsize=15)
        plt.xticks(x[::4], timeH[::4], rotation=45)
        plt.savefig(path7)
        # 环境温度曲线
        plt.figure()
        plt.plot(x, d2, color=colors[0], label=labels[1])
        plt.ylabel("outdoor temperature  $^\circ$C", fontsize=15)
        plt.xlabel("time /h ", fontsize=15)
        plt.xticks(x[::4], timeH[::4], rotation=45)
        plt.savefig(path8)
        plt.close()
        # 环境湿度曲线
        plt.figure()
        plt.plot(x, d3, color=colors[0], label=labels[1])
        plt.ylabel("outdoor humidity   %", fontsize=15)
        plt.xlabel("time /h ", fontsize=15)
        plt.xticks(x[::4], timeH[::4], rotation=45)
        plt.savefig(path9)
        plt.close()
        # 环境风速曲线
        plt.figure()
        plt.plot(x, d4, color=colors[0], label=labels[1])
        plt.ylabel("wind speed   m/s", fontsize=15)
        plt.xlabel("time /h ", fontsize=15)
        plt.xticks(x[::4], timeH[::4], rotation=45)
        plt.savefig(path10)
        plt.close()
        print(" -----------")
    

def mean_value(d1, d2, d3, d4):
    k = [30, 50, 80, 100, 130, 150, 180, 200, 250]  # 找若干个点检测传感器温度
    Sum = Num = 0
    if np.unique(d1[k]).size > 4:  # 小于4，至少有4-6小时数据未发生变化，一般情况是传感器损坏了，节点测量值为0.0
        Sum = Sum + d1
        Num = Num + 1
    if np.unique(d2[k]).size > 4:
        Sum = Sum + d1
        Num = Num + 1
    if np.unique(d3[k]).size > 4:
        Sum = Sum + d1
        Num = Num + 1
    if np.unique(d4[k]).size > 4:
        Sum = Sum + d1
        Num = Num + 1
    va = Sum / Num
    return va
#
#
# if __name__ == "__main__":
#     s = DataProcessAndPlot()
#     s.plot_data1()
#     s.plot_data2()
#     s.plot_data3()
#     DataProcessAndPlot.plot_data3()
#     s.plot_data4()
#     print("ff test")
