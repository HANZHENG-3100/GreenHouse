# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *
from .app_settings import Settings
# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////
class AppFunctions(MainWindow):
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
        self.ui.plainTextEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.tableWidget.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.scrollArea.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.comboBox.setStyleSheet("background-color: #6272a4;")
        self.ui.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")

    def Btn_open_web(self):
        import webbrowser
        webbrowser.open('http://www.0531yun.com/')
        print("Btn_open_web run")

        return

    def clear_computer_info(self):
        # 更改设置的flag
        self.seriesS.clear()
        self.seriesL.clear()
        self.chart.addSeries(self.seriesS)
        self.chart.addSeries(self.seriesL)

    def open_guide_book(self):
        import webbrowser
        webbrowser.open("shuoming" + '.docx')

    def data_display(self, str):
        # 获取已经记录好的数据并展示
        # 设置一个flag
        with open(r'./computer_info.csv', 'r') as f:
            reader = f.readlines()
            reader_last = reader[-1].replace('\n', '').split(',')
            # 横坐标
            col = int(reader_last[0])
            # cpu
            cpu = float(reader_last[1])
            # 内存
            memory = float(reader_last[2])

        self.seriesS.append(col, cpu)
        self.seriesL.append(col, memory)
        self.chart = QChart()  # 创建 Chart
        self.chart.setTitle("device information")
        self.chart.addSeries(self.seriesS)
        self.chart.addSeries(self.seriesL)
        self.chart.createDefaultAxes()
        widgets.graphicsView.setChart(self.chart)
