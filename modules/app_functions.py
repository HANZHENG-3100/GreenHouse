# -*- coding: gbk -*-
# ///////////////////////////////////////////////////////////////
from datetime import datetime
import os
from ddddocr import DdddOcr
from selenium import webdriver

from PySide6.QtGui import QPixmap, Qt
import OpenCloudWeb
from .app_settings import Settings

from main import MyMainWindow
# WITH ACCESS TO MAIN WINDOW WIDGETS


class AppFunctions:
    # def __init__(self, MyMainWindow):
    #     UI = MyMainWindow.ui

    def setThemeHack(MyMainWindow):
        UI = MyMainWindow.ui
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """

        # SET MANUAL STYLES
        UI.lineEdit.setStyleSheet("background-color: #6272a4;")
        # UI.pushButton.setStyleSheet("background-color: #6272a4;")
       # UI.plainTextEdit.setStyleSheet("background-color: #6272a4;")
        # UI.tableWidget.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        #UI.scrollArea.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
       # UI.comboBox.setStyleSheet("background-color: #6272a4;")
        # UI.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
       # UI.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
      # UI.commandLinkButton.setStyleSheet("color: #ff79c6;")

    @staticmethod
    def Btn_open_web():
        # global driver
        # driver = webdriver.Edge()  # "./chromedriver_win32/chromedriver.exe" = webdriver.Edge()  # "./chromedriver_win32/chromedriver.exe"
        op = OpenCloudWeb.OpenWeb()
        op.open_cloud_web()
        print("Btn_open_web run")
        return

    @staticmethod
    def display(self):
        UI = self.ui
        # YUN = window.yun
        currPath = os.getcwd()  # 获取当前工作路径
        image_label_list = [UI.image_1, UI.image_2, UI.image_3,
                            UI.image_4, UI.image_5, UI.image_6,
                            UI.image_7, UI.image_8, UI.image_9,
                            UI.image_10]
        for i in range(1, 11):
            path = r'{}\data\image\image{}.png'.format(currPath, i)
            image = image_label_list[i - 1]
            pix = QPixmap(path)
            pix.scaled(image.size(), aspectMode=Qt.KeepAspectRatio)
            image.setPixmap(pix)
            image.setScaledContents(True)
        return

    @staticmethod
    def Refresh_radioBtn(MyMainWindow, pageNum):
        UI = MyMainWindow.ui
        yun = MyMainWindow.yun
        # 读取继电器工作状态
        yun.read_all_delay_status(pageNum)
        # if yun.relay1_status[]
        if pageNum ==1:
            # manual_control_page1 按键设置 3行 4列
            if 0 == yun.relay1_status[1]:  # 卷帘机
                UI.Rbtn1_11_up.setChecked(True)
            if 0 == yun.relay1_status[2]:
                UI.Rbtn1_11_stop.setChecked(True)
            if 0 == yun.relay1_status[3]:
                UI.Rbtn1_11_down.setChecked(True)
            # 卷膜机
            if 0 == yun.relay1_status[4]:
                UI.Rbtn1_12_up.setChecked(True)
            if 0 == yun.relay1_status[5]:
                UI.Rbtn1_12_stop.setChecked(True)
            if 0 == yun.relay1_status[6]:
                UI.Rbtn1_12_down.setChecked(True)

            if 0 == yun.relay1_status[7]:
                UI.Rbtn1_13_open.setChecked(True)   # 补光灯1
            if 1 == yun.relay1_status[7]:
                UI.Rbtn1_13_close.setChecked(True)

            if 0 == yun.relay1_status[8]:
                UI.Rbtn1_14_open.setChecked(True)  # 补光灯2
            if 1 == yun.relay1_status[8]:
                UI.Rbtn1_14_close.setChecked(True)

            if 0 == yun.relay2_status[1]:
                UI.Rbtn1_21_open.setChecked(True)  # 照明灯
            if 1 == yun.relay2_status[1]:
                UI.Rbtn1_21_close.setChecked(True)

            if 0 == yun.relay2_status[2]:
                UI.Rbtn1_22_open.setChecked(True)  # 门厅灯
            if 1 == yun.relay2_status[2]:
                UI.Rbtn1_22_close.setChecked(True)

            if 0 == yun.relay2_status[3]:
                UI.Rbtn1_23_open.setChecked(True)  # 循环乙二醇泵
            if 1 == yun.relay2_status[3]:
                UI.Rbtn1_23_close.setChecked(True)

            if 0 == yun.relay1_status[4]:
                UI.Rbtn1_24_open.setChecked(True)  # 循环乙二醇泵（备用）
            if 1 == yun.relay1_status[4]:
                UI.Rbtn1_24_close.setChecked(True)

            if 0 == yun.relay2_status[5]:
                UI.Rbtn1_31_open.setChecked(True)  # 循环水与乙二醇换热泵
            if 1 == yun.relay2_status[5]:
                UI.Rbtn1_31_close.setChecked(True)

            if 0 == yun.relay2_status[6]:
                UI.Rbtn1_32_open.setChecked(True)  # 循环水与乙二醇换热泵（备用）
            if 1 == yun.relay2_status[6]:
                UI.Rbtn1_32_close.setChecked(True)

            if 0 == yun.relay2_status[7]:
                UI.Rbtn1_33_open.setChecked(True)  # 循环水与空气换热泵
            if 1 == yun.relay2_status[7]:
                UI.Rbtn1_33_close.setChecked(True)

            if 0 == yun.relay2_status[8]:
                UI.Rbtn1_34_open.setChecked(True)
            if 1 == yun.relay2_status[8]:
                UI.Rbtn1_34_close.setChecked(True)  # 循环水与空气换热泵（备用）

        if pageNum == 2:
            # manual_control_page2   按键设置 3行 4列
            if 0 == yun.relay3_status[1]:
                UI.Rbtn2_11_open.setChecked(True)  # 加热棒1
            if 1 == yun.relay3_status[1]:
                UI.Rbtn2_11_close.setChecked(True)

            if 0 == yun.relay3_status[2]:
                UI.Rbtn2_12_open.setChecked(True)  # 加热棒2
            if 1 == yun.relay3_status[2]:
                UI.Rbtn2_12_close.setChecked(True)

            if 0 == yun.relay3_status[3]:
                UI.Rbtn2_13_open.setChecked(True)  # 加热棒3
            if 1 == yun.relay3_status[3]:
                UI.Rbtn2_13_close.setChecked(True)

            if 0 == yun.relay3_status[4]:
                UI.Rbtn2_14_open.setChecked(True)  # 控制回路电源
            if 1 == yun.relay3_status[4]:
                UI.Rbtn2_14_close.setChecked(True)

            if 0 == yun.relay3_status[5]:
                UI.Rbtn2_21_open.setChecked(True)  # 排风机1
            if 1 == yun.relay3_status[5]:
                UI.Rbtn2_21_close.setChecked(True)

            if 0 == yun.relay3_status[6]:
                UI.Rbtn2_22_open.setChecked(True)  # 排风机2
            if 1 == yun.relay3_status[6]:
                UI.Rbtn2_22_close.setChecked(True)

            if 0 == yun.relay3_status[7]:
                UI.Rbtn2_23_open.setChecked(True)  # 排风机3
            if 1 == yun.relay3_status[7]:
                UI.Rbtn2_23_close.setChecked(True)

            if 0 == yun.relay3_status[8]:
                UI.Rbtn2_24_open.setChecked(True)  # 排风机4
            if 1 == yun.relay3_status[8]:
                UI.Rbtn2_24_close.setChecked(True)

            if 0 == yun.relay4_status[1]:
                UI.Rbtn2_31_open.setChecked(True)  # 水肥一体机泵
            if 1 == yun.relay4_status[1]:
                UI.Rbtn2_31_close.setChecked(True)

            if 0 == yun.relay4_status[2]:
                UI.Rbtn2_32_open.setChecked(True)  # 水肥一体机电磁阀门
            if 1 == yun.relay4_status[2]:
                UI.Rbtn2_32_close.setChecked(True)

            if 0 == yun.relay4_status[3]:
                UI.Rbtn2_33_open.setChecked(True)  # 室内监测电源
            if 1 == yun.relay4_status[3]:
                UI.Rbtn2_33_close.setChecked(True)

            if 0 == yun.relay4_status[4]:
                UI.Rbtn2_34_open.setChecked(True)  # 气象站电源
            if 1 == yun.relay4_status[4]:
                UI.Rbtn2_34_close.setChecked(True)


        return

    @staticmethod
    def btn_get_data_12hours(MyMainWindow):
        UI = MyMainWindow.ui
        YUN = MyMainWindow.yun
        print("btn_get_data_12hours knob down")
        # now = datetime.now().timestamp()
        ''' 以下代码下载数据使用'''
        # self.yun.check_token()
        YUN.get_cloud_data_12hours()
        UI.label_time.setText(u"获取时间：" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        return


if __name__ == "__main__":
    import os
    import sys

    os.chdir('../')
    currPath = os.getcwd()
    print(currPath)
    # print("sys.path[0] = ", sys.path[0])
    # print("sys.argv[0] = ", sys.argv[0])






