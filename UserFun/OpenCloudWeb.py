
from PySide6.QtCore import Signal
from PySide6.QtCore.QThread import QThread

class OpenCloudWeb(QThread) :
    webSignal = Signal(str)

    def __init__(self):
        super.__init__()


