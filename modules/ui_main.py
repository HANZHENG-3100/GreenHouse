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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTextBrowser, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1314, 780)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
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
        self.verticalLayout_19 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Sunken)
        self.bgApp.setMidLineWidth(1)
        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setGeometry(QRect(66, 1, 0, 541))
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(16777215, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 16777215))
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
        self.extraCenter.setMinimumSize(QSize(0, 0))
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)


        self.extraColumLayout.addWidget(self.extraContent)

        self.gridLayout_9 = QGridLayout(self.bgApp)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(240, 760))
        self.leftMenuBg.setMaximumSize(QSize(0, 16777215))
        self.leftMenuBg.setContextMenuPolicy(Qt.NoContextMenu)
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topLogoInfo.sizePolicy().hasHeightForWidth())
        self.topLogoInfo.setSizePolicy(sizePolicy)
        self.topLogoInfo.setMinimumSize(QSize(240, 60))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.topLogoInfo)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.titleLeftApp.setFont(font)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_8.addWidget(self.titleLeftApp, 0, 1, 1, 1)

        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setMinimumSize(QSize(0, 30))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftDescription.setFont(font1)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_8.addWidget(self.titleLeftDescription, 1, 1, 1, 1)

        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setMinimumSize(QSize(60, 60))
        self.topLogo.setMaximumSize(QSize(60, 60))
        self.topLogo.setStyleSheet(u"image: url(:/images/images/images/PyDracula .png);")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Plain)

        self.gridLayout_8.addWidget(self.topLogo, 0, 0, 2, 1)


        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(69, 0))
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        sizePolicy.setHeightForWidth(self.toggleBox.sizePolicy().hasHeightForWidth())
        self.toggleBox.setSizePolicy(sizePolicy)
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        self.toggleButton.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
        self.toggleButton.setMinimumSize(QSize(60, 45))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        self.toggleButton.setFont(font2)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setMouseTracking(True)
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setAutoFillBackground(False)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalLayout_2.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        sizePolicy.setHeightForWidth(self.topMenu.sizePolicy().hasHeightForWidth())
        self.topMenu.setSizePolicy(sizePolicy)
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_cloud1 = QPushButton(self.topMenu)
        self.btn_cloud1.setObjectName(u"btn_cloud1")
        self.btn_cloud1.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.btn_cloud1.sizePolicy().hasHeightForWidth())
        self.btn_cloud1.setSizePolicy(sizePolicy1)
        self.btn_cloud1.setMinimumSize(QSize(60, 45))
        self.btn_cloud1.setFont(font2)
        self.btn_cloud1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cloud1.setLayoutDirection(Qt.LeftToRight)
        self.btn_cloud1.setAutoFillBackground(False)
        self.btn_cloud1.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-cloudy.png);")
        self.btn_cloud1.setIconSize(QSize(16, 16))

        self.verticalLayout_8.addWidget(self.btn_cloud1)

        self.btn_cloud2 = QPushButton(self.topMenu)
        self.btn_cloud2.setObjectName(u"btn_cloud2")
        sizePolicy1.setHeightForWidth(self.btn_cloud2.sizePolicy().hasHeightForWidth())
        self.btn_cloud2.setSizePolicy(sizePolicy1)
        self.btn_cloud2.setMinimumSize(QSize(60, 45))
        self.btn_cloud2.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-cloudy.png);")

        self.verticalLayout_8.addWidget(self.btn_cloud2)

        self.btn_manual_control1 = QPushButton(self.topMenu)
        self.btn_manual_control1.setObjectName(u"btn_manual_control1")
        sizePolicy1.setHeightForWidth(self.btn_manual_control1.sizePolicy().hasHeightForWidth())
        self.btn_manual_control1.setSizePolicy(sizePolicy1)
        self.btn_manual_control1.setMinimumSize(QSize(60, 45))
        self.btn_manual_control1.setFont(font2)
        self.btn_manual_control1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_manual_control1.setLayoutDirection(Qt.LeftToRight)
        self.btn_manual_control1.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-hand-point-up.png);")

        self.verticalLayout_8.addWidget(self.btn_manual_control1)

        self.btn_manual_control2 = QPushButton(self.topMenu)
        self.btn_manual_control2.setObjectName(u"btn_manual_control2")
        sizePolicy1.setHeightForWidth(self.btn_manual_control2.sizePolicy().hasHeightForWidth())
        self.btn_manual_control2.setSizePolicy(sizePolicy1)
        self.btn_manual_control2.setMinimumSize(QSize(60, 45))
        self.btn_manual_control2.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-hand-point-up.png);")

        self.verticalLayout_8.addWidget(self.btn_manual_control2)

        self.btn_auto_control = QPushButton(self.topMenu)
        self.btn_auto_control.setObjectName(u"btn_auto_control")
        sizePolicy1.setHeightForWidth(self.btn_auto_control.sizePolicy().hasHeightForWidth())
        self.btn_auto_control.setSizePolicy(sizePolicy1)
        self.btn_auto_control.setMinimumSize(QSize(60, 45))
        self.btn_auto_control.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-change.png);")

        self.verticalLayout_8.addWidget(self.btn_auto_control)

        self.btn_energy = QPushButton(self.topMenu)
        self.btn_energy.setObjectName(u"btn_energy")
        sizePolicy1.setHeightForWidth(self.btn_energy.sizePolicy().hasHeightForWidth())
        self.btn_energy.setSizePolicy(sizePolicy1)
        self.btn_energy.setMinimumSize(QSize(60, 45))
        self.btn_energy.setFont(font2)
        self.btn_energy.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_energy.setLayoutDirection(Qt.LeftToRight)
        self.btn_energy.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-speedometer.png);")

        self.verticalLayout_8.addWidget(self.btn_energy)

        self.btn_information = QPushButton(self.topMenu)
        self.btn_information.setObjectName(u"btn_information")
        sizePolicy1.setHeightForWidth(self.btn_information.sizePolicy().hasHeightForWidth())
        self.btn_information.setSizePolicy(sizePolicy1)
        self.btn_information.setMinimumSize(QSize(60, 45))
        self.btn_information.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-closed.png);")

        self.verticalLayout_8.addWidget(self.btn_information)


        self.verticalLayout_2.addWidget(self.topMenu)

        self.label_3 = QLabel(self.leftMenuFrame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        sizePolicy.setHeightForWidth(self.bottomMenu.sizePolicy().hasHeightForWidth())
        self.bottomMenu.setSizePolicy(sizePolicy)
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.bottomMenu.setLineWidth(5)
        self.formLayout = QFormLayout(self.bottomMenu)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy1.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy1)
        self.toggleLeftBox.setMinimumSize(QSize(60, 45))
        self.toggleLeftBox.setFont(font2)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.toggleLeftBox)


        self.verticalLayout_2.addWidget(self.bottomMenu)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)

        self.leftMenuFrame.raise_()
        self.topLogoInfo.raise_()

        self.gridLayout_9.addWidget(self.leftMenuBg, 0, 0, 1, 1)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.contentBox)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 60))
        self.contentTopBg.setMaximumSize(QSize(16777215, 60))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        self.titleRightInfo.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMinimumSize(QSize(1, 60))
        self.titleRightInfo.setMaximumSize(QSize(16777215, 80))
        self.titleRightInfo.setSizeIncrement(QSize(0, 6))
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
        self.rightButtons.setMinimumSize(QSize(0, 50))
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


        self.horizontalLayout.addWidget(self.rightButtons)


        self.verticalLayout_16.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.contentBottom.sizePolicy().hasHeightForWidth())
        self.contentBottom.setSizePolicy(sizePolicy4)
        self.contentBottom.setMinimumSize(QSize(1000, 580))
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setMinimumSize(QSize(0, 0))
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pagesContainer.sizePolicy().hasHeightForWidth())
        self.pagesContainer.setSizePolicy(sizePolicy5)
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font2)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.energy_page = QWidget()
        self.energy_page.setObjectName(u"energy_page")
        self.energy_page.setStyleSheet(u"")
        self.verticalLayout_18 = QVBoxLayout(self.energy_page)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.energy_page_row_2 = QFrame(self.energy_page)
        self.energy_page_row_2.setObjectName(u"energy_page_row_2")
        self.energy_page_row_2.setMinimumSize(QSize(150, 100))
        self.energy_page_row_2.setFrameShape(QFrame.StyledPanel)
        self.energy_page_row_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.energy_page_row_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")

        self.gridLayout_5.addWidget(self.energy_page_row_2, 0, 0, 1, 1)

        self.energy_page_row_3 = QFrame(self.energy_page)
        self.energy_page_row_3.setObjectName(u"energy_page_row_3")
        self.energy_page_row_3.setFrameShape(QFrame.StyledPanel)
        self.energy_page_row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.energy_page_row_3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")

        self.gridLayout_5.addWidget(self.energy_page_row_3, 1, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label = QLabel(self.energy_page)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.label)

        self.label_2 = QLabel(self.energy_page)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_14.addWidget(self.label_2)


        self.gridLayout_5.addLayout(self.horizontalLayout_14, 2, 0, 1, 1)


        self.verticalLayout_18.addLayout(self.gridLayout_5)

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
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(4)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.auto_control_page_row_1.sizePolicy().hasHeightForWidth())
        self.auto_control_page_row_1.setSizePolicy(sizePolicy6)
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
        sizePolicy1.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy1)
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

        self.btn_auto_control_2 = QPushButton(self.auto_control_page_row_1)
        self.btn_auto_control_2.setObjectName(u"btn_auto_control_2")

        self.gridLayout_3.addWidget(self.btn_auto_control_2, 1, 6, 1, 1)

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
        self.btn_open_control_file = QPushButton(self.frame_content_wid_1)
        self.btn_open_control_file.setObjectName(u"btn_open_control_file")
        self.btn_open_control_file.setMinimumSize(QSize(150, 30))
        self.btn_open_control_file.setFont(font2)
        self.btn_open_control_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_control_file.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_open_control_file.setIcon(icon4)

        self.gridLayout.addWidget(self.btn_open_control_file, 0, 1, 1, 1)

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
        self.manual_control_page1 = QWidget()
        self.manual_control_page1.setObjectName(u"manual_control_page1")
        self.verticalLayout_17 = QVBoxLayout(self.manual_control_page1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_k = QFrame(self.manual_control_page1)
        self.frame_k.setObjectName(u"frame_k")
        sizePolicy4.setHeightForWidth(self.frame_k.sizePolicy().hasHeightForWidth())
        self.frame_k.setSizePolicy(sizePolicy4)
        self.frame_k.setMinimumSize(QSize(600, 400))
        self.frame_k.setMaximumSize(QSize(16777215, 16777215))
        self.frame_k.setFrameShape(QFrame.StyledPanel)
        self.frame_k.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_k)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 10, 0)
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
        self.Rbtn_mc2_up = QRadioButton(self.frame_5)
        self.Rbtn_mc2_up.setObjectName(u"Rbtn_mc2_up")
        self.Rbtn_mc2_up.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.Rbtn_mc2_up)

        self.Rbtn_mc2_stop = QRadioButton(self.frame_5)
        self.Rbtn_mc2_stop.setObjectName(u"Rbtn_mc2_stop")
        self.Rbtn_mc2_stop.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.Rbtn_mc2_stop)

        self.Rbtn_mc2_down = QRadioButton(self.frame_5)
        self.Rbtn_mc2_down.setObjectName(u"Rbtn_mc2_down")
        self.Rbtn_mc2_down.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.Rbtn_mc2_down)


        self.horizontalLayout_21.addLayout(self.verticalLayout_31)


        self.gridLayout_4.addWidget(self.frame_5, 0, 2, 1, 1)

        self.frame_28 = QFrame(self.frame_k)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Box)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.frame_28.setLineWidth(0)
        self.frame_28.setMidLineWidth(2)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_11 = QLabel(self.frame_28)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_11)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.Rbtn_mc11_open = QRadioButton(self.frame_28)
        self.Rbtn_mc11_open.setObjectName(u"Rbtn_mc11_open")
        self.Rbtn_mc11_open.setStyleSheet(u"")

        self.verticalLayout_34.addWidget(self.Rbtn_mc11_open)

        self.RB_close_shuibeng = QRadioButton(self.frame_28)
        self.RB_close_shuibeng.setObjectName(u"RB_close_shuibeng")
        self.RB_close_shuibeng.setStyleSheet(u"")

        self.verticalLayout_34.addWidget(self.RB_close_shuibeng)


        self.horizontalLayout_24.addLayout(self.verticalLayout_34)


        self.gridLayout_4.addWidget(self.frame_28, 3, 3, 1, 1)

        self.frame_25 = QFrame(self.frame_k)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Box)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.frame_25.setLineWidth(0)
        self.frame_25.setMidLineWidth(2)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_6 = QLabel(self.frame_25)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_6)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.Rbtn_mc3_open = QRadioButton(self.frame_25)
        self.Rbtn_mc3_open.setObjectName(u"Rbtn_mc3_open")
        self.Rbtn_mc3_open.setStyleSheet(u"")

        self.verticalLayout_29.addWidget(self.Rbtn_mc3_open)

        self.RB_close_buguang = QRadioButton(self.frame_25)
        self.RB_close_buguang.setObjectName(u"RB_close_buguang")
        self.RB_close_buguang.setStyleSheet(u"")

        self.verticalLayout_29.addWidget(self.RB_close_buguang)


        self.horizontalLayout_19.addLayout(self.verticalLayout_29)


        self.gridLayout_4.addWidget(self.frame_25, 0, 3, 1, 1)

        self.frame_13 = QFrame(self.frame_k)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Box)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.frame_13.setLineWidth(0)
        self.frame_13.setMidLineWidth(2)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_17 = QLabel(self.frame_13)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_17)

        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.Rbtn_mc10_open = QRadioButton(self.frame_13)
        self.Rbtn_mc10_open.setObjectName(u"Rbtn_mc10_open")
        self.Rbtn_mc10_open.setStyleSheet(u"")

        self.verticalLayout_39.addWidget(self.Rbtn_mc10_open)

        self.RB_close_jire_4 = QRadioButton(self.frame_13)
        self.RB_close_jire_4.setObjectName(u"RB_close_jire_4")
        self.RB_close_jire_4.setStyleSheet(u"")

        self.verticalLayout_39.addWidget(self.RB_close_jire_4)


        self.horizontalLayout_29.addLayout(self.verticalLayout_39)


        self.gridLayout_4.addWidget(self.frame_13, 3, 2, 1, 1)

        self.frame_29 = QFrame(self.frame_k)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.Box)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.frame_29.setLineWidth(0)
        self.frame_29.setMidLineWidth(2)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_12 = QLabel(self.frame_29)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_12)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.Rbtn_mc12_open = QRadioButton(self.frame_29)
        self.Rbtn_mc12_open.setObjectName(u"Rbtn_mc12_open")
        self.Rbtn_mc12_open.setStyleSheet(u"")

        self.verticalLayout_35.addWidget(self.Rbtn_mc12_open)

        self.RB_close_shuibeng_2 = QRadioButton(self.frame_29)
        self.RB_close_shuibeng_2.setObjectName(u"RB_close_shuibeng_2")
        self.RB_close_shuibeng_2.setStyleSheet(u"")

        self.verticalLayout_35.addWidget(self.RB_close_shuibeng_2)


        self.horizontalLayout_25.addLayout(self.verticalLayout_35)


        self.gridLayout_4.addWidget(self.frame_29, 3, 5, 1, 1)

        self.frame_27 = QFrame(self.frame_k)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Box)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.frame_27.setLineWidth(0)
        self.frame_27.setMidLineWidth(2)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_7 = QLabel(self.frame_27)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_7)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.Rbtn_mc6_open = QRadioButton(self.frame_27)
        self.Rbtn_mc6_open.setObjectName(u"Rbtn_mc6_open")
        self.Rbtn_mc6_open.setStyleSheet(u"")

        self.verticalLayout_30.addWidget(self.Rbtn_mc6_open)

        self.RB_close_jiare = QRadioButton(self.frame_27)
        self.RB_close_jiare.setObjectName(u"RB_close_jiare")
        self.RB_close_jiare.setStyleSheet(u"")

        self.verticalLayout_30.addWidget(self.RB_close_jiare)


        self.horizontalLayout_20.addLayout(self.verticalLayout_30)


        self.gridLayout_4.addWidget(self.frame_27, 1, 2, 1, 1)

        self.frame_12 = QFrame(self.frame_k)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Box)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_12.setLineWidth(0)
        self.frame_12.setMidLineWidth(2)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_16 = QLabel(self.frame_12)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_16)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.Rbtn_mc9_open = QRadioButton(self.frame_12)
        self.Rbtn_mc9_open.setObjectName(u"Rbtn_mc9_open")
        self.Rbtn_mc9_open.setStyleSheet(u"")

        self.verticalLayout_38.addWidget(self.Rbtn_mc9_open)

        self.RB_close_jire_3 = QRadioButton(self.frame_12)
        self.RB_close_jire_3.setObjectName(u"RB_close_jire_3")
        self.RB_close_jire_3.setStyleSheet(u"")

        self.verticalLayout_38.addWidget(self.RB_close_jire_3)


        self.horizontalLayout_28.addLayout(self.verticalLayout_38)


        self.gridLayout_4.addWidget(self.frame_12, 3, 0, 1, 1)

        self.frame_11 = QFrame(self.frame_k)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Box)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_11.setLineWidth(0)
        self.frame_11.setMidLineWidth(2)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_15 = QLabel(self.frame_11)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_15)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.Rbtn_mc8_open = QRadioButton(self.frame_11)
        self.Rbtn_mc8_open.setObjectName(u"Rbtn_mc8_open")
        self.Rbtn_mc8_open.setStyleSheet(u"")

        self.verticalLayout_37.addWidget(self.Rbtn_mc8_open)

        self.RB_close_jire_2 = QRadioButton(self.frame_11)
        self.RB_close_jire_2.setObjectName(u"RB_close_jire_2")
        self.RB_close_jire_2.setStyleSheet(u"")

        self.verticalLayout_37.addWidget(self.RB_close_jire_2)


        self.horizontalLayout_27.addLayout(self.verticalLayout_37)


        self.gridLayout_4.addWidget(self.frame_11, 1, 5, 1, 1)

        self.frame_26 = QFrame(self.frame_k)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Box)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.frame_26.setLineWidth(0)
        self.frame_26.setMidLineWidth(2)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_4 = QLabel(self.frame_26)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_4)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.Rbtn_mc5_open = QRadioButton(self.frame_26)
        self.Rbtn_mc5_open.setObjectName(u"Rbtn_mc5_open")
        self.Rbtn_mc5_open.setStyleSheet(u"")

        self.verticalLayout_27.addWidget(self.Rbtn_mc5_open)

        self.RB_close_zhaoming = QRadioButton(self.frame_26)
        self.RB_close_zhaoming.setObjectName(u"RB_close_zhaoming")
        self.RB_close_zhaoming.setStyleSheet(u"")

        self.verticalLayout_27.addWidget(self.RB_close_zhaoming)


        self.horizontalLayout_17.addLayout(self.verticalLayout_27)


        self.gridLayout_4.addWidget(self.frame_26, 1, 0, 1, 1)

        self.frame_10 = QFrame(self.frame_k)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Box)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.frame_10.setLineWidth(0)
        self.frame_10.setMidLineWidth(2)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_13 = QLabel(self.frame_10)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_13)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.Rbtn_mc4_open = QRadioButton(self.frame_10)
        self.Rbtn_mc4_open.setObjectName(u"Rbtn_mc4_open")
        self.Rbtn_mc4_open.setStyleSheet(u"")

        self.verticalLayout_36.addWidget(self.Rbtn_mc4_open)

        self.RB_close_buguang_2 = QRadioButton(self.frame_10)
        self.RB_close_buguang_2.setObjectName(u"RB_close_buguang_2")
        self.RB_close_buguang_2.setStyleSheet(u"")

        self.verticalLayout_36.addWidget(self.RB_close_buguang_2)


        self.horizontalLayout_26.addLayout(self.verticalLayout_36)


        self.gridLayout_4.addWidget(self.frame_10, 0, 5, 1, 1)

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
        self.Rbtn_mc7_open = QRadioButton(self.frame_7)
        self.Rbtn_mc7_open.setObjectName(u"Rbtn_mc7_open")
        self.Rbtn_mc7_open.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.Rbtn_mc7_open)

        self.RB_close_jire = QRadioButton(self.frame_7)
        self.RB_close_jire.setObjectName(u"RB_close_jire")
        self.RB_close_jire.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.RB_close_jire)


        self.horizontalLayout_23.addLayout(self.verticalLayout_33)


        self.gridLayout_4.addWidget(self.frame_7, 1, 3, 1, 1)

        self.frame_4 = QFrame(self.frame_k)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setContextMenuPolicy(Qt.NoContextMenu)
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
        self.Rbtn_mc1_up = QRadioButton(self.frame_4)
        self.Rbtn_mc1_up.setObjectName(u"Rbtn_mc1_up")
        self.Rbtn_mc1_up.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.Rbtn_mc1_up)

        self.Rbtn_mc1_stop = QRadioButton(self.frame_4)
        self.Rbtn_mc1_stop.setObjectName(u"Rbtn_mc1_stop")
        self.Rbtn_mc1_stop.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.Rbtn_mc1_stop)

        self.Rbtn_mc1_down = QRadioButton(self.frame_4)
        self.Rbtn_mc1_down.setObjectName(u"Rbtn_mc1_down")
        self.Rbtn_mc1_down.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.Rbtn_mc1_down)


        self.horizontalLayout_18.addLayout(self.verticalLayout_28)


        self.gridLayout_4.addWidget(self.frame_4, 0, 0, 1, 1)


        self.verticalLayout_17.addWidget(self.frame_k)

        self.stackedWidget.addWidget(self.manual_control_page1)
        self.manual_control_page2 = QWidget()
        self.manual_control_page2.setObjectName(u"manual_control_page2")
        self.gridLayout_6 = QGridLayout(self.manual_control_page2)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 10, 0)
        self.frame_14 = QFrame(self.manual_control_page2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Box)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.frame_14.setLineWidth(0)
        self.frame_14.setMidLineWidth(2)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_14)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_18)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.Rbtn_mc14_open = QRadioButton(self.frame_14)
        self.Rbtn_mc14_open.setObjectName(u"Rbtn_mc14_open")
        self.Rbtn_mc14_open.setStyleSheet(u"")

        self.verticalLayout_40.addWidget(self.Rbtn_mc14_open)

        self.Rbtn_mc14_close = QRadioButton(self.frame_14)
        self.Rbtn_mc14_close.setObjectName(u"Rbtn_mc14_close")
        self.Rbtn_mc14_close.setStyleSheet(u"")

        self.verticalLayout_40.addWidget(self.Rbtn_mc14_close)


        self.horizontalLayout_30.addLayout(self.verticalLayout_40)


        self.gridLayout_6.addWidget(self.frame_14, 0, 1, 1, 1)

        self.frame_23 = QFrame(self.manual_control_page2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Box)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.frame_23.setLineWidth(0)
        self.frame_23.setMidLineWidth(2)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_27 = QLabel(self.frame_23)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_27)

        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.Rbtn_mc20_open = QRadioButton(self.frame_23)
        self.Rbtn_mc20_open.setObjectName(u"Rbtn_mc20_open")
        self.Rbtn_mc20_open.setStyleSheet(u"")

        self.verticalLayout_49.addWidget(self.Rbtn_mc20_open)

        self.Rbtn_mc20_close = QRadioButton(self.frame_23)
        self.Rbtn_mc20_close.setObjectName(u"Rbtn_mc20_close")
        self.Rbtn_mc20_close.setStyleSheet(u"")

        self.verticalLayout_49.addWidget(self.Rbtn_mc20_close)


        self.horizontalLayout_39.addLayout(self.verticalLayout_49)


        self.gridLayout_6.addWidget(self.frame_23, 1, 3, 1, 1)

        self.frame_17 = QFrame(self.manual_control_page2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Box)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.frame_17.setLineWidth(0)
        self.frame_17.setMidLineWidth(2)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_21 = QLabel(self.frame_17)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_21)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.Rbtn_mc17_open = QRadioButton(self.frame_17)
        self.Rbtn_mc17_open.setObjectName(u"Rbtn_mc17_open")
        self.Rbtn_mc17_open.setStyleSheet(u"")

        self.verticalLayout_43.addWidget(self.Rbtn_mc17_open)

        self.Rbtn_mc17_close = QRadioButton(self.frame_17)
        self.Rbtn_mc17_close.setObjectName(u"Rbtn_mc17_close")
        self.Rbtn_mc17_close.setStyleSheet(u"")

        self.verticalLayout_43.addWidget(self.Rbtn_mc17_close)


        self.horizontalLayout_33.addLayout(self.verticalLayout_43)


        self.gridLayout_6.addWidget(self.frame_17, 1, 0, 1, 1)

        self.frame_18 = QFrame(self.manual_control_page2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Box)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.frame_18.setLineWidth(0)
        self.frame_18.setMidLineWidth(2)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_22 = QLabel(self.frame_18)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_22)

        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.Rbtn_mc18_open = QRadioButton(self.frame_18)
        self.Rbtn_mc18_open.setObjectName(u"Rbtn_mc18_open")
        self.Rbtn_mc18_open.setStyleSheet(u"")

        self.verticalLayout_44.addWidget(self.Rbtn_mc18_open)

        self.Rbtn_mc18_close = QRadioButton(self.frame_18)
        self.Rbtn_mc18_close.setObjectName(u"Rbtn_mc18_close")
        self.Rbtn_mc18_close.setStyleSheet(u"")

        self.verticalLayout_44.addWidget(self.Rbtn_mc18_close)


        self.horizontalLayout_34.addLayout(self.verticalLayout_44)


        self.gridLayout_6.addWidget(self.frame_18, 1, 1, 1, 1)

        self.frame_24 = QFrame(self.manual_control_page2)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Box)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.frame_24.setLineWidth(0)
        self.frame_24.setMidLineWidth(2)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_28 = QLabel(self.frame_24)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.label_28)

        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.Rbtn_mc24_open = QRadioButton(self.frame_24)
        self.Rbtn_mc24_open.setObjectName(u"Rbtn_mc24_open")
        self.Rbtn_mc24_open.setStyleSheet(u"")

        self.verticalLayout_50.addWidget(self.Rbtn_mc24_open)

        self.Rbtn_mc24_close = QRadioButton(self.frame_24)
        self.Rbtn_mc24_close.setObjectName(u"Rbtn_mc24_close")
        self.Rbtn_mc24_close.setStyleSheet(u"")

        self.verticalLayout_50.addWidget(self.Rbtn_mc24_close)


        self.horizontalLayout_40.addLayout(self.verticalLayout_50)


        self.gridLayout_6.addWidget(self.frame_24, 2, 3, 1, 1)

        self.frame_19 = QFrame(self.manual_control_page2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Box)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_19.setLineWidth(0)
        self.frame_19.setMidLineWidth(2)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_23 = QLabel(self.frame_19)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_23)

        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.Rbtn_mc19_open = QRadioButton(self.frame_19)
        self.Rbtn_mc19_open.setObjectName(u"Rbtn_mc19_open")
        self.Rbtn_mc19_open.setStyleSheet(u"")

        self.verticalLayout_45.addWidget(self.Rbtn_mc19_open)

        self.Rbtn_mc19_close = QRadioButton(self.frame_19)
        self.Rbtn_mc19_close.setObjectName(u"Rbtn_mc19_close")
        self.Rbtn_mc19_close.setStyleSheet(u"")

        self.verticalLayout_45.addWidget(self.Rbtn_mc19_close)


        self.horizontalLayout_35.addLayout(self.verticalLayout_45)


        self.gridLayout_6.addWidget(self.frame_19, 1, 2, 1, 1)

        self.frame_21 = QFrame(self.manual_control_page2)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Box)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.frame_21.setLineWidth(0)
        self.frame_21.setMidLineWidth(2)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_25 = QLabel(self.frame_21)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_25)

        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.Rbtn_mc22_open = QRadioButton(self.frame_21)
        self.Rbtn_mc22_open.setObjectName(u"Rbtn_mc22_open")
        self.Rbtn_mc22_open.setStyleSheet(u"")

        self.verticalLayout_47.addWidget(self.Rbtn_mc22_open)

        self.Rbtn_mc22_close = QRadioButton(self.frame_21)
        self.Rbtn_mc22_close.setObjectName(u"Rbtn_mc22_close")
        self.Rbtn_mc22_close.setStyleSheet(u"")

        self.verticalLayout_47.addWidget(self.Rbtn_mc22_close)


        self.horizontalLayout_37.addLayout(self.verticalLayout_47)


        self.gridLayout_6.addWidget(self.frame_21, 2, 1, 1, 1)

        self.frame_16 = QFrame(self.manual_control_page2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Box)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_16.setLineWidth(0)
        self.frame_16.setMidLineWidth(2)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_20 = QLabel(self.frame_16)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_20)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.Rbtn_mc16_open = QRadioButton(self.frame_16)
        self.Rbtn_mc16_open.setObjectName(u"Rbtn_mc16_open")
        self.Rbtn_mc16_open.setStyleSheet(u"")

        self.verticalLayout_42.addWidget(self.Rbtn_mc16_open)

        self.Rbtn_mc16_close = QRadioButton(self.frame_16)
        self.Rbtn_mc16_close.setObjectName(u"Rbtn_mc16_close")
        self.Rbtn_mc16_close.setStyleSheet(u"")

        self.verticalLayout_42.addWidget(self.Rbtn_mc16_close)


        self.horizontalLayout_32.addLayout(self.verticalLayout_42)


        self.gridLayout_6.addWidget(self.frame_16, 0, 3, 1, 1)

        self.frame_22 = QFrame(self.manual_control_page2)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Box)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.frame_22.setLineWidth(0)
        self.frame_22.setMidLineWidth(2)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_26 = QLabel(self.frame_22)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_26)

        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.Rbtn_mc23_open = QRadioButton(self.frame_22)
        self.Rbtn_mc23_open.setObjectName(u"Rbtn_mc23_open")
        self.Rbtn_mc23_open.setStyleSheet(u"")

        self.verticalLayout_48.addWidget(self.Rbtn_mc23_open)

        self.Rbtn_mc23_close = QRadioButton(self.frame_22)
        self.Rbtn_mc23_close.setObjectName(u"Rbtn_mc23_close")
        self.Rbtn_mc23_close.setStyleSheet(u"")

        self.verticalLayout_48.addWidget(self.Rbtn_mc23_close)


        self.horizontalLayout_38.addLayout(self.verticalLayout_48)


        self.gridLayout_6.addWidget(self.frame_22, 2, 2, 1, 1)

        self.frame_20 = QFrame(self.manual_control_page2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Box)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.frame_20.setLineWidth(0)
        self.frame_20.setMidLineWidth(2)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_24 = QLabel(self.frame_20)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_24)

        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.Rbtn_mc21_open = QRadioButton(self.frame_20)
        self.Rbtn_mc21_open.setObjectName(u"Rbtn_mc21_open")
        self.Rbtn_mc21_open.setStyleSheet(u"")

        self.verticalLayout_46.addWidget(self.Rbtn_mc21_open)

        self.Rbtn_mc21_close = QRadioButton(self.frame_20)
        self.Rbtn_mc21_close.setObjectName(u"Rbtn_mc21_close")
        self.Rbtn_mc21_close.setStyleSheet(u"")

        self.verticalLayout_46.addWidget(self.Rbtn_mc21_close)


        self.horizontalLayout_36.addLayout(self.verticalLayout_46)


        self.gridLayout_6.addWidget(self.frame_20, 2, 0, 1, 1)

        self.frame_15 = QFrame(self.manual_control_page2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Box)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.frame_15.setLineWidth(0)
        self.frame_15.setMidLineWidth(2)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_15)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_19)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.Rbtn_mc15_open = QRadioButton(self.frame_15)
        self.Rbtn_mc15_open.setObjectName(u"Rbtn_mc15_open")
        self.Rbtn_mc15_open.setStyleSheet(u"")

        self.verticalLayout_41.addWidget(self.Rbtn_mc15_open)

        self.Rbtn_mc15_close = QRadioButton(self.frame_15)
        self.Rbtn_mc15_close.setObjectName(u"Rbtn_mc15_close")
        self.Rbtn_mc15_close.setStyleSheet(u"")

        self.verticalLayout_41.addWidget(self.Rbtn_mc15_close)


        self.horizontalLayout_31.addLayout(self.verticalLayout_41)


        self.gridLayout_6.addWidget(self.frame_15, 0, 2, 1, 1)

        self.frame_6 = QFrame(self.manual_control_page2)
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
        self.Rbtn_mc13_open = QRadioButton(self.frame_6)
        self.Rbtn_mc13_open.setObjectName(u"Rbtn_mc13_open")
        self.Rbtn_mc13_open.setStyleSheet(u"")

        self.verticalLayout_32.addWidget(self.Rbtn_mc13_open)

        self.Rbtn_mc13_close = QRadioButton(self.frame_6)
        self.Rbtn_mc13_close.setObjectName(u"Rbtn_mc13_close")
        self.Rbtn_mc13_close.setStyleSheet(u"")

        self.verticalLayout_32.addWidget(self.Rbtn_mc13_close)


        self.horizontalLayout_22.addLayout(self.verticalLayout_32)


        self.gridLayout_6.addWidget(self.frame_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.manual_control_page2)
        self.cloud_page1 = QWidget()
        self.cloud_page1.setObjectName(u"cloud_page1")
        self.cloud_page1.setStyleSheet(u"")
        self.gridLayout_7 = QGridLayout(self.cloud_page1)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_c1 = QFrame(self.cloud_page1)
        self.frame_c1.setObjectName(u"frame_c1")
        self.frame_c1.setMaximumSize(QSize(16777215, 60))
        self.frame_c1.setFrameShape(QFrame.StyledPanel)
        self.frame_c1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_c1)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_get_data_12hours = QPushButton(self.frame_c1)
        self.btn_get_data_12hours.setObjectName(u"btn_get_data_12hours")
        self.btn_get_data_12hours.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_11.addWidget(self.btn_get_data_12hours)

        self.label_time = QLabel(self.frame_c1)
        self.label_time.setObjectName(u"label_time")

        self.horizontalLayout_11.addWidget(self.label_time)

        self.Btn_open_cloud_web = QPushButton(self.frame_c1)
        self.Btn_open_cloud_web.setObjectName(u"Btn_open_cloud_web")
        self.Btn_open_cloud_web.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_11.addWidget(self.Btn_open_cloud_web)


        self.gridLayout_7.addWidget(self.frame_c1, 0, 0, 1, 1)

        self.frame_c2 = QFrame(self.cloud_page1)
        self.frame_c2.setObjectName(u"frame_c2")
        self.horizontalLayout_7 = QHBoxLayout(self.frame_c2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.image_1 = QLabel(self.frame_c2)
        self.image_1.setObjectName(u"image_1")

        self.horizontalLayout_7.addWidget(self.image_1)

        self.image_2 = QLabel(self.frame_c2)
        self.image_2.setObjectName(u"image_2")

        self.horizontalLayout_7.addWidget(self.image_2)

        self.image_3 = QLabel(self.frame_c2)
        self.image_3.setObjectName(u"image_3")

        self.horizontalLayout_7.addWidget(self.image_3)


        self.gridLayout_7.addWidget(self.frame_c2, 1, 0, 1, 1)

        self.frame_c3 = QFrame(self.cloud_page1)
        self.frame_c3.setObjectName(u"frame_c3")
        self.horizontalLayout_6 = QHBoxLayout(self.frame_c3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.text_humidness = QLineEdit(self.frame_c3)
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

        self.horizontalLayout_6.addWidget(self.text_humidness)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.text_temperature = QLineEdit(self.frame_c3)
        self.text_temperature.setObjectName(u"text_temperature")
        self.text_temperature.setStyleSheet(u"")
        self.text_temperature.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.text_temperature)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.text_illumination = QLineEdit(self.frame_c3)
        self.text_illumination.setObjectName(u"text_illumination")
        self.text_illumination.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.text_illumination)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.gridLayout_7.addWidget(self.frame_c3, 2, 0, 1, 1)

        self.frame_c4 = QFrame(self.cloud_page1)
        self.frame_c4.setObjectName(u"frame_c4")
        self.horizontalLayout_8 = QHBoxLayout(self.frame_c4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.image_4 = QLabel(self.frame_c4)
        self.image_4.setObjectName(u"image_4")

        self.horizontalLayout_8.addWidget(self.image_4)

        self.image_5 = QLabel(self.frame_c4)
        self.image_5.setObjectName(u"image_5")
        self.image_5.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_8.addWidget(self.image_5)

        self.image_6 = QLabel(self.frame_c4)
        self.image_6.setObjectName(u"image_6")

        self.horizontalLayout_8.addWidget(self.image_6)


        self.gridLayout_7.addWidget(self.frame_c4, 3, 0, 1, 1)

        self.frame_c5 = QFrame(self.cloud_page1)
        self.frame_c5.setObjectName(u"frame_c5")
        self.horizontalLayout_10 = QHBoxLayout(self.frame_c5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.lineEdit_3 = QLineEdit(self.frame_c5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lineEdit_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.lineEdit_4 = QLineEdit(self.frame_c5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lineEdit_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.lineEdit_2 = QLineEdit(self.frame_c5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lineEdit_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)


        self.gridLayout_7.addWidget(self.frame_c5, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.cloud_page1)
        self.cloud_page2 = QWidget()
        self.cloud_page2.setObjectName(u"cloud_page2")
        self.gridLayout_2 = QGridLayout(self.cloud_page2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gg = QFrame(self.cloud_page2)
        self.gg.setObjectName(u"gg")
        self.verticalLayout_20 = QVBoxLayout(self.gg)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame2_c1 = QFrame(self.gg)
        self.frame2_c1.setObjectName(u"frame2_c1")
        self.horizontalLayout_42 = QHBoxLayout(self.frame2_c1)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.image_7 = QLabel(self.frame2_c1)
        self.image_7.setObjectName(u"image_7")

        self.horizontalLayout_42.addWidget(self.image_7)

        self.image_8 = QLabel(self.frame2_c1)
        self.image_8.setObjectName(u"image_8")

        self.horizontalLayout_42.addWidget(self.image_8)


        self.verticalLayout_20.addWidget(self.frame2_c1)

        self.frame2_c2 = QFrame(self.gg)
        self.frame2_c2.setObjectName(u"frame2_c2")
        self.horizontalLayout_43 = QHBoxLayout(self.frame2_c2)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.text_humidness_3 = QLineEdit(self.frame2_c2)
        self.text_humidness_3.setObjectName(u"text_humidness_3")
        self.text_humidness_3.setMinimumSize(QSize(60, 0))
        self.text_humidness_3.setMaximumSize(QSize(160, 16777215))
        self.text_humidness_3.setFont(font5)
        self.text_humidness_3.setLayoutDirection(Qt.LeftToRight)
        self.text_humidness_3.setStyleSheet(u"")
        self.text_humidness_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.text_humidness_3)

        self.text_humidness_2 = QLineEdit(self.frame2_c2)
        self.text_humidness_2.setObjectName(u"text_humidness_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.text_humidness_2.sizePolicy().hasHeightForWidth())
        self.text_humidness_2.setSizePolicy(sizePolicy7)
        self.text_humidness_2.setMinimumSize(QSize(60, 32))
        self.text_humidness_2.setMaximumSize(QSize(160, 32))
        self.text_humidness_2.setFont(font5)
        self.text_humidness_2.setLayoutDirection(Qt.LeftToRight)
        self.text_humidness_2.setStyleSheet(u"")
        self.text_humidness_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.text_humidness_2)


        self.verticalLayout_20.addWidget(self.frame2_c2)

        self.frame2_c3 = QFrame(self.gg)
        self.frame2_c3.setObjectName(u"frame2_c3")
        self.horizontalLayout_44 = QHBoxLayout(self.frame2_c3)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.image_9 = QLabel(self.frame2_c3)
        self.image_9.setObjectName(u"image_9")

        self.horizontalLayout_44.addWidget(self.image_9)

        self.image_10 = QLabel(self.frame2_c3)
        self.image_10.setObjectName(u"image_10")
        self.image_10.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_44.addWidget(self.image_10)


        self.verticalLayout_20.addWidget(self.frame2_c3)

        self.frame2_c4_2 = QFrame(self.gg)
        self.frame2_c4_2.setObjectName(u"frame2_c4_2")
        self.frame2_c4 = QHBoxLayout(self.frame2_c4_2)
        self.frame2_c4.setObjectName(u"frame2_c4")
        self.text_humidness_5 = QLineEdit(self.frame2_c4_2)
        self.text_humidness_5.setObjectName(u"text_humidness_5")
        self.text_humidness_5.setMaximumSize(QSize(160, 16777215))
        self.text_humidness_5.setFont(font5)
        self.text_humidness_5.setLayoutDirection(Qt.LeftToRight)
        self.text_humidness_5.setStyleSheet(u"")
        self.text_humidness_5.setAlignment(Qt.AlignCenter)

        self.frame2_c4.addWidget(self.text_humidness_5)

        self.text_humidness_4 = QLineEdit(self.frame2_c4_2)
        self.text_humidness_4.setObjectName(u"text_humidness_4")
        self.text_humidness_4.setMaximumSize(QSize(160, 16777215))
        self.text_humidness_4.setFont(font5)
        self.text_humidness_4.setLayoutDirection(Qt.LeftToRight)
        self.text_humidness_4.setStyleSheet(u"")
        self.text_humidness_4.setAlignment(Qt.AlignCenter)

        self.frame2_c4.addWidget(self.text_humidness_4)


        self.verticalLayout_20.addWidget(self.frame2_c4_2)


        self.gridLayout_2.addWidget(self.gg, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.cloud_page2)
        self.information_page = QWidget()
        self.information_page.setObjectName(u"information_page")
        self.verticalLayout_9 = QVBoxLayout(self.information_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.textBrowser = QTextBrowser(self.information_page)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(0, 0))
        self.textBrowser.setInputMethodHints(Qt.ImhNone)

        self.verticalLayout_9.addWidget(self.textBrowser)

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
        self.themeSettingsTopDetail.setMinimumSize(QSize(41, 8))
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
        sizePolicy1.setHeightForWidth(self.btn_change_topic.sizePolicy().hasHeightForWidth())
        self.btn_change_topic.setSizePolicy(sizePolicy1)
        self.btn_change_topic.setMinimumSize(QSize(0, 45))
        self.btn_change_topic.setFont(font2)
        self.btn_change_topic.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_change_topic.setLayoutDirection(Qt.LeftToRight)
        self.btn_change_topic.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-moon.png);")

        self.verticalLayout_14.addWidget(self.btn_change_topic)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy1.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy1)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font2)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy1.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy1)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font2)
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
        self.creditsLabel.setMaximumSize(QSize(16777215, 20))
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


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_16.addWidget(self.contentBottom)


        self.gridLayout_9.addWidget(self.contentBox, 0, 1, 1, 1)

        self.leftMenuBg.raise_()
        self.contentBox.raise_()
        self.extraLeftBox.raise_()

        self.verticalLayout_19.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"\u5185\u8499\u53e4\u5de5\u4e1a\u5927\u5b66", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"\u80fd\u6e90\u4e0e\u52a8\u529b\u5de5\u7a0b\u5b66\u9662", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf", None))
        self.btn_cloud1.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u7aef\u6e29\u6e7f\u5ea6\u6570\u636e", None))
        self.btn_cloud2.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u7aef\u6c14\u8c61\u7ad9\u6570\u636e", None))
        self.btn_manual_control1.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52a8\u8fdc\u7a0b\u63a7\u52361", None))
        self.btn_manual_control2.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52a8\u8fdc\u7a0b\u63a7\u52362", None))
        self.btn_auto_control.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u63a7\u5236", None))
        self.btn_energy.setText(QCoreApplication.translate("MainWindow", u"\u80fd\u91cf\u6536\u652f", None))
        self.btn_information.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u8f6f\u4ef6", None))
        self.label_3.setText("")
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"\u8f6f\u4ef6\u4ecb\u7ecd", None))
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4ea7\u751f\u7535\u80fd\u603b\u91cf\uff1aXXXXX                        ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"   \u6d88\u8017\u7535\u80fd\u603b\u91cf\uff1a XXXX", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"\u5ea6", None))
        self.lineEdit_10.setText(QCoreApplication.translate("MainWindow", u"CO2\u6d53\u5ea6\uff1a", None))
        self.lineEdit_13.setText(QCoreApplication.translate("MainWindow", u"umol/m2s    (PPFD)", None))
#if QT_CONFIG(accessibility)
        self.lineEdit_8.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(accessibility)
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"\u571f\u58e4\u6e7f\u5ea6\uff1a", None))
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u"ppm", None))
        self.btn_auto_control_2.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u63a7\u5236", None))
        self.lineEdit_9.setText(QCoreApplication.translate("MainWindow", u"% ", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u73af\u5883\u503c\u8bbe\u7f6e\uff1a", None))
        self.lineEdit_12.setText(QCoreApplication.translate("MainWindow", u"\u5149\u7167\u5f3a\u5ea6\uff1a", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"\u7efc\u5408\u6e29\u5ea6\u503c\uff1a", None))
        self.lineEdit_14.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6\u73af\u5883\u6570\u636e\uff1a", None))
        self.btn_open_control_file.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6587\u4ef6\u8def\u5f84", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"\u63a7\u5236\u6570\u636e\u6587\u4ef6\u6a21\u677f\u89c1\u8bf4\u660e\u4e66", None))
        self.lineEdit_15.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6\u73af\u5883\u6570\u636e\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5377\u819c\u673a", None))
        self.Rbtn_mc2_up.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u5377", None))
        self.Rbtn_mc2_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.Rbtn_mc2_down.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u653e", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5faa\u73af\u6c34\u4e0e\u7a7a\u6c14\n"
"\u6362\u70ed\u6cf5", None))
        self.Rbtn_mc11_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.RB_close_shuibeng.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8865\u5149\u706f1", None))
        self.Rbtn_mc3_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.RB_close_buguang.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u5faa\u73af\u6c34\u4e0e\n"
"\u4e59\u4e8c\u9187\u6362\n"
"\u70ed\u6cf5(\u5907\u7528)", None))
        self.Rbtn_mc10_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.RB_close_jire_4.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u5faa\u73af\u6c34\u4e0e\u7a7a\u6c14\n"
"\u6362\u70ed\u6cf5", None))
        self.Rbtn_mc12_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.RB_close_shuibeng_2.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u95e8\u5385\u706f", None))
        self.Rbtn_mc6_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.RB_close_jiare.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u5faa\u73af\u6c34\u4e0e\n"
"\u4e59\u4e8c\u9187\u6362\n"
"\u70ed\u6cf5", None))
        self.Rbtn_mc9_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.RB_close_jire_3.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u5faa\u73af\u4e59\n"
"\u4e8c\u9187\u6cf5\n"
"\uff08\u5907\u7528\uff09", None))
        self.Rbtn_mc8_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.RB_close_jire_2.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7167\u660e\u706f", None))
        self.Rbtn_mc5_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.RB_close_zhaoming.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u8865\u5149\u706f2", None))
        self.Rbtn_mc4_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.RB_close_buguang_2.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5faa\u73af\u4e59\n"
"\u4e8c\u9187\u6cf5", None))
        self.Rbtn_mc7_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.RB_close_jire.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5377\u5e18\u673a", None))
        self.Rbtn_mc1_up.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u5377", None))
        self.Rbtn_mc1_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.Rbtn_mc1_down.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u653e", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u70ed\u68d22", None))
        self.Rbtn_mc14_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.Rbtn_mc14_close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u6392\u98ce\u673a4", None))
        self.Rbtn_mc20_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.Rbtn_mc20_close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u6392\u98ce\u673a1", None))
        self.Rbtn_mc17_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.Rbtn_mc17_close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u6392\u98ce\u673a2", None))
        self.Rbtn_mc18_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.Rbtn_mc18_close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u6c14\u8c61\u7ad9\n"
"\u7535\u6e90", None))
        self.Rbtn_mc24_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.Rbtn_mc24_close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u6392\u98ce\u673a3", None))
        self.Rbtn_mc19_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.Rbtn_mc19_close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u80a5\u4e00\u4f53\u673a\n"
"\u7535\u78c1\u9600\u95e8", None))
        self.Rbtn_mc22_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.Rbtn_mc22_close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u63a7\u5236\u56de\u8def\n"
"\u7535\u6e90", None))
        self.Rbtn_mc16_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.Rbtn_mc16_close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u5ba4\u5185\u76d1\u6d4b\n"
"\u7535\u6e90", None))
        self.Rbtn_mc23_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.Rbtn_mc23_close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u80a5\u4e00\u4f53\u673a\n"
"\u6cf5", None))
        self.Rbtn_mc21_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.Rbtn_mc21_close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u70ed\u68d23", None))
        self.Rbtn_mc15_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.Rbtn_mc15_close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u70ed\u68d21", None))
        self.Rbtn_mc13_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.Rbtn_mc13_close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.btn_get_data_12hours.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u83b7\u53d612\u5c0f\u65f6\u73af\u5883\u6570\u636e", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u65f6\u95f4\uff1a", None))
        self.Btn_open_cloud_web.setText(QCoreApplication.translate("MainWindow", u"\u767b\u9646\u4e91\u5e73\u53f0\u67e5\u770b\u8be6\u7ec6\u4fe1\u606f", None))
        self.image_1.setText(QCoreApplication.translate("MainWindow", u"image_1", None))
        self.image_2.setText(QCoreApplication.translate("MainWindow", u"image_2", None))
        self.image_3.setText(QCoreApplication.translate("MainWindow", u"image_3", None))
        self.text_humidness.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u6c14\u6e7f\u5ea6", None))
        self.text_temperature.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u6c14\u6e29\u5ea6", None))
        self.text_illumination.setText(QCoreApplication.translate("MainWindow", u"\u5149\u7167\u5f3a\u5ea6", None))
        self.image_4.setText(QCoreApplication.translate("MainWindow", u"image_4", None))
        self.image_5.setText(QCoreApplication.translate("MainWindow", u"image_5", None))
        self.image_6.setText(QCoreApplication.translate("MainWindow", u"image_6", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"\u571f\u58e4\u6e29\u5ea6", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"\u571f\u58e4\u6e7f\u5ea6", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"\u4e8c\u6c27\u5316\u78b3\u6d53\u5ea6", None))
        self.image_7.setText(QCoreApplication.translate("MainWindow", u"image_7", None))
        self.image_8.setText(QCoreApplication.translate("MainWindow", u"image_8", None))
        self.text_humidness_3.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u6c14\u6e7f\u5ea6", None))
        self.text_humidness_2.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u6c14\u6e29\u5ea6", None))
        self.image_9.setText(QCoreApplication.translate("MainWindow", u"image_9", None))
        self.image_10.setText(QCoreApplication.translate("MainWindow", u"image_10", None))
        self.text_humidness_5.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u6c14\u6e29\u5ea6", None))
        self.text_humidness_4.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u6c14\u6e7f\u5ea6", None))
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

