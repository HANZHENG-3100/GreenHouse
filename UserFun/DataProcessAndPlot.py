# -*- coding: gbk -*-
import json
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
my_font = FontProperties(fname='C:\\Windows\\Fonts\\simsun.ttc', size=10)


class DataProcessAndPlot:
    @staticmethod  # ʹ������1 ����2��������� image1��image2 ����ͼ��
    def plot_data1():
        plt.style.use("seaborn-whitegrid")
        currPath = os.getcwd()
        path1 = r'{}\data\image\image{}.png'.format(currPath, "1")
        path2 = r'{}\data\image\image{}.png'.format(currPath, "2")
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
            timeH.append(ss[11:16])
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
        labels = ["2.8m ", "1m", "0.2m", "0.1m"]
        plt.figure()
        for i in range(4):
            plt.plot(x, y[i], color=colors[i], label=labels[i])
        plt.legend(frameon=True, fontsize=10)
        plt.ylabel("air temperature  $^\circ$C", fontsize=15)
        plt.xlabel("time /h ", fontsize=15)
        plt.xticks(x[::12], timeH[::12], rotation=45)
        plt.ylim(0, 60)
        # plt.show()
        plt.subplots_adjust(bottom=0.15)
        plt.savefig(path1)
        plt.close()

        # ���� ����ʪ������
        y = [value_Humi1, value_Humi2, value_Humi3, value_Humi4]  # ȡ������

        x = list(range(1, len(time_) + 1))
        colors = ["blue", "g", "r", "pink", "yellow"]
        labels = ["2.8m ", "1m", "0.2m", "0.1m"]
        plt.figure()
        for i in range(4):
            plt.plot(x, y[i], color=colors[i], label=labels[i])
        plt.legend(frameon=True, fontsize=10)
        plt.ylabel("air humidness  %", fontsize=15)
        plt.xlabel("time /h ", fontsize=15)
        plt.xticks(x[::12], timeH[::12], rotation=45)
        plt.ylim(0, 100)
        plt.subplots_adjust(bottom=0.15)
        plt.savefig(path2)
        plt.close()
        # plt.show()
        print("te test")

    @staticmethod  # ʹ��������1��������2 ��������1 ��������2 ������� image4��image5 ����ͼ��
    def plot_data2():
        plt.style.use("seaborn-whitegrid")
        currPath = os.getcwd()
        path3 = r'{}\data\image\image{}.png'.format(currPath, "4")
        path4 = r'{}\data\image\image{}.png'.format(currPath, "5")

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
            timeH.append(ss[11:16])  # ȡ��Сʱ��Ϊx��������
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
        # ���������¶�����
        y = [value_Temp1, value_Temp2, value_Temp3, value_Temp4, value_Temp5]
        x = list(range(1, len(time_)+1))
        colors = ["blue", "g", "r", "pink", "yellow", "blank"]
        labels = ["1  ", "2", "3", "4", "5"]
        plt.figure()
        for i in range(5):
            plt.plot(x, y[i], color=colors[i], label=labels[i])
            print("{}test".format(i))
        plt.legend(frameon=True, fontsize=10)
        plt.ylabel("soil temperature  $^\circ$C", fontsize=15)
        plt.xlabel("time /h ", fontsize=15)
        plt.xticks(x[::24], timeH[::24], rotation=45)   # ÿ24�����ݲ���һ��
        y_min = round(min([min(y[0]), min(y[1]), min(y[2]), min(y[3]), min(y[4])]))
        y_max = round(max([max(y[0]), max(y[1]), max(y[2]), max(y[3]), max(y[4])]))
        plt.ylim(y_min-5, y_max+5)
        plt.subplots_adjust(bottom=0.15)
        plt.savefig(path3)  # �洢ͼ��
        plt.close()
    
        # ��������ʪ������
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
        plt.xticks(x[::24], timeH[::24], rotation=45)
        y_min = round(min([min(y[0]), min(y[1]), min(y[2]), min(y[3]), min(y[4])]))
        y_max = round(max([max(y[0]), max(y[1]), max(y[2]), max(y[3]), max(y[4])]))
        plt.ylim(y_min-10, y_max+10)
        # plt.axis("equal")
        plt.subplots_adjust(bottom=0.15)
        plt.savefig(path4)
        plt.close()

    @staticmethod  # ������������� image3,image6 ����ͼ��
    def plot_data3():
        plt.style.use("seaborn-whitegrid")
        currPath = os.getcwd()
        path7 = r'{}\data\image\image{}.png'.format(currPath, "3")
        path8 = r'{}\data\image\image{}.png'.format(currPath, "6")

        name1 = "./data/������_20009680.json"

        with open(name1, "r") as f1:
            j = json.load(f1)
        time_ = list(j["CO2"][1])
        timeH = []
        for i in range(len(time_)):
            ss = time_[i]
            timeH.append(ss[11:16])  # ȡ��Сʱ��Ϊx��������
        x = list(range(1, len(time_) + 1))
        d1 = np.array(list(map(float, j["CO2"][0])))
        d2 = np.array(list(map(float, j["ˮ��1"][0])))
        d3 = np.array(list(map(float, j["ˮ��2"][0])))
        d4 = np.array(list(map(float, j["ˮ��3"][0])))
        d1 = np.flip(d1)
        d2 = np.flip(d2)
        d3 = np.flip(d3)
        d4 = np.flip(d4)
        d1 = mean_value_one(d1)
        d2 = mean_value_one(d2)
        d3 = mean_value_one(d3)
        d4 = mean_value_one(d4)
        timeH = np.flip(timeH)
        colors = ["blue", "g", "r", "pink", "yellow"]
        labels = ["0 ", "1", "2", "3", "3"]
        # CO2Ũ������
        plt.figure()
        plt.plot(x, d1, color=colors[0], label=labels[1])
        plt.ylabel("CO2  /ppm", fontsize=15)
        plt.xlabel("time /h  ", fontsize=15)
        plt.xticks(x[::24], timeH[::24], rotation=60)
        plt.subplots_adjust(bottom=0.15)
        plt.savefig(path7)
        plt.close()
        # ��ǽ����ˮ���¶�����
        plt.figure()
        plt.plot(x, d2, color=colors[0], label=labels[1])
        plt.plot(x, d3, color=colors[1], label=labels[2])
        plt.plot(x, d4, color=colors[2], label=labels[3])
        plt.ylabel("Water tank temperature   $^\circ$C", fontsize=15)
        plt.xlabel("time /h ", fontsize=15)
        plt.xticks(x[::24], timeH[::24], rotation=50)
        plt.subplots_adjust(bottom=0.15)
        plt.savefig(path8)
        plt.close()
        print(" -----------")

    @staticmethod  # ����վ������� image7,image8,image9,image10 ����ͼ��
    def plot_data4():
        plt.style.use("seaborn-whitegrid")
        currPath = os.getcwd()
        path7 = r'{}\data\image\image{}.png'.format(currPath, "7")
        path8 = r'{}\data\image\image{}.png'.format(currPath, "8")
        path9 = r'{}\data\image\image{}.png'.format(currPath, "9")
        path10 = r'{}\data\image\image{}.png'.format(currPath, "10")
    
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
        d1 = mean_value_one(d1)
        d2 = mean_value_one(d2)
        d3 = mean_value_one(d3)
        d4 = mean_value_one(d4)
        timeH = np.flip(timeH)
        colors = ["blue", "g", "r", "pink", "yellow"]
        labels = ["0 ", "1", "2", "3", "3"]
        # ����ǿ������
        plt.figure()
        fig = plt.plot(x, d1, color=colors[0], label=labels[1])
        plt.ylabel("light intensity /LUX", fontsize=15)
        plt.xlabel("time /h  ", fontsize=15)
        plt.xticks(x[::24], timeH[::24], rotation=45)
        plt.subplots_adjust(bottom=0.15)
        plt.savefig(path7)
        # �����¶�����
        plt.figure()
        plt.plot(x, d2, color=colors[0], label=labels[1])
        plt.ylabel("outdoor temperature  $^\circ$C", fontsize=15)
        plt.xlabel("time /h ", fontsize=15)
        plt.xticks(x[::24], timeH[::24], rotation=45)
        plt.subplots_adjust(bottom=0.15)
        plt.savefig(path8)
        plt.close()
        # ����ʪ������
        plt.figure()
        plt.plot(x, d3, color=colors[0], label=labels[1])
        plt.ylabel("outdoor humidity   %", fontsize=15)
        plt.xlabel("time /h ", fontsize=15)
        plt.xticks(x[::24], timeH[::24], rotation=45)
        plt.subplots_adjust(bottom=0.15)
        plt.savefig(path9)
        plt.close()
        # ������������
        plt.figure()
        plt.plot(x, d4, color=colors[0], label=labels[1])
        plt.ylabel("wind speed   m/s", fontsize=15)
        plt.xlabel("time /h ", fontsize=15)
        plt.xticks(x[::24], timeH[::24], rotation=45)
        plt.subplots_adjust(bottom=0.15)
        plt.savefig(path10)
        plt.close()
        print(" -----------")
    

def mean_value(d1, d2, d3, d4):
    k = [30, 50, 80, 100, 130, 150, 180, 200, 250]  # �����ɸ����⴫�����¶�
    Sum = [0]
    Num = 0
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
    if Num == 0:
        return d1   # �˴��и�bug
    va = Sum / Num
    for i in range(3, len(va)-3):
        va[i] =(va[i-2]+va[i-1]+va[i]+va[i+1]+va[i+2])/5  # ��ֵ�˲�
    return va


def mean_value_one(d):
    va = d
    for i in range(3, len(va)-3):
        va[i] =(va[i-2]+va[i-1]+va[i]+va[i+1]+va[i+2])/5
    return va


if __name__ == "__main__":
    print(os.getcwd())  # ��ʾ��ǰ·��
    os.chdir('../')
    DataProcessAndPlot.plot_data1()
    DataProcessAndPlot.plot_data2()
    DataProcessAndPlot.plot_data3()
    DataProcessAndPlot.plot_data4()
    print("ff test")
