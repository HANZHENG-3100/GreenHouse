# ///////////////////////////////////////////////////////////////
#
# BY: HANZHENG
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# /////////////////////////////////////////////////////////////// # _*_ coding:TUF-8 _*_
# -*- coding: gbk -*-
import sys
import PySide6
import os
# IMPORT / GUI AND MODULES AND WIDGETS
from UserFun.YunControl import YunControl
from modules import *
from widgets import *
from PySide6.QtCharts import QChart, QLineSeries, QValueAxis
# SET AS GLOBAL WIDGETS
widgets = None
yun = None


class MyMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.yun = YunControl()
        self.ui.setupUi(self)
        global widgets, yun
        widgets = self.ui
        yun = self.yun

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        # APP NAME
        title = "智能物联网温室环境自动控制系统"
        description = "智能物联网温室环境自动控制系统"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)
        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))  # 实现隐藏功能按钮
        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # UIFunctions.toggleMenu(self, enable=False)
        # self.show()
        # QTableWidget PARAMETERS
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        '''
        # btn_cloud -> cloud_page；
        # btn_manual_control->manual_control_page
        # btn_auto_control-> auto_control_page；
        # btn_energy-> energy_page；
        # btn_information->information_page；
        '''

        # LEFT MENUS
        widgets.btn_cloud1.clicked.connect(self.buttonClick)
        widgets.btn_cloud2.clicked.connect(self.buttonClick)
        widgets.btn_manual_control1.clicked.connect(self.buttonClick)
        widgets.btn_manual_control2.clicked.connect(self.buttonClick)
        widgets.btn_auto_control.clicked.connect(self.buttonClick)
        widgets.btn_energy.clicked.connect(self.buttonClick)
        widgets.btn_information.clicked.connect(self.buttonClick)
        # widgets.btn_open_web.clicked.connect(self.buttonClick)
        #  CHANGE THEMES
        widgets.btn_change_topic.clicked.connect(self.buttonClick)
        # OPEN CLOUD WEB
        widgets.Btn_open_cloud_web.clicked.connect(self.buttonClick)
        # GET 12HOURS DATA
        widgets.btn_get_data_12hours.clicked.connect(self.buttonClick)
        AppFunctions.display(self)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        # widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        # widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        # 路径冻结，防止打包成exe后路径错乱
        if getattr(sys, 'frozen', False):
            absPath = os.path.dirname(os.path.abspath(sys.executable))
        elif __file__:
            absPath = os.path.dirname(os.path.abspath(__file__))
        useCustomTheme = False
        self.useCustomTheme = useCustomTheme
        self.absPath = absPath
        themeFile = os.path.abspath(os.path.join(absPath, "themes\py_dracula_light.qss"))
        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.cloud_page1)  # 设置首页显示
        # widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()  # 获取发送信号的对象
        btnName = btn.objectName()
        '''
        # btn_auto_control-> auto_control_page；
        # btn_cloud -> cloud_page；
        # btn_energy-> energy_page；
        # btn_information->information_page；
        # btn_manual_control->manual_control_page
        '''
        # SHOW cloud_page
        if btnName == "btn_cloud1":
            widgets.stackedWidget.setCurrentWidget(widgets.cloud_page1)  # 堆栈窗口设置为cloud_page窗口
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(self, btn.styleSheet()))
        if btnName == "btn_cloud2":
            widgets.stackedWidget.setCurrentWidget(widgets.cloud_page2)  # 堆栈窗口设置为cloud_page窗口
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(self, btn.styleSheet()))
        # SHOW energy_page
        if btnName == "btn_energy":
            widgets.stackedWidget.setCurrentWidget(widgets.energy_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(self, btn.styleSheet()))
            QMessageBox.information(self, "Sorry", "该功能还在开发之中", QMessageBox.Yes)

        # SHOW auto_control_page
        if btnName == "btn_auto_control":
            widgets.stackedWidget.setCurrentWidget(widgets.auto_control_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(self, btn.styleSheet()))  # SELECT MENU

        # SHOW auto_control_page
        if btnName == "btn_manual_control1":
            # print("Save BTN clicked!")
            widgets.stackedWidget.setCurrentWidget(widgets.manual_control_page1)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(self, btn.styleSheet()))  # SELECT MENU
            # QMessageBox.information(self, "提示", "该功能暂未实现", QMessageBox.Yes)
        if btnName == "btn_manual_control2":
            # print("Save BTN clicked!")
            widgets.stackedWidget.setCurrentWidget(widgets.manual_control_page2)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(self, btn.styleSheet()))  # SELECT MENU
            # QMessageBox.information(self, "提示", "该功能暂未实现", QMessageBox.Yes)

        if btnName == "btn_information":
            widgets.stackedWidget.setCurrentWidget(widgets.information_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(self, btn.styleSheet()))  # SELECT MENU

        # change topic button
        if btnName == "btn_change_topic":
            if self.useCustomTheme:
                themeFile = os.path.abspath(os.path.join(self.absPath, "themes\py_dracula_dark.qss"))
                UIFunctions.theme(self, themeFile, True)
                # SET HACKS
                AppFunctions.setThemeHack(self)
                self.useCustomTheme = False
            else:
                themeFile = os.path.abspath(os.path.join(self.absPath, "themes\py_dracula_light.qss"))
                UIFunctions.theme(self, themeFile, True)
                # SET HACKS
                AppFunctions.setThemeHack(self)
                self.useCustomTheme = True

        #  Button in cloud_page
        if btnName == "Btn_open_cloud_web":
            AppFunctions.Btn_open_web(self)
        print(f'Button "{btnName}" pressed!')
        if btnName == "btn_get_data_12hours":
            AppFunctions.btn_get_data_12hours(self)
            print()
    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        # self.dragPos = event.globalPos()
        self.dragPos = event.globalPosition().toPoint()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    # def start_computer_info(self):
    #     """
    #     开始获取电脑数据
    #     :return:
    #     """
    #     # 开始分析记录电脑数据，需持续获取，然后分析
    #     self.thread1 = NewThread()  # 实例化一个线程
    #     # 将线程thread的信号finishSignal和UI主线程中的槽函数data_display进行连接
    #     self.thread1.finishSignal.connect(self.data_display)
    #     # 启动线程，执行线程类中run函数
    #     self.thread1.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("bakeup/icon.ico"))
    window = MyMainWindow()
    sys.exit(app.exec())
