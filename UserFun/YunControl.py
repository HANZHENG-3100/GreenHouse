import os
import requests
import json
import urllib3
import datetime
# import sys, tty, select, termios


class YunControl():

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
                           '北部土壤传感器2': "21043747",
                           '南部土壤传感器1': "21043765",
                           '南部土壤传感器2': "21043765",
                           '主机1': "40184157",
                           '主机2': "40184180",
                           '网络继电器': "40191625"
                           }
        self.addr_weather_station = "40133062"       # 气象站设备地址
        self.addr_concentrator = "20009680"          # 集中器地址            数据6个 甲烷、氮气、水箱123、CO2浓度
        self.Addr_Comparison_soil = "21043744"       # 对照土壤传感器       （5个温度值，5个湿度值）
        self.addr_northern_soil = "21043747"        # 北部土壤传感器1      （5个温度值，5个湿度值）
        self.addr_northern_soil2 = "21043747"        # 北部土壤传感器2      （5个温度值，5个湿度值）
        self.addr_southern_soil1 = "21043765"        # 南部土壤传感器1      （5个温度值，5个湿度值）
        self.addr_southern_soil2 = "21043765"        # 南部土壤传感器2      （5个温度值，5个湿度值）
        self.addr_host1 = "40184157"                 # 主机1地址            （32组温湿度）
        self.addr_host2 = "40184180"                 # 主机2地址            （29组温湿度） 不确定
        self.addr_relay = "40191625"                 # 网络继电器地址
        self.delay_time = 2                          # 程序运行时间间隔，由传感器采集频率决定

        self.relay_command = {1: 1, 2: 1, 3: 1, 4: 0, 5: 0, 6: 0, 7: 1, 8: 1}  # 继电器控制初始状态  0灯亮 闭合  1灯灭 断开
        self.relay_num = {'1', '2', '3', '4', '5', '6', '7', '8'}
        self.air_temperature_buffer = {}  # 存储临时环境数据
        self.air_humidity_buffer = {}
        self.soil_temperature_buffer = {}  #
        self.soil_humidity_buffer = {}

        self.headers = ""
        self.token_expiration_time = 0.0
        self.token_time = 0.0
    #  获取传感器历史数据 deviceAddr=主机地址, nodeId=传感器因子号, startTime, endTime时间格式：YYYY-MM-dd HH:mm:ss
    #  使用接口获取历史数据时，每分钟只能执行6次，超出次数会被拒绝。

    def get_history_data(self, deviceAddr, startTime, endTime, nodeId=-1,):
        iid = list(self.deviceAddr.values()).index(deviceAddr)
        name = list(self.deviceAddr.keys())[iid]
        url = self.url_yun + "api/data/historyList"
        params = {"deviceAddr": int(deviceAddr), "nodeId": nodeId, "startTime": startTime, "endTime": endTime}
        r = requests.get(url=url, headers=self.headers, params=params)
        p = json.loads(r.content)  # 将json字符串转换为python dict对象
        if p['code'] == 1000:
            print(name + "请求数据成功！")
            if p['data']:
                data = p['data']
                print(name+"历史数据下载成功！\n")
            else:
                print(name + "无历史数据,请检查近期传感器连接情况。\n")
                return
        else:
            print(name+"请求数据失败，请查看网络通信。\n")
            return
        deviceAddr = str(data[0]['deviceAddr'])  # 取地址

        filename = "{0}_{1}_{2}-{3}".format(name, deviceAddr, startTime, endTime)
        filename = filename.replace(" ", "_")
        filename = filename.replace(":", "-")
        filename = "../data/{0}.csv".format(filename)

        f = open(filename, 'w')
        for i in range(len(data)):
            index = "{0}-{1}".format(data[i]['data'][0]['registerName'],
                                     data[i]['nodeId'])  # 命名规则 甲烷-1-1 ：名称-节点号-因子寄存器0/1
            value = data[i]['data'][0]['value']
            tim = data[i]['recordTimeStr']
            f.write(f"{index},{value},{tim}\n")
            if len(data[i]['data']) == 2:
                ind = "{}-{}".format(data[i]['data'][1]['registerName'],
                                     data[i]['nodeId'])  # 命名规则 甲烷-1-1 ：名称-节点号-因子寄存器0/1
                value = data[i]['data'][1]['value']
                tim = data[i]['recordTimeStr']
                f.write(f"{ind},{value},{tim}\n")
        f.close()

        return

    def get_token(self):
        url = self.url_yun + "api/getToken?loginName=" + self.ID + "&password=" + self.PW
        r = requests.get(url)
        # print(r.status_code)
        # print(type(r.text))
        # print(r.json())
        info = r.json()
        if info['data']['token']:
            print("已经读取到token数据...")
            self.token_expiration_time = info['data']['expiration']
            self.token_time = datetime.datetime.now().timestamp()
            t = info['data']['token']
            self.header = {'authorization': "{}".format(t), }  # 'Content-Type': 'multipart/form-data',
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

    # 开启某个继电器
    def set_one_relay(self, relay_num):
        url = self.url_yun + "api/device/setRelay?deviceAddr=" + self.addr_relay + "&relayNo={}".format(
            relay_num) + "&opt={}".format(1)
        # http://www.0531yun.com/api/device/setRelay?deviceAddr=40191625&relayNo=5&opt=0
        if relay_num in self.relay_num:
            r = requests.post(url, headers=self.headers)
            print("正打开继电器{}...".format(relay_num))
            if r.status_code == 200:
                print("打开成功。")
                return
            else:
                print("打开失败")
                return
        else:
            print("继电器号超范围")
        return

    # 关闭某个继电器
    def clear_one_relay(self, relay_num):
        url = self.url_yun + "api/device/setRelay?deviceAddr=" + self.addr_relay + "&relayNo={}".format(
            relay_num) + "&opt={}".format(0)
        # http://www.0531yun.com/api/device/setRelay?deviceAddr=40191625&relayNo=5&opt=0
        if relay_num in self.relay_num:
            r = requests.post(url, headers=self.headers)
            print("正打开继电器{}...".format(relay_num))
            if r.status_code == 200:
                print("关闭成功。")
                return
            else:
                print("关闭失败")
                return
        else:
            print("继电器号超出范围")
            return

    def get_cloud_data_12hours(self):
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
        self.get_history_data(self.addr_host1, startTime, endTime)
        self.get_history_data(self.addr_southern_soil1, startTime, endTime)
        self.get_history_data(self.addr_weather_station, startTime, endTime)
        self.get_history_data(self.addr_concentrator, startTime, endTime)
        return

    def draw_data(self):

        pass
        return

    def check_token(self):
        consumed_time = datetime.datetime.now().timestamp() - self.token_time  # consumed time/ second.
        if self.token_expiration_time < (consumed_time - 2):
            self.get_token()
        return

    # def refrash_header(self):
    #     headers = {'authorization': "{}".format(Yun.get_token()), }  # 'Content-Type': 'multipart/form-data',
    #     print("已经读取到token数据...")
    #     return


if __name__ == "__main__":
    # create data buffer, stores the data download from cloud server last time.
    Yun = YunControl()
    # create communication header
    Yun.get_token()
    # time.sleep(2)
    # 设置继电器状态
    flag = 1
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
