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

        # ====================================================================
        # NUEVO: AGREGAR BOTÓN "CARGAR" MANUALMENTE
        # ====================================================================
        # Como no está en el .ui, lo creamos aquí mismo.
        # Lo pondremos debajo del botón "Enviar".
        self.ui.btnCargar = QtWidgets.QPushButton(parent=self.ui.centralwidget)
        self.ui.btnCargar.setGeometry(QtCore.QRect(620, 280, 150, 50)) 
        
        # Le damos estilo para que se vea igual a los otros
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ui.btnCargar.setFont(font)
        self.ui.btnCargar.setText("📂 Cargar TXT")
        self.ui.btnCargar.setObjectName("btnCargar")
        
        # ¡Importante! Hay que mostrarlo
        self.ui.btnCargar.show()