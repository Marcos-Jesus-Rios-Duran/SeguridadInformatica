from PyQt6 import QtWidgets, QtCore, QtGui # Importamos esto para crear el botón manual
from PyQt6.QtWidgets import QMainWindow
from encriptacion.views.frnEncriptar import Ui_MainWindow
from common.MenuBarComponent import MenuBarComponent

class EncriptarWindowUI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 1. Pintar lo básico
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # 2. Navbar
        self.menuBar().setParent(None)
        self.menubar_component = MenuBarComponent(self)
        menubar = self.menubar_component.setup_menubar()
        self.setMenuBar(menubar)