# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1343, 800)
        MainWindow.setMinimumSize(QSize(1200, 800))
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet(u"")
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"# BY: WANDERSON M.PIMENTA\n"
"# PROJECT MADE WITH: Qt Designer and PySide6\n"
"# V: 1.0.0\n"
"#\n"
"# This project can be used freely for all uses, as long as they maintain the\n"
"# respective credits only in the Python scripts, any information in the visual\n"
"# interface (GUI) can be modified without any implication.\n"
"#\n"
"# There are limitations on Qt licenses if you want to use your products\n"
"# commercially, I recommend reading them on the official website:\n"
"# https://doc.qt.io/qtforpython/licenses.html\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	 color: rgb(221, 221, 221);\n"
"    /* color: rgb(80, 80, 80);*/\n"
"\n"
"	font: 14pt \"Segoe UI\";\n"
"}\n"
"Line{\n"
"color: rgb(189, 147, 249);\n"
"}\n"
"/* /////////////"
                        "////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-positi"
                        "on: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 15pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 12pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMe"
                        "nu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-po"
                        "sition: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
""
                        "}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel "
                        "{ font-size: 14px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	pa"
                        "dding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader{\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit \n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
""
                        "	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"} \n"
"*/\n"
"\n"
"/*LineEdit  \u4eae\u8272*/\n"
"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-back"
                        "ground-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
""
                        "}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
" "
                        "    subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
""
                        "	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	"
                        "subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
""
                        "    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QComm"
                        "andLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QRadioButton */\n"
"QRadioButton::indicator {\n"
"    width:     "
                        "           30px;\n"
"    height:               30px;\n"
"    border-radius:        17px;\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
"    background-color:       green;\n"
"    border:                3px solid white;\n"
"}\n"
" \n"
"/*QRadioButton::indicator:unchecked {\n"
"    background-color:       red;\n"
"    border:                 2px solid white;\n"
"}*/\n"
"QTextBrowser{\n"
"border-width:0;\n"
"border-style:outset;}")
        self.gridLayout_2 = QGridLayout(self.styleSheet)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"image: url(:/images/images/images/PyDracula .png);")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(65, 0))
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_cloud = QPushButton(self.topMenu)
        self.btn_cloud.setObjectName(u"btn_cloud")
        self.btn_cloud.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btn_cloud.sizePolicy().hasHeightForWidth())
        self.btn_cloud.setSizePolicy(sizePolicy)
        self.btn_cloud.setMinimumSize(QSize(0, 45))
        self.btn_cloud.setFont(font)
        self.btn_cloud.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cloud.setLayoutDirection(Qt.LeftToRight)
        self.btn_cloud.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-cloudy.png);")

        self.verticalLayout_8.addWidget(self.btn_cloud)

        self.btn_manual_control = QPushButton(self.topMenu)
        self.btn_manual_control.setObjectName(u"btn_manual_control")
        sizePolicy.setHeightForWidth(self.btn_manual_control.sizePolicy().hasHeightForWidth())
        self.btn_manual_control.setSizePolicy(sizePolicy)
        self.btn_manual_control.setMinimumSize(QSize(0, 45))
        self.btn_manual_control.setFont(font)
        self.btn_manual_control.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_manual_control.setLayoutDirection(Qt.LeftToRight)
        self.btn_manual_control.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-hand-point-up.png);")

        self.verticalLayout_8.addWidget(self.btn_manual_control)

        self.btn_auto_control = QPushButton(self.topMenu)
        self.btn_auto_control.setObjectName(u"btn_auto_control")
        self.btn_auto_control.setMinimumSize(QSize(0, 45))
        self.btn_auto_control.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-change.png);")

        self.verticalLayout_8.addWidget(self.btn_auto_control)

        self.btn_energy = QPushButton(self.topMenu)
        self.btn_energy.setObjectName(u"btn_energy")
        sizePolicy.setHeightForWidth(self.btn_energy.sizePolicy().hasHeightForWidth())
        self.btn_energy.setSizePolicy(sizePolicy)
        self.btn_energy.setMinimumSize(QSize(0, 45))
        self.btn_energy.setFont(font)
        self.btn_energy.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_energy.setLayoutDirection(Qt.LeftToRight)
        self.btn_energy.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-speedometer.png);")

        self.verticalLayout_8.addWidget(self.btn_energy)

        self.btn_information = QPushButton(self.topMenu)
        self.btn_information.setObjectName(u"btn_information")
        self.btn_information.setMinimumSize(QSize(0, 45))
        self.btn_information.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-closed.png);")

        self.verticalLayout_8.addWidget(self.btn_information)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 60))
        self.contentTopBg.setMaximumSize(QSize(16777215, 60))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font3 = QFont()
        font3.setFamilies([u"\u6977\u4f53"])
        font3.setPointSize(22)
        font3.setBold(False)
        font3.setItalic(False)
        self.titleRightInfo.setFont(font3)
        self.titleRightInfo.setStyleSheet(u"font: 22pt \"\u6977\u4f53\";")
        self.titleRightInfo.setTextFormat(Qt.AutoText)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.energy_page = QWidget()
        self.energy_page.setObjectName(u"energy_page")
        self.energy_page.setStyleSheet(u"")
        self.energy_page_row_1 = QFrame(self.energy_page)
        self.energy_page_row_1.setObjectName(u"energy_page_row_1")
        self.energy_page_row_1.setGeometry(QRect(20, 0, 781, 121))
        self.energy_page_row_1.setMinimumSize(QSize(150, 100))
        self.energy_page_row_1.setFrameShape(QFrame.StyledPanel)
        self.energy_page_row_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.energy_page_row_1)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label = QLabel(self.energy_page_row_1)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.label)

        self.energy_page_row_2 = QFrame(self.energy_page)
        self.energy_page_row_2.setObjectName(u"energy_page_row_2")
        self.energy_page_row_2.setGeometry(QRect(10, 140, 801, 121))
        self.energy_page_row_2.setMinimumSize(QSize(150, 100))
        self.energy_page_row_2.setFrameShape(QFrame.StyledPanel)
        self.energy_page_row_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.energy_page_row_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_2 = QLabel(self.energy_page_row_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_15.addWidget(self.label_2)

        self.energy_page_row_3 = QFrame(self.energy_page)
        self.energy_page_row_3.setObjectName(u"energy_page_row_3")
        self.energy_page_row_3.setGeometry(QRect(10, 260, 661, 121))
        self.energy_page_row_3.setFrameShape(QFrame.StyledPanel)
        self.energy_page_row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.energy_page_row_3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_14 = QLabel(self.energy_page_row_3)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_16.addWidget(self.label_14)

        self.stackedWidget.addWidget(self.energy_page)
        self.auto_control_page = QWidget()
        self.auto_control_page.setObjectName(u"auto_control_page")
        self.auto_control_page.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.auto_control_page)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.auto_control_page_row_1 = QFrame(self.auto_control_page)
        self.auto_control_page_row_1.setObjectName(u"auto_control_page_row_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(4)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.auto_control_page_row_1.sizePolicy().hasHeightForWidth())
        self.auto_control_page_row_1.setSizePolicy(sizePolicy3)
        self.auto_control_page_row_1.setFrameShape(QFrame.StyledPanel)
        self.auto_control_page_row_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.auto_control_page_row_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.spinBox = QSpinBox(self.auto_control_page_row_1)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout_3.addWidget(self.spinBox, 2, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.auto_control_page_row_1)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_3.addWidget(self.lineEdit_7, 2, 2, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_22, 3, 3, 1, 1)

        self.lineEdit_10 = QLineEdit(self.auto_control_page_row_1)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_3.addWidget(self.lineEdit_10, 3, 0, 1, 1)

        self.lineEdit_13 = QLineEdit(self.auto_control_page_row_1)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout_3.addWidget(self.lineEdit_13, 3, 6, 1, 1)

        self.lineEdit_8 = QLineEdit(self.auto_control_page_row_1)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setMouseTracking(True)
        self.lineEdit_8.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit_8.setInputMethodHints(Qt.ImhUppercaseOnly)
        self.lineEdit_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lineEdit_8, 2, 4, 1, 1)

        self.lineEdit_11 = QLineEdit(self.auto_control_page_row_1)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_3.addWidget(self.lineEdit_11, 3, 2, 1, 1)

        self.spinBox_3 = QSpinBox(self.auto_control_page_row_1)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.gridLayout_3.addWidget(self.spinBox_3, 3, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.auto_control_page_row_1)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 6, 1, 1)

        self.spinBox_2 = QSpinBox(self.auto_control_page_row_1)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.gridLayout_3.addWidget(self.spinBox_2, 2, 5, 1, 1)

        self.lineEdit_9 = QLineEdit(self.auto_control_page_row_1)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_3.addWidget(self.lineEdit_9, 2, 6, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_21, 2, 3, 1, 1)

        self.lineEdit_5 = QLineEdit(self.auto_control_page_row_1)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_3.addWidget(self.lineEdit_5, 1, 0, 1, 2)

        self.lineEdit_12 = QLineEdit(self.auto_control_page_row_1)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lineEdit_12, 3, 4, 1, 1)

        self.lineEdit_6 = QLineEdit(self.auto_control_page_row_1)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_3.addWidget(self.lineEdit_6, 2, 0, 1, 1)

        self.spinBox_4 = QSpinBox(self.auto_control_page_row_1)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.gridLayout_3.addWidget(self.spinBox_4, 3, 5, 1, 1)


        self.verticalLayout.addWidget(self.auto_control_page_row_1)

        self.lineEdit_14 = QLineEdit(self.auto_control_page)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.verticalLayout.addWidget(self.lineEdit_14)

        self.line = QFrame(self.auto_control_page)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.auto_control_page_row_2 = QFrame(self.auto_control_page)
        self.auto_control_page_row_2.setObjectName(u"auto_control_page_row_2")
        self.auto_control_page_row_2.setMinimumSize(QSize(0, 150))
        self.auto_control_page_row_2.setFrameShape(QFrame.StyledPanel)
        self.auto_control_page_row_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.auto_control_page_row_2)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_content_wid_1 = QFrame(self.auto_control_page_row_2)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.horizontalLayout_12.addWidget(self.frame_content_wid_1)


        self.verticalLayout.addWidget(self.auto_control_page_row_2)

        self.lineEdit_15 = QLineEdit(self.auto_control_page)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.verticalLayout.addWidget(self.lineEdit_15)

        self.stackedWidget.addWidget(self.auto_control_page)
        self.manual_control_page = QWidget()
        self.manual_control_page.setObjectName(u"manual_control_page")
        self.frame_k = QFrame(self.manual_control_page)
        self.frame_k.setObjectName(u"frame_k")
        self.frame_k.setGeometry(QRect(30, 10, 1041, 600))
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_k.sizePolicy().hasHeightForWidth())
        self.frame_k.setSizePolicy(sizePolicy4)
        self.frame_k.setMinimumSize(QSize(0, 600))
        self.frame_k.setMaximumSize(QSize(16777215, 400))
        self.frame_k.setFrameShape(QFrame.StyledPanel)
        self.frame_k.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_k)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_1 = QFrame(self.frame_k)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setFrameShape(QFrame.Box)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.frame_1.setLineWidth(0)
        self.frame_1.setMidLineWidth(2)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_1)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_4 = QLabel(self.frame_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_4)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.RB_open_zhaoming = QRadioButton(self.frame_1)
        self.RB_open_zhaoming.setObjectName(u"RB_open_zhaoming")
        self.RB_open_zhaoming.setStyleSheet(u"")

        self.verticalLayout_27.addWidget(self.RB_open_zhaoming)

        self.RB_close_zhaoming = QRadioButton(self.frame_1)
        self.RB_close_zhaoming.setObjectName(u"RB_close_zhaoming")
        self.RB_close_zhaoming.setStyleSheet(u"")

        self.verticalLayout_27.addWidget(self.RB_close_zhaoming)


        self.horizontalLayout_17.addLayout(self.verticalLayout_27)


        self.gridLayout_4.addWidget(self.frame_1, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame_k)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(0)
        self.frame_3.setMidLineWidth(2)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_7)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.RB_open_jiare = QRadioButton(self.frame_3)
        self.RB_open_jiare.setObjectName(u"RB_open_jiare")
        self.RB_open_jiare.setStyleSheet(u"")

        self.verticalLayout_30.addWidget(self.RB_open_jiare)

        self.RB_close_jiare = QRadioButton(self.frame_3)
        self.RB_close_jiare.setObjectName(u"RB_close_jiare")
        self.RB_close_jiare.setStyleSheet(u"")

        self.verticalLayout_30.addWidget(self.RB_close_jiare)


        self.horizontalLayout_20.addLayout(self.verticalLayout_30)


        self.gridLayout_4.addWidget(self.frame_3, 0, 2, 1, 1)

        self.frame_4 = QFrame(self.frame_k)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.frame_4.setMidLineWidth(2)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_5)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.RB_open_juanlian = QRadioButton(self.frame_4)
        self.RB_open_juanlian.setObjectName(u"RB_open_juanlian")
        self.RB_open_juanlian.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.RB_open_juanlian)

        self.RB_close_juanlian = QRadioButton(self.frame_4)
        self.RB_close_juanlian.setObjectName(u"RB_close_juanlian")
        self.RB_close_juanlian.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.RB_close_juanlian)

        self.RB_close_juanlian_2 = QRadioButton(self.frame_4)
        self.RB_close_juanlian_2.setObjectName(u"RB_close_juanlian_2")
        self.RB_close_juanlian_2.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.RB_close_juanlian_2)


        self.horizontalLayout_18.addLayout(self.verticalLayout_28)


        self.gridLayout_4.addWidget(self.frame_4, 0, 3, 1, 1)

        self.frame_8 = QFrame(self.frame_k)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Box)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setLineWidth(0)
        self.frame_8.setMidLineWidth(2)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_11)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.RB_open_shuibeng = QRadioButton(self.frame_8)
        self.RB_open_shuibeng.setObjectName(u"RB_open_shuibeng")
        self.RB_open_shuibeng.setStyleSheet(u"")

        self.verticalLayout_34.addWidget(self.RB_open_shuibeng)

        self.RB_close_shuibeng = QRadioButton(self.frame_8)
        self.RB_close_shuibeng.setObjectName(u"RB_close_shuibeng")
        self.RB_close_shuibeng.setStyleSheet(u"")

        self.verticalLayout_34.addWidget(self.RB_close_shuibeng)


        self.horizontalLayout_24.addLayout(self.verticalLayout_34)


        self.gridLayout_4.addWidget(self.frame_8, 1, 1, 1, 1)

        self.frame_6 = QFrame(self.frame_k)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Box)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setLineWidth(0)
        self.frame_6.setMidLineWidth(2)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_9)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.RB_open_tongfeng = QRadioButton(self.frame_6)
        self.RB_open_tongfeng.setObjectName(u"RB_open_tongfeng")
        self.RB_open_tongfeng.setStyleSheet(u"")

        self.verticalLayout_32.addWidget(self.RB_open_tongfeng)

        self.RB_close_tongfeng = QRadioButton(self.frame_6)
        self.RB_close_tongfeng.setObjectName(u"RB_close_tongfeng")
        self.RB_close_tongfeng.setStyleSheet(u"")

        self.verticalLayout_32.addWidget(self.RB_close_tongfeng)


        self.horizontalLayout_22.addLayout(self.verticalLayout_32)


        self.gridLayout_4.addWidget(self.frame_6, 1, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_k)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Box)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setLineWidth(0)
        self.frame_7.setMidLineWidth(2)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_10)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.RB_open_jire = QRadioButton(self.frame_7)
        self.RB_open_jire.setObjectName(u"RB_open_jire")
        self.RB_open_jire.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.RB_open_jire)

        self.RB_close_jire = QRadioButton(self.frame_7)
        self.RB_close_jire.setObjectName(u"RB_close_jire")
        self.RB_close_jire.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.RB_close_jire)


        self.horizontalLayout_23.addLayout(self.verticalLayout_33)


        self.gridLayout_4.addWidget(self.frame_7, 1, 2, 1, 1)

        self.frame_2 = QFrame(self.frame_k)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setMidLineWidth(2)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_6)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.RB_open_buguang = QRadioButton(self.frame_2)
        self.RB_open_buguang.setObjectName(u"RB_open_buguang")
        self.RB_open_buguang.setStyleSheet(u"")

        self.verticalLayout_29.addWidget(self.RB_open_buguang)

        self.RB_close_buguang = QRadioButton(self.frame_2)
        self.RB_close_buguang.setObjectName(u"RB_close_buguang")
        self.RB_close_buguang.setStyleSheet(u"")

        self.verticalLayout_29.addWidget(self.RB_close_buguang)


        self.horizontalLayout_19.addLayout(self.verticalLayout_29)


        self.gridLayout_4.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame_9 = QFrame(self.frame_k)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Box)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_9.setLineWidth(0)
        self.frame_9.setMidLineWidth(2)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_13)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.RB_open_shuifeiyitiji = QRadioButton(self.frame_9)
        self.RB_open_shuifeiyitiji.setObjectName(u"RB_open_shuifeiyitiji")
        self.RB_open_shuifeiyitiji.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.RB_open_shuifeiyitiji)

        self.RB_close_shuifeiyitiji_2 = QRadioButton(self.frame_9)
        self.RB_close_shuifeiyitiji_2.setObjectName(u"RB_close_shuifeiyitiji_2")
        self.RB_close_shuifeiyitiji_2.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.RB_close_shuifeiyitiji_2)

        self.RB_open_shuifeiyitiji_3 = QRadioButton(self.frame_9)
        self.RB_open_shuifeiyitiji_3.setObjectName(u"RB_open_shuifeiyitiji_3")
        self.RB_open_shuifeiyitiji_3.setStyleSheet(u"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.RB_open_shuifeiyitiji_3)

        self.RB_open_shuifeiyitiji_2 = QRadioButton(self.frame_9)
        self.RB_open_shuifeiyitiji_2.setObjectName(u"RB_open_shuifeiyitiji_2")
        self.RB_open_shuifeiyitiji_2.setStyleSheet(u"")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.RB_open_shuifeiyitiji_2)


        self.horizontalLayout_26.addLayout(self.formLayout)


        self.gridLayout_4.addWidget(self.frame_9, 2, 0, 1, 2)

        self.frame_5 = QFrame(self.frame_k)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(0)
        self.frame_5.setMidLineWidth(2)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_8)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.RB_open_juanmo = QRadioButton(self.frame_5)
        self.RB_open_juanmo.setObjectName(u"RB_open_juanmo")
        self.RB_open_juanmo.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.RB_open_juanmo)

        self.RB_close_juanmo = QRadioButton(self.frame_5)
        self.RB_close_juanmo.setObjectName(u"RB_close_juanmo")
        self.RB_close_juanmo.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.RB_close_juanmo)

        self.RB_close_juanmo_2 = QRadioButton(self.frame_5)
        self.RB_close_juanmo_2.setObjectName(u"RB_close_juanmo_2")
        self.RB_close_juanmo_2.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.RB_close_juanmo_2)


        self.horizontalLayout_21.addLayout(self.verticalLayout_31)


        self.gridLayout_4.addWidget(self.frame_5, 1, 3, 1, 1)

        self.stackedWidget.addWidget(self.manual_control_page)
        self.cloud_page = QWidget()
        self.cloud_page.setObjectName(u"cloud_page")
        self.cloud_page.setStyleSheet(u"")
        self.verticalLayout_21 = QVBoxLayout(self.cloud_page)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame = QFrame(self.cloud_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_19 = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_19)

        self.btn_get_12data = QPushButton(self.frame)
        self.btn_get_12data.setObjectName(u"btn_get_12data")
        self.btn_get_12data.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_11.addWidget(self.btn_get_12data)

        self.horizontalSpacer_20 = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_20)

        self.label_time = QLabel(self.frame)
        self.label_time.setObjectName(u"label_time")

        self.horizontalLayout_11.addWidget(self.label_time)


        self.verticalLayout_21.addWidget(self.frame)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.graphicsView = QGraphicsView(self.cloud_page)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout_6.addWidget(self.graphicsView)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)

        self.graphicsView_4 = QGraphicsView(self.cloud_page)
        self.graphicsView_4.setObjectName(u"graphicsView_4")

        self.horizontalLayout_6.addWidget(self.graphicsView_4)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.graphicsView_2 = QGraphicsView(self.cloud_page)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.horizontalLayout_6.addWidget(self.graphicsView_2)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)


        self.verticalLayout_21.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.text_humidness = QLineEdit(self.cloud_page)
        self.text_humidness.setObjectName(u"text_humidness")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(14)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setKerning(True)
        self.text_humidness.setFont(font5)
        self.text_humidness.setLayoutDirection(Qt.LeftToRight)
        self.text_humidness.setStyleSheet(u"")
        self.text_humidness.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.text_humidness)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.text_temperature = QLineEdit(self.cloud_page)
        self.text_temperature.setObjectName(u"text_temperature")
        self.text_temperature.setStyleSheet(u"")
        self.text_temperature.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.text_temperature)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.text_illumination = QLineEdit(self.cloud_page)
        self.text_illumination.setObjectName(u"text_illumination")
        self.text_illumination.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.text_illumination)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_21.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_13)

        self.graphicsView_3 = QGraphicsView(self.cloud_page)
        self.graphicsView_3.setObjectName(u"graphicsView_3")

        self.horizontalLayout_8.addWidget(self.graphicsView_3)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_14)

        self.graphicsView_5 = QGraphicsView(self.cloud_page)
        self.graphicsView_5.setObjectName(u"graphicsView_5")

        self.horizontalLayout_8.addWidget(self.graphicsView_5)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_15)

        self.graphicsView_6 = QGraphicsView(self.cloud_page)
        self.graphicsView_6.setObjectName(u"graphicsView_6")

        self.horizontalLayout_8.addWidget(self.graphicsView_6)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_16)


        self.verticalLayout_21.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.lineEdit_3 = QLineEdit(self.cloud_page)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lineEdit_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.lineEdit_4 = QLineEdit(self.cloud_page)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lineEdit_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.lineEdit_2 = QLineEdit(self.cloud_page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lineEdit_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)


        self.verticalLayout_21.addLayout(self.horizontalLayout_10)

        self.frame_10 = QFrame(self.cloud_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_18)

        self.pushButton_10 = QPushButton(self.frame_10)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_13.addWidget(self.pushButton_10)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_17)


        self.verticalLayout_21.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.cloud_page)
        self.information_page = QWidget()
        self.information_page.setObjectName(u"information_page")
        self.textBrowser = QTextBrowser(self.information_page)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(70, 30, 811, 351))
        self.textBrowser.setInputMethodHints(Qt.ImhNone)
        self.stackedWidget.addWidget(self.information_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_change_topic = QPushButton(self.topMenus)
        self.btn_change_topic.setObjectName(u"btn_change_topic")
        sizePolicy.setHeightForWidth(self.btn_change_topic.sizePolicy().hasHeightForWidth())
        self.btn_change_topic.setSizePolicy(sizePolicy)
        self.btn_change_topic.setMinimumSize(QSize(0, 45))
        self.btn_change_topic.setFont(font)
        self.btn_change_topic.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_change_topic.setLayoutDirection(Qt.LeftToRight)
        self.btn_change_topic.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-moon.png);")

        self.verticalLayout_14.addWidget(self.btn_change_topic)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 30))
        self.bottomBar.setMaximumSize(QSize(16777215, 30))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setBold(False)
        font6.setItalic(False)
        self.creditsLabel.setFont(font6)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.gridLayout_2.addWidget(self.bgApp, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"\u5185\u8499\u53e4\u5de5\u4e1a\u5927\u5b66", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"\u80fd\u6e90\u4e0e\u52a8\u529b\u5de5\u7a0b\u5b66\u9662", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf", None))
        self.btn_cloud.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u7aef\u6570\u636e\u663e\u793a", None))
        self.btn_manual_control.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52a8\u8fdc\u7a0b\u63a7\u5236", None))
        self.btn_auto_control.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u63a7\u5236", None))
        self.btn_energy.setText(QCoreApplication.translate("MainWindow", u"\u80fd\u91cf\u6536\u652f", None))
        self.btn_information.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u8f6f\u4ef6", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"\u8f6f\u4ef6\u4ecb\u7ecd", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"SoftwareInfor", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">\u7cfb\u7edf\u4ecb\u7ecd</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#55aaff;\">\u8be5\u8f6f\u4ef6\u7cfb\u7edf\u6839\u636e\u5b9e\u9645\u9700\u6c42\uff0c\u63d0\u4f9b\u4e86\u4e00\u4e2a\u6e29\u5ea6\u3001\u6e7f\u5ea6\u3001\u5149\u7167\u3001\u6c14\u4f53\u3001\u6c34\u80a5\u53ca"
                        "\u6c14\u8c61\u7b49\u7f51\u7edc\u4f20\u611f\u5668\u6570\u636e\u7684\u7efc\u5408\u5e73\u53f0\uff0c\u540c\u65f6\u4e3a\u5b9e\u9a8c\u5e73\u53f0\u63d0\u4f9b\u5927\u68da\u5377\u5e18\u3001\u6c34\u80a5\u3001\u901a\u98ce\u3001\u8865\u5149\u3001\u8865\u70ed\u7b49\u6267\u884c\u5668\u7684\u624b\u52a8\u53ca\u81ea\u52a8\u63a7\u5236\u529f\u80fd\u3002\u8f6f\u4ef6\u4f7f\u7528 Python\u3001 PySide \u7f16\u5199(\u652f\u6301 PyQt).</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#55aaff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\""
                        " font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\u667a\u80fd\u7269\u8054\u7f51\u6e29\u5ba4\u73af\u5883\u81ea\u52a8\u63a7\u5236\u7cfb\u7edf", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4ea7\u751f\u7535\u80fd\u603b\u91cf\uff1aXXXXX                           \u6d88\u8017\u7535\u80fd\u603b\u91cf\uff1a XXXX", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u592a\u9633\u8f90\u5c04\u80fd\u603b\u91cf\uff1aXXXX                \u8017\u6563\u70ed\u80fd\u603b\u91cf\uff1aXXXXX", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u70ed\u80fd\u603b\u91cf\uff1aXXXXX                          \u8017\u6563\u70ed\u80fd\u603b\u91cf\uff1aXXXXX", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"\u5ea6", None))
        self.lineEdit_10.setText(QCoreApplication.translate("MainWindow", u"CO2\u6d53\u5ea6\uff1a", None))
        self.lineEdit_13.setText(QCoreApplication.translate("MainWindow", u"umol/m2s    (PPFD)", None))
#if QT_CONFIG(accessibility)
        self.lineEdit_8.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(accessibility)
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"\u571f\u58e4\u6e7f\u5ea6\uff1a", None))
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u"ppm", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u63a7\u5236", None))
        self.lineEdit_9.setText(QCoreApplication.translate("MainWindow", u"% ", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u73af\u5883\u503c\u8bbe\u7f6e\uff1a", None))
        self.lineEdit_12.setText(QCoreApplication.translate("MainWindow", u"\u5149\u7167\u5f3a\u5ea6\uff1a", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"\u7efc\u5408\u6e29\u5ea6\u503c\uff1a", None))
        self.lineEdit_14.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6\u73af\u5883\u6570\u636e\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6587\u4ef6\u8def\u5f84", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"\u63a7\u5236\u6570\u636e\u6587\u4ef6\u6a21\u677f\u89c1\u8bf4\u660e\u4e66", None))
        self.lineEdit_15.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6\u73af\u5883\u6570\u636e\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7167\u660e\u706f", None))
        self.RB_open_zhaoming.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.RB_close_zhaoming.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u70ed\u706f", None))
        self.RB_open_jiare.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.RB_close_jiare.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5377\u5e18\u673a", None))
        self.RB_open_juanlian.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u5377", None))
        self.RB_close_juanlian.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.RB_close_juanlian_2.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u653e", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u6cf5", None))
        self.RB_open_shuibeng.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.RB_close_shuibeng.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u901a\u98ce\u673a", None))
        self.RB_open_tongfeng.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.RB_close_tongfeng.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u96c6\u70ed\u5668", None))
        self.RB_open_jire.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.RB_close_jire.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8865\u5149\u706f", None))
        self.RB_open_buguang.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.RB_close_buguang.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u80a5\u4e00\u4f53\u673a", None))
        self.RB_open_shuifeiyitiji.setText(QCoreApplication.translate("MainWindow", u"\u8865\u6c34", None))
        self.RB_close_shuifeiyitiji_2.setText(QCoreApplication.translate("MainWindow", u"\u65bd\u80a5", None))
        self.RB_open_shuifeiyitiji_3.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u65bd\u80a5", None))
        self.RB_open_shuifeiyitiji_2.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u8865\u6c34", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5377\u819c\u673a", None))
        self.RB_open_juanmo.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u5377", None))
        self.RB_close_juanmo.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.RB_close_juanmo_2.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u653e", None))
        self.btn_get_12data.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u83b7\u53d612\u5c0f\u65f6\u73af\u5883\u6570\u636e", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u65f6\u95f4\uff1a", None))
        self.text_humidness.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u6c14\u6e7f\u5ea6", None))
        self.text_temperature.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u6c14\u6e29\u5ea6", None))
        self.text_illumination.setText(QCoreApplication.translate("MainWindow", u"\u5149\u7167\u5f3a\u5ea6", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"\u571f\u58e4\u6e29\u5ea6", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"\u571f\u58e4\u6e7f\u5ea6", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"\u4e8c\u6c27\u5316\u78b3\u6d53\u5ea6", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u767b\u9646\u4e91\u5e73\u53f0http://www.0531yun.com \u67e5\u770b\u8be6\u7ec6\u4fe1\u606f", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">       \u672c\u8f6f\u4ef6\u57fa\u4e8e\u201cxxx\u9879\u76ee\u201d\u592a\u9633\u80fd\u667a\u80fd\u6e29\u5ba4\u5927\u68da\u5b9e\u9645\u5e94\u7528\u5f00\u53d1\uff0c\u96c6\u6210\u5e38\u7528\u6e29\u5ba4\u5927\u68da\u6570\u636e\u91c7\u96c6\u5668\u53ca\u63a7\u5236\u5668\uff0c\u914d\u5408\u4e13\u7528\u201c\u81ea\u52a8\u63a7\u5236\u7cfb\u7edf&quot;\u786c\u4ef6\u4f7f\u7528\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> "
                        "      \u8f6f\u4ef6\u7248\u6743\u5f52\u201c\u5185\u8499\u53e4\u777f\u529b\u80fd\u6e90\u6709\u9650\u516c\u53f8\u201d\u6240\u6709\uff0c\u975e\u7ecf\u516c\u53f8\u6388\u6743\uff0c\u4e0d\u80fd\u5c06\u5176\u7528\u4e8e\u76c8\u5229\u6216\u975e\u76c8\u5229\u7684\u4efb\u4f55\u7528\u9014\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     \u8f6f\u4ef6\u6280\u672f\u652f\u6301\u8bf7\u8054\u7cfb\uff1a15389769877</p></body></html>", None))
        self.btn_change_topic.setText(QCoreApplication.translate("MainWindow", u"\u6539\u53d8\u4e3b\u9898", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u8bbe\u529f\u80fd2print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u8bbe\u529f\u80fd1logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: han zheng", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi

