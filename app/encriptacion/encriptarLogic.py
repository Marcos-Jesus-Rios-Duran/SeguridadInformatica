from PyQt6.QtWidgets import QMainWindow
from encriptacion.frnEncriptar import Ui_MainWindow

class EncriptarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)