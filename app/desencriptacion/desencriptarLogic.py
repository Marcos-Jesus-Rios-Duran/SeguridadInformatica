from PyQt6.QtWidgets import QMainWindow
from desencriptacion.frnDesencriptar import Ui_MainWindow

class DesencriptarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)