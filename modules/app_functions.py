# -*- coding: gbk -*-

# MAIN FILE
# ///////////////////////////////////////////////////////////////
import urllib3

from main import *
from main import MainWindow
from .app_settings import Settings
from UserFun.YunControl import YunControl

import datetime

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from time import strftime
# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////


class AppFunctions(MainWindow):
    def __init__(self):
        self.yun = YunControl()

    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """

        # SET MANUAL STYLES
        self.ui.lineEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.pushButton.setStyleSheet("background-color: #6272a4;")
       # self.ui.plainTextEdit.setStyleSheet("background-color: #6272a4;")
        # self.ui.tableWidget.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        #self.ui.scrollArea.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
       # self.ui.comboBox.setStyleSheet("background-color: #6272a4;")
        # self.ui.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
       # self.ui.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
      # self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")

    def Btn_open_web(self):
        import webbrowser
        webbrowser.open('http://www.0531yun.com/')
        print("Btn_open_web run")
        return

    def btn_get_data_12hours(self):
        print("btn_get_data_12hours knob down")
        # now = datetime.datetime.now().timestamp()
        self.yun.check_token()
        self.yun.get_cloud_data_12hours()
        self.ui.label_time.setText(u"获取时间：" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


        return

    def compute_initial_figure(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.grid('on')
        self.axes.plot(t, s)








