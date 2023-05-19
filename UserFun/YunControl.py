import threading
import time

import numpy as np
import requests
import json
import urllib3
import datetime
import matplotlib.pyplot as plt
from UserFun.DataProcessAndPlot import DataProcessAndPlot


class YunControl:
    # noinspection SpellCheckingInspection
    def __init__(self):
        urllib3.disable_warnings()  # 忽略https安全证书的验证
        self.url_yun = "http://www.0531yun.com/"  # 建大仁科综合环境监控云平台地址
        self.ID = "h211222yqhz"  # 云服务器登录账号
        self.PW = "h211222yqhz"  # 云服务器登录密码
        self.deviceAddr = {'气象站': "40133062",
                           '集中器': "20009680",
                           '对照土壤': "21043744",
                           '北部土壤传感器1': "21043747",
                           '北部土壤传感器2': "21043782",
                           '南部土壤传感器1': "21043765",
                           '南部土壤传感器2': "21043786",
                           '主机1': "40184157",
                           '主机2': "40184180",
                           '网络继电器1': "40261493",
                           '网络继电器2': "40261505",
                           '网络继电器3': "40261506",
                           '网络继电器4': "40261512",
                           '网络继电器5': "40261513"
                           }
        self.addr_weather_station = "40133062"       # 气象站设备地址
        self.addr_concentrator = "20009680"          # 集中器地址            数据6个 甲烷、氮气、水箱123、CO2浓度
        self.Addr_Comparison_soil = "21043744"       # 对照土壤传感器       （5个温度值，5个湿度值）
        self.addr_northern_soil1 = "21043747"        # 北部土壤传感器1      （5个温度值，5个湿度值）
        self.addr_northern_soil2 = "21043782"        # 北部土壤传感器2      （5个温度值，5个湿度值）
        self.addr_southern_soil1 = "21043765"        # 南部土壤传感器1      （5个温度值，5个湿度值）
        self.addr_southern_soil2 = "21043786"        # 南部土壤传感器2      （5个温度值，5个湿度值）
        self.addr_host1 = "40184157"                 # 主机1地址            （32组温湿度）
        self.addr_host2 = "40184180"                 # 主机2地址            （29组温湿度） 不确定

        self.addr_relay1 = "40261493"                # 网络继电器1地址
        self.addr_relay2 = "40261505"                # 网络继电器2地址
        self.addr_relay3 = "40261506"                # 网络继电器3地址
        self.addr_relay4 = "40261512"                # 网络继电器4地址
        self.addr_relay5 = "40261513"                # 网络继电器5地址(未用)

        self.delay_time = 2                          # 程序运行时间间隔，由传感器采集频率决定

        self.file_list = ['./data/主机1_40184157.json', './data/主机2_40184180.json',
                          './data/南部土壤传感器1_21043765.json', './data/南部土壤传感器1_21043765.json',
                          './data/北部土壤传感器1_21043747.json', './data/北部土壤传感器1_21043747.json',
                          './data/气象站_40133062.json', './data/集中器_20009680.json']
        self.relay_command = {1: 1, 2: 1, 3: 1, 4: 0, 5: 0, 6: 0, 7: 1, 8: 1}  # 继电器控制初始状态  0灯亮 闭合  1灯灭 断开
        self.relay_num = {1, 2, 3, 4, 5, 6, 7, 8}
        # self.relay_num = {'1', '2', '3', '4', '5', '6', '7', '8'}
        self.air_temperature_buffer = {}  # 存储临时环境数据
        self.air_humidity_buffer = {}
        self.soil_temperature_buffer = {}  #
        self.soil_humidity_buffer = {}

        self.headers = ""
        self.token_expiration_time = 0.0
        self.token_time = 0.0
    #  获取传感器历史数据 deviceAddr=主机地址, nodeId=传感器因子号, startTime, endTime时间格式：YYYY-MM-dd HH:mm:ss
    #  使用接口获取历史数据时，每分钟只能执行6次，超出次数会被拒绝。

    def get_history_data_withoutThreads(self, deviceAddr, startTime, endTime, nodeId=-1):
        self.check_token()  # 检测token是否过期
        iid = list(self.deviceAddr.values()).index(deviceAddr)
        name = list(self.deviceAddr.keys())[iid]  # name存储地址对应的中文名称
        url = self.url_yun + "api/data/historyList"
        # params 构建表单
        params = {"deviceAddr": int(deviceAddr), "nodeId": nodeId, "startTime": startTime, "endTime": endTime}
        r = requests.get(url=url, headers=self.headers, params=params)
        p = json.loads(r.content)  # 将json字符串转换为python dict对象
        if p['code'] == 1000:
            # print(name + "请求数据成功！")
            if p['data']:  # 正常获取数据后，此项非空
                data = p['data']  # here data is a list
                print(name+"历史数据下载成功！")
            else:
                print(name + "无历史数据,请检查近期传感器连接情况。")
                return
        else:
            print(name+"请求数据失败，请查看网络通信。\n")
            print(str(p["code"])+"  "+ p["message"])
            return
        deviceAddr = str(data[0]['deviceAddr'])  # 取地址信息
        # 构建存储时的文件名称
        # filename = "{0}_{1}_{2}-{3}".format(name, deviceAddr, startTime, endTime)
        filename = "{0}_{1}".format(name, deviceAddr)  # 简化文件名
        filename = filename.replace(" ", "_")
        filename = filename.replace(":", "-")
        filename = "./data/{0}.json".format(filename)
        # self.file_list.append(filename)
        # 解析数据并存储到文件
        # f = open(filename, 'w')  # 属性w 打开一个文件只写，无则新建，有则重写
        # for i in range(len(data)):  #
        #     index = "{0}-{1}".format(data[i]['data'][0]['registerName'],
        #                              data[i]['nodeId'])  # 命名规则 甲烷-1-1 ：名称-节点号-因子寄存器0/1
        #     value = data[i]['data'][0]['value']  # 取得测点的测量值
        #     tim = data[i]['recordTimeStr']       # 该测点测定的时间
        #
        #     f.write(f"{index},{value},{tim}\n")  #
        #     if len(data[i]['data']) == 2:
        #         ind = "{0}-{1}".format(data[i]['data'][1]['registerName'],
        #                              data[i]['nodeId'])  # 命名规则 甲烷-1-1 ：名称-节点号-因子寄存器0/1
        #         value = data[i]['data'][1]['value']
        #         tim = data[i]['recordTimeStr']
        #         f.write(f"{ind},{value},{tim}\n")
        registerNames = []
        regName = []
        value = []
        tim = []
        data_t=[[], []]  # 声明一个二维list
        data_json = {}
        for i in range(len(data)):
            if data[i]['data'][0]['registerName'] not in registerNames:
                registerNames.append(data[i]['data'][0]['registerName'])
            regName.append(data[i]['data'][0]['registerName'])  # 名字列表
            value.append(data[i]['data'][0]['text'])   # 取得测点的测量值
            tim.append(data[i]['recordTimeStr'])        # 该测点测定的时间
            if len(data[i]['data']) == 2:
                if data[i]['data'][1]['registerName'] not in registerNames:
                    registerNames.append(data[i]['data'][1]['registerName'])
                regName.append(data[i]['data'][1]['registerName'])  # 名字列表
                value.append(data[i]['data'][1]['text'])  # 取得测点的测量值
                tim.append(data[i]['recordTimeStr'])  # 该测点测定的时间
        # list convent to numpy
        regName = np.array(regName)
        value = np.array(value)
        tim = np.array(tim)
        for i in registerNames:

            temp = value[regName == i]
            data_t[0] = np.ndarray.tolist(temp)
            temp1 = tim[regName == i]
            data_t[1] = np.ndarray.tolist(temp1)
            data_json[i] = data_t.copy()
        # 存储json数据
        with open(filename, "w") as f:
            json.dump(data_json, f)
        print(name + "数据存储成功！\n")
        return

    def get_history_data(self, deviceAddr, startTime, endTime, nodeId=-1):
        newThread = threading.Thread(target=self.get_history_data_withoutThreads,
                                     args=(deviceAddr, startTime, endTime, nodeId),
                                     name="get_history_data")
        newThread.start()
        return
    def get_token(self):
        url = self.url_yun + "api/getToken?loginName=" + self.ID + "&password=" + self.PW
        r = requests.get(url)
        # print(r.status_code)
        # print(type(r.text))
        # print(r.json())
        info = json.loads(r.content)
        if info['data']['token']:
            print("已经读取到token数据...")
            self.token_expiration_time = info['data']['expiration']
            self.token_time = datetime.datetime.now().timestamp()
            t = info['data']['token']
            self.headers = {'authorization': "{}".format(t), }  # 'Content-Type': 'multipart/form-data',
            print("已经更新网络接口请求头header...")
        else:
            print("读取到token数据错误！请查看源代码")
        # print("token:{}".format(t))
        return

    #  函数功能：采集当前主机1 和主机2的温湿度数据，并存储在air_temperature_buffer和air_humidity_buffer中
    def get_air_temperature_and_humidity_data(self):   # 解析存储空气温度-湿度数据
        # 读主机1 数据
        print("正在下载空气温湿度数据...")
        url = self.url_yun + "api/data/getRealTimeDataByDeviceAddr?deviceAddrs={}".format(self.addr_host1)
        r = requests.get(url, headers=self.headers)
        p = json.loads(r.content)
        print(type(p))
        data = p['data'][0]['dataItem']  # 数据在dataItem list中
        for k in range(32):
            temp = data[k]['registerItem'][0]['data']
            self.air_temperature_buffer["温度1_{}".format(k)] = temp
            temp = data[k]['registerItem'][1]['data']
            self.air_humidity_buffer["湿度1_{}".format(k)] = temp

        # 读主机2 的数据
        url = self.url_yun + "api/data/getRealTimeDataByDeviceAddr?deviceAddrs={}".format(self.addr_host2)
        r = requests.get(url, json, headers=self.headers)
        q = json.loads(r.content)
        for k in range(29):
            temp = q['data'][0]['dataItem'][k]['registerItem'][0]['data']
            self.air_temperature_buffer["温度2_{}".format(k)] = temp
            temp = q['data'][0]['dataItem'][k]['registerItem'][1]['data']
            self.air_humidity_buffer["湿度2_{}".format(k)] = temp

        print("空气温湿度数据已经下载完成... ")

        # print(air_temperature_buffer)
        # print(air_temperature_buffer)

    #
    def get_soil_temperature_and_humidity_data(self):   # 解析存储土壤温度-湿度数据
        # 下载土壤温湿度数据
        print("正在下载土壤温湿度数据...")
        # 北土壤1数据
        url = self.url_yun + "api/data/getRealTimeDataByDeviceAddr?deviceAddr={}".format(self.addr_northern_soil)
        r = requests.get(url, json, headers=self.headers)
        s = json.loads(r.content)
        print(type(s))
        for k in range(5):
            temp = s['data'][0]['dataItem'][k]['registerItem'][0]['data']
            self.soil_temperature_buffer["北土1温度_{}".format(k)] = temp
            temp = s['data'][0]['dataItem'][k]['registerItem'][1]['data']
            self.soil_humidity_buffer["北土1湿度_{}".format(k)] = temp
        # 北土壤2数据
        url = self.url_yun + "api/data/getRealTimeDataByDeviceAddr?deviceAddr={}".format(self.addr_northern_soil2)
        r = requests.get(url, json, headers=self.headers)
        s = json.loads(r.content)
        for k in range(5):
            temp = s['data'][0]['dataItem'][k]['registerItem'][0]['data']
            self.soil_temperature_buffer["北土2温度_{}".format(k)] = temp
            temp = s['data'][0]['dataItem'][k]['registerItem'][1]['data']
            self. soil_humidity_buffer["北土2湿度_{}".format(k)] = temp
        # 南土壤1 数据
        url = self.url_yun + "api/data/getRealTimeDataByDeviceAddr?deviceAddr={}".format(self.addr_southern_soil1)
        r = requests.get(url, json, headers=self.headers)
        s = json.loads(r.content)
        for k in range(5):
            temp = s['data'][0]['dataItem'][k]['registerItem'][0]['data']
            self.soil_temperature_buffer["南土1温度_{}".format(k)] = temp
            temp = s['data'][0]['dataItem'][k]['registerItem'][1]['data']
            self. soil_humidity_buffer["南土1湿度_{}".format(k)] = temp
        # 南土壤2数据
        url = self.url_yun + "api/data/getRealTimeDataByDeviceAddr?deviceAddr={}".format(self.addr_northern_soil2)
        r = requests.get(url, json, headers=self.headers)
        s = json.loads(r.content)
        for k in range(5):
            temp = s['data'][0]['dataItem'][k]['registerItem'][0]['data']
            self.soil_temperature_buffer["南土2温度_{}".format(k)] = temp
            temp = s['data'][0]['dataItem'][k]['registerItem'][1]['data']
            self.soil_humidity_buffer["南土2湿度_{}".format(k)] = temp

    def get_radiation_intensity_data(self):    # 解析室内太阳能辐射数据
        pass

    def intelligent_control_method(self):    # 利用算法计算所有继电器需要的控制状态
        # 添加算法进行数据处理
        pass

        self.relay_command[2] = 1
        self.relay_command[4] = 1
        return 0

    # 使用self.relay_command字典设置继电器开关动作
    def set_relay_state_all(self):   # 控制继电器动作
        # headers.
        for x in range(1, 9):  # x= [1,2 ...8]
            url = self.url_yun + "api/device/setRelay?deviceAddr=" + self.addr_relay +\
                  "&relayNo={}".format(x)+"&opt={}".format(self.relay_command[x])
            # http://www.0531yun.com/api/device/setRelay?deviceAddr=40191625&relayNo=5&opt=0

            print("设定继电器{}".format(x)+"状态为:{}....".format(self.relay_command[x]))
            # data
            r = requests.post(url, headers=self.headers)
            # print(r.json)
            # print(r.request.headers)
            if r.status_code == 200:
                print("操作成功")
            else:
                print("操作失败")

    # 开启某个继电器  addr_relay:继电器地址    relay_num： 继电器编号 取值范围1-8
    def set_one_relay_withoutThreads(self, addr_relay, relay_num):
        url = self.url_yun + "api/device/setRelay?deviceAddr=" + addr_relay + "&relayNo={}".format(
            relay_num) + "&opt={}".format(1)
        # http://www.0531yun.com/api/device/setRelay?deviceAddr=40191625&relayNo=5&opt=0
        if relay_num in self.relay_num:
            r = requests.post(url, headers=self.headers)
            print("正打开继电器{0}-{1}...".format(addr_relay,relay_num))
            if r.status_code == 200:
                print("打开成功。")
                return
            else:
                print("打开失败")
                return
        else:
            print("继电器号超范围")
        return

    def set_one_relay(self, addr_relay, relay_num):
        newThread1 = threading.Thread(target=self.set_one_relay_withoutThreads,
                                      args=(addr_relay, relay_num),
                                      name="newThread_set_one_relay")
        newThread1.start()

    # 关闭某个继电器
    def clear_one_relay_withoutThreads(self, addr_relay, relay_num):
        url = self.url_yun + "api/device/setRelay?deviceAddr=" + addr_relay + "&relayNo={}".format(
            relay_num) + "&opt={}".format(0)
        # http://www.0531yun.com/api/device/setRelay?deviceAddr=40191625&relayNo=5&opt=0
        if relay_num in self.relay_num:
            r = requests.post(url, headers=self.headers)
            print("正关闭继电器{0}-{1}...".format(addr_relay, relay_num))
            if r.status_code == 200:
                print("关闭成功。")
                return
            else:
                print("关闭失败")
                return
        else:
            print("继电器号超出范围")
            return

    def clear_one_relay(self, addr_relay, relay_num):
        newThread2 = threading.Thread(target=self.clear_one_relay_withoutThreads,
                                      args=(addr_relay, relay_num),
                                      name="newThread_clear_one_relay")
        newThread2.start()

    def set_and_clear_one_relay_withoutThreads(self, addr_relay, relay_num):
        self.set_one_relay_withoutThreads(addr_relay, relay_num)
        time.sleep(0.05)
        self.clear_one_relay_withoutThreads(addr_relay, relay_num)

    def set_and_clear_one_relay(self, addr_relay, relay_num):
        newThread = threading.Thread(target=self.set_and_clear_one_relay_withoutThreads,
                                     args=(addr_relay, relay_num),
                                     name="newThread_set_and_clear_one_relay")
        newThread.start()

    def get_cloud_data_12hours_without_Thread(self):
        now = datetime.datetime.now()
        endTime = now.strftime("%Y-%m-%d %H:%M:%S")
        month = int(endTime[5:7])
        day = int(endTime[8:10])
        if day == 1:
            if month in [1, 3, 4, 7, 8, 10, 11]:  # not considered Feb
                day = 31
                month = month-1
            else:
                day = 30
                month = month - 1
        else:
            day = day-1

        startTime = endTime[0:5]+str(month)+'-'+str(day)+endTime[10:]
        # 数据使用主机数据获得 空气温湿度 ；使用气象站获取光照强度；
        # 使用土壤南1 获取土壤温湿度；使用集中器获取CO2浓度数据

        # self.get_history_data_withoutThreads(self.addr_host1, startTime, endTime)  # 主机1
        # self.get_history_data_withoutThreads(self.addr_host2, startTime, endTime)  # 主机2
        self.get_history_data_withoutThreads(self.addr_southern_soil1, startTime, endTime)  # 南土壤1
        self.get_history_data_withoutThreads(self.addr_southern_soil2, startTime, endTime)  # 南土壤2
        self.get_history_data_withoutThreads(self.addr_northern_soil1, startTime, endTime)  # 北土壤1
        self.get_history_data_withoutThreads(self.addr_northern_soil2, startTime, endTime)  # 北土壤2
        self.get_history_data_withoutThreads(self.addr_weather_station, startTime, endTime)  # 气象站
        self.get_history_data_withoutThreads(self.addr_concentrator, startTime, endTime)   # 集中器
        return

    def get_cloud_data_12hours(self):
        newThread = threading.Thread(target=self.get_cloud_data_12hours_without_Thread)
        newThread.start()
        return

    def draw_data(self):
        pass
        return

    def check_token(self):
        consumed_time = datetime.datetime.now().timestamp() - self.token_time  # consumed time/ second.
        # self.get_token()
        if self.token_expiration_time < (consumed_time - 2):
            self.get_token()
        return

    # def refrash_header(self):
    #     headers = {'authorization': "{}".format(Yun.get_token()), }  # 'Content-Type': 'multipart/form-data',
    #     print("已经读取到token数据...")
    #     return

    #  plot the data from "data_dir"  ,data_dir is a str .
    def plot_data(self, data_dir=""):
       with open(self.file_list[0]) as f:  # file_list[0] 主机1




        plt.style.use("seaborn-whitegrid")
        x = [1, 2, 3, 4]
        y = [1, 4, 9, 16]
        # fig = plt.figure()
        plt.plot(x, y)
        plt.ylabel("squares")
        base_dir = "../data/image"
        name = base_dir + "./plot_test"
        plt.savefig(name)
        plt.show()




if __name__ == "__main__":

    # # create data buffer, stores the data download from cloud server last time.
    Yun = YunControl()
    Yun.plot_data()
    # # create communication header
    # Yun.get_token()
    # time.sleep(2)
    # 设置继电器状态
    flag = 0
    while flag:
        # 时间格式 YYYY-MM-dd HH:mm:ss
        Yun.get_cloud_data_12hours()
        # Yun.get_history_data(Yun.addr_concentrator, "2023-01-18 16:19:00 ", "2023-02-16 16:19:00")
        # Yun.get_air_temperature_and_humidity_data()  # ok
        # Yun.get_soil_temperature_and_humidity_data()
        # print("延时3秒钟后，刷新下一帧数据...")
        print()
        flag = ~ flag
        # time.sleep(delay_time)
        # print("空气温度数据：")
        # print(air_temperature_buffer)
        # print("空气湿度数据：")
        # print(air_humidity_buffer)
        # print("土壤温度数据：")
        # print(soil_temperature_buffer)
        # print("土壤湿度数据：")
        # print(soil_humidity_buffer)
        #
        # print("延时3秒钟后，刷新下一帧数据...")
        # time.sleep(Yun.delay_time)
        # intelligent_control_method()  # ok
