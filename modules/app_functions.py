# -*- coding: gbk -*-

# MAIN FILE
# ///////////////////////////////////////////////////////////////
import urllib3

from main import *
from .app_settings import Settings
from UserFun.YunControl import YunControl

import datetime
from time import strftime
# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////


class AppFunctions(MainWindow):
    yun = YunControl()

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
        consumed_time = datetime.datetime.now().timestamp() - AppFunctions.yun.token_time # consumed time/ second.
        if AppFunctions.yun.token_expiration_time < (consumed_time - 2):
            AppFunctions.yun.get_token()
        AppFunctions.yun.get_cloud_data_12hours()

        self.ui.label_time.setText(u"获取时间：" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        return





