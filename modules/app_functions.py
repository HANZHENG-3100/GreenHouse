# -*- coding: gbk -*-
# ///////////////////////////////////////////////////////////////
from datetime import datetime
import os
from PySide6.QtGui import QPixmap, Qt
# from main import MyMainWindow
from .app_settings import Settings

# WITH ACCESS TO MAIN WINDOW WIDGETS


class AppFunctions:
    # def __init__(self, MyMainWindow):
    #     UI = MyMainWindow.ui
    @staticmethod
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
        import webbrowser
        webbrowser.open('http://www.0531yun.com/')
        print("Btn_open_web run")
        return

    @staticmethod
    def display(MyMainWindow):
        UI = MyMainWindow.ui
        currPath = os.getcwd()
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






