import sys 
from frnMenu import menu as MenuUI  # Renombramos para evitar conflicto
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QPushButton

class MenuWindow(QMainWindow):  # Clase ventana del menú
    def __init__(self):
        super().__init__()
        # Crear la interfaz del menú
        self.ui = MenuUI()
        # Configurar la UI en esta ventana
        self.ui.setupUi(self)