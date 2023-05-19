# -*- coding: gbk -*-
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
my_font = FontProperties(fname='C:\\Windows\\Fonts\\simsun.ttc', size=10)


class DataProcessAndPlot:
    @staticmethod  # ʹ������1 ����2��������� image1��image2 ����ͼ��
    def plot_data1():
        plt.style.use("seaborn-whitegrid")
        path1 = r'D:\greenhouse_control\data\image\image{}.png'.format("1")
        path2 = r'D:\greenhouse_control\data\image\image{}.png'.format("2")
        name1 = "./data/����1_40184157.json"
        name2 = "./data/����2_40184180.json"
        with open(name1, "r") as f1:
            w1 = json.load(f1)
        with open(name2, "r") as f2:
            w2 = json.load(f2)
        time_ = list(w1["�¶�1"][1])
        timeH = []
        for i in range(len(time_)):
            ss = time_[i]
            timeH.append(ss[11:13])
        # useNames = ["�¶�5", "�¶�26", "�¶�22", "�¶�23"]
        # �����¶�����1---�¶�5(����1)���¶�23(����2)���¶�26(����1)���¶�22(����2)��
        d1 = np.array(list(map(float, w1["�¶�5"][0])))
        d2 = np.array(list(map(float, w1["�¶�26"][0])))
        d3 = np.array(list(map(float, w2["�¶�22"][0])))
        d4 = np.array(list(map(float, w2["�¶�23"][0])))
        value_Temp1 = mean_value(d1, d2, d3, d4)
        # �����¶�����2---�¶�1(����1)���¶�6(����2)���¶�17(����1)���¶�2(����2)��
        d1 = np.array(list(map(float, w1["�¶�1"][0])))
        d2 = np.array(list(map(float, w2["�¶�6"][0])))
        d3 = np.array(list(map(float, w1["�¶�17"][0])))
        d4 = np.array(list(map(float, w2["�¶�2"][0])))
        value_Temp2 = mean_value(d1, d2, d3, d4)
        # �����¶�����3---�¶�23(����1)���¶�10(����2)���¶�31(����1)���¶�9(����2)��
        d1 = np.array(list(map(float, w1["�¶�23"][0])))
        d2 = np.array(list(map(float, w2["�¶�10"][0])))
        d3 = np.array(list(map(float, w1["�¶�31"][0])))
        d4 = np.array(list(map(float, w2["�¶�9"][0])))
        value_Temp3 = mean_value(d1, d2, d3, d4)
        # �����¶�����4---�¶�15(����1)���¶�15(����2)���¶�3(����1)���¶�14(����2)��
        d1 = np.array(list(map(float, w1["�¶�15"][0])))
        d2 = np.array(list(map(float, w2["�¶�15"][0])))
        d3 = np.array(list(map(float, w1["�¶�3"][0])))
        d4 = np.array(list(map(float, w2["�¶�14"][0])))
        value_Temp4 = mean_value(d1, d2, d3, d4)

        # ����ʪ������1---ʪ��5(����1)��ʪ��23(����2)��ʪ��26(����1)��ʪ��22(����2)��
        d1 = np.array(list(map(float, w1["ʪ��5"][0])))
        d2 = np.array(list(map(float, w1["ʪ��26"][0])))
        d3 = np.array(list(map(float, w2["ʪ��22"][0])))
        d4 = np.array(list(map(float, w2["ʪ��23"][0])))
        value_Humi1 = mean_value(d1, d2, d3, d4)
        # ����ʪ������2---ʪ��1(����1)��ʪ��6(����2)��ʪ��17(����1)��ʪ��2(����2)��
        d1 = np.array(list(map(float, w1["ʪ��1"][0])))
        d2 = np.array(list(map(float, w2["ʪ��6"][0])))
        d3 = np.array(list(map(float, w1["ʪ��17"][0])))
        d4 = np.array(list(map(float, w2["ʪ��2"][0])))
        value_Humi2 = mean_value(d1, d2, d3, d4)
        # ����ʪ������3---ʪ��23(����1)��ʪ��10(����2)��ʪ��31(����1)��ʪ�¶�9(����2)��
        d1 = np.array(list(map(float, w1["ʪ��23"][0])))
        d2 = np.array(list(map(float, w2["ʪ��10"][0])))
        d3 = np.array(list(map(float, w1["ʪ��31"][0])))
        d4 = np.array(list(map(float, w2["ʪ��9"][0])))
        value_Humi3 = mean_value(d1, d2, d3, d4)
        # ����ʪ������4---ʪ��15(����1)��ʪ��15(����2)��ʪ��3(����1)��ʪ��14(����2)��
        d1 = np.array(list(map(float, w1["ʪ��15"][0])))
        d2 = np.array(list(map(float, w2["ʪ��15"][0])))
        d3 = np.array(list(map(float, w1["ʪ��3"][0])))
        d4 = np.array(list(map(float, w2["ʪ��14"][0])))
        value_Humi4 = mean_value(d1, d2, d3, d4)
        # ���ƿ����¶�����
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

        # ���� ����ʪ������
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

    @staticmethod  # ʹ��������1��������2 ��������1 ��������2 ������� image3��image4 ����ͼ��
    def plot_data2():
        plt.style.use("seaborn-whitegrid")
        path3 = r'D:\greenhouse_control\data\image\image{}.png'.format("4")
        path4 = r'D:\greenhouse_control\data\image\image{}.png'.format("5")

        name1 = "./data/��������������1_21043747.json"
        name2 = "./data/��������������2_21043782.json"
        name3 = "./data/�ϲ�����������1_21043765.json"
        name4 = "./data/�ϲ�����������2_21043786.json"
        with open(name1, "r") as f1:
            n1 = json.load(f1)
        with open(name2, "r") as f2:
            n2 = json.load(f2)
        with open(name3, "r") as f1:
            s1 = json.load(f1)
        with open(name4, "r") as f2:
            s2 = json.load(f2)

        time_ = list(n1["�¶�1"][1])
        timeH = []
        for i in range(len(time_)):
            ss = time_[i]
            timeH.append(ss[11:13])  # ȡ��Сʱ��Ϊx��������
        # useNames = ["�¶�5", "�¶�26", "�¶�22", "�¶�23"]
        # �����¶�����1---�¶�1(����1)���¶�1(����2)���¶�1(����1)���¶�1(����1)
        d1 = np.array(list(map(float, n1["�¶�1"][0])))
        d2 = np.array(list(map(float, n2["�¶�1"][0])))
        d3 = np.array(list(map(float, s1["�¶�1"][0])))
        d4 = np.array(list(map(float, s2["�¶�1"][0])))
        value_Temp1 = mean_value(d1, d2, d3, d4)
        # �����¶�����2---�¶�2(����1)���¶�2(����2)���¶�2(����1)���¶�2(����1)��
        d1 = np.array(list(map(float, n1["�¶�2"][0])))
        d2 = np.array(list(map(float, n2["�¶�2"][0])))
        d3 = np.array(list(map(float, s1["�¶�2"][0])))
        d4 = np.array(list(map(float, s2["�¶�2"][0])))
        value_Temp2 = mean_value(d1, d2, d3, d4)
        # �����¶�����3---�¶�3(����1)���¶�3(����2)���¶�3(����1)���¶�3(����1)��
        d1 = np.array(list(map(float, n1["�¶�3"][0])))
        d2 = np.array(list(map(float, n2["�¶�3"][0])))
        d3 = np.array(list(map(float, s1["�¶�3"][0])))
        d4 = np.array(list(map(float, s2["�¶�3"][0])))
        value_Temp3 = mean_value(d1, d2, d3, d4)
        # �����¶�����4---�¶�1(����1)���¶�1(����2)���¶�1(����1)���¶�1(����1)��
        d1 = np.array(list(map(float, n1["�¶�4"][0])))
        d2 = np.array(list(map(float, n2["�¶�4"][0])))
        d3 = np.array(list(map(float, s1["�¶�4"][0])))
        d4 = np.array(list(map(float, s2["�¶�4"][0])))
        value_Temp4 = mean_value(d1, d2, d3, d4)

        # �����¶�����5---�¶�5(����1)���¶�5(����2)���¶�5(����1)���¶�5(����1)��
        d1 = np.array(list(map(float, n1["�¶�5"][0])))
        d2 = np.array(list(map(float, n2["�¶�5"][0])))
        d3 = np.array(list(map(float, s1["�¶�5"][0])))
        d4 = np.array(list(map(float, s2["�¶�5"][0])))
        value_Temp5 = mean_value(d1, d2, d3, d4)

        # ����ʪ������1---ʪ��1(����1)��ʪ��1(����2)��ʪ��1(����1)��ʪ��1(����1)��
        d1 = np.array(list(map(float, n1["ʪ��1"][0])))
        d2 = np.array(list(map(float, n1["ʪ��1"][0])))
        d3 = np.array(list(map(float, s2["ʪ��1"][0])))
        d4 = np.array(list(map(float, s2["ʪ��1"][0])))
        value_Humi1 = mean_value(d1, d2, d3, d4)
        # ����ʪ������2---ʪ��2(����1)��ʪ��2(����2)��ʪ��2(����1)��ʪ��2(����1)��
        d1 = np.array(list(map(float, n1["ʪ��2"][0])))
        d2 = np.array(list(map(float, n2["ʪ��2"][0])))
        d3 = np.array(list(map(float, s1["ʪ��2"][0])))
        d4 = np.array(list(map(float, s2["ʪ��2"][0])))
        value_Humi2 = mean_value(d1, d2, d3, d4)
        # ����ʪ������3---ʪ��3(����1)��ʪ��3(����2)��ʪ��3(����1)��ʪ��3(����1)��
        d1 = np.array(list(map(float, n1["ʪ��3"][0])))
        d2 = np.array(list(map(float, n2["ʪ��3"][0])))
        d3 = np.array(list(map(float, s1["ʪ��3"][0])))
        d4 = np.array(list(map(float, s2["ʪ��3"][0])))
        value_Humi3 = mean_value(d1, d2, d3, d4)
        # ����ʪ������4---ʪ��4(����1)��ʪ��4(����2)��ʪ��4(����1)��ʪ��4(����1)��
        d1 = np.array(list(map(float, n1["ʪ��4"][0])))
        d2 = np.array(list(map(float, n2["ʪ��4"][0])))
        d3 = np.array(list(map(float, s1["ʪ��4"][0])))
        d4 = np.array(list(map(float, s2["ʪ��4"][0])))
        value_Humi4 = mean_value(d1, d2, d3, d4)
        # ����ʪ������5---ʪ��5(����1)��ʪ��5(����2)��ʪ��5(����1)��ʪ��5(����1)��
        d1 = np.array(list(map(float, n1["ʪ��5"][0])))
        d2 = np.array(list(map(float, n2["ʪ��5"][0])))
        d3 = np.array(list(map(float, s1["ʪ��5"][0])))
        d4 = np.array(list(map(float, s2["ʪ��5"][0])))
        value_Humi5 = mean_value(d1, d2, d3, d4)
        # ���ƿ����¶�����
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
    
        # ���� ����ʪ������
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

    @staticmethod  # ������������� image5-image6 ����ͼ��
    def plot_data3():
        plt.style.use("seaborn-whitegrid")
        path7 = r'D:\greenhouse_control\data\image\image{}.png'.format("3")
        path8 = r'D:\greenhouse_control\data\image\image{}.png'.format("6")

        name1 = "./data/������_20009680.json"

        with open(name1, "r") as f1:
            j = json.load(f1)
        time_ = list(j["CO2"][1])
        timeH = []
        for i in range(len(time_)):
            ss = time_[i]
            timeH.append(ss[11:13])  # ȡ��Сʱ��Ϊx��������
        x = list(range(1, len(time_) + 1))
        d1 = np.array(list(map(float, j["CO2"][0])))
        d2 = np.array(list(map(float, j["ˮ��1"][0])))
        d3 = np.array(list(map(float, j["ˮ��2"][0])))
        d4 = np.array(list(map(float, j["ˮ��3"][0])))
        d1 = np.flip(d1)
        d2 = np.flip(d2)
        d3 = np.flip(d3)
        d4 = np.flip(d4)
        timeH = np.flip(timeH)
        colors = ["blue", "g", "r", "pink", "yellow"]
        labels = ["0 ", "1", "2", "3", "3"]
        # CO2Ũ������
        plt.figure()
        plt.plot(x, d1, color=colors[0], label=labels[1])
        plt.ylabel("CO2  /ppm", fontsize=15)
        plt.xlabel("time /h  ", fontsize=15)
        plt.xticks(x[::12], timeH[::12], rotation=60)
        plt.savefig(path7)
        plt.close()
        # ��ǽ����ˮ���¶�����
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

    @staticmethod  # ����վ������� image7-image10 ����ͼ��
    def plot_data4():
        plt.style.use("seaborn-whitegrid")
        path7 = r'D:\greenhouse_control\data\image\image{}.png'.format("7")
        path8 = r'D:\greenhouse_control\data\image\image{}.png'.format("8")
        path9 = r'D:\greenhouse_control\data\image\image{}.png'.format("9")
        path10 = r'D:\greenhouse_control\data\image\image{}.png'.format("10")
    
        name1 = "./data/����վ_40133062.json"
    
        with open(name1, "r") as f1:
            q1 = json.load(f1)
        time_ = list(q1["����"][1])
        timeH = []
        for i in range(len(time_)):
            ss = time_[i]
            timeH.append(ss[11:16])  # ȡ��Сʱ��Ϊx��������
        x = list(range(1, len(time_) + 1))
        d1 = np.array(list(map(float, q1["����"][0])))
        d2 = np.array(list(map(float, q1["�����¶�"][0])))
        d3 = np.array(list(map(float, q1["����ʪ��"][0])))
        d4 = np.array(list(map(float, q1["����"][0])))
        d1 = np.flip(d1)
        d2 = np.flip(d2)
        d3 = np.flip(d3)
        d4 = np.flip(d4)
        timeH = np.flip(timeH)
        colors = ["blue", "g", "r", "pink", "yellow"]
        labels = ["0 ", "1", "2", "3", "3"]
        # ����ǿ������
        plt.figure()
        plt.plot(x, d1, color=colors[0], label=labels[1])
        plt.ylabel("light intensity /LUX", fontsize=15)
        plt.xlabel("time /h  ", fontsize=15)
        plt.xticks(x[::4], timeH[::4], rotation=45)
        plt.savefig(path7)
        # �����¶�����
        plt.figure()
        plt.plot(x, d2, color=colors[0], label=labels[1])
        plt.ylabel("outdoor temperature  $^\circ$C", fontsize=15)
        plt.xlabel("time /h ", fontsize=15)
        plt.xticks(x[::4], timeH[::4], rotation=45)
        plt.savefig(path8)
        plt.close()
        # ����ʪ������
        plt.figure()
        plt.plot(x, d3, color=colors[0], label=labels[1])
        plt.ylabel("outdoor humidity   %", fontsize=15)
        plt.xlabel("time /h ", fontsize=15)
        plt.xticks(x[::4], timeH[::4], rotation=45)
        plt.savefig(path9)
        plt.close()
        # ������������
        plt.figure()
        plt.plot(x, d4, color=colors[0], label=labels[1])
        plt.ylabel("wind speed   m/s", fontsize=15)
        plt.xlabel("time /h ", fontsize=15)
        plt.xticks(x[::4], timeH[::4], rotation=45)
        plt.savefig(path10)
        plt.close()
        print(" -----------")
    

def mean_value(d1, d2, d3, d4):
    k = [30, 50, 80, 100, 130, 150, 180, 200, 250]  # �����ɸ����⴫�����¶�
    Sum = Num = 0
    if np.unique(d1[k]).size > 4:  # С��4��������4-6Сʱ����δ�����仯��һ������Ǵ��������ˣ��ڵ����ֵΪ0.0
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
