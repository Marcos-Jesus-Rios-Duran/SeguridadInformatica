"""
Vista Compuesta de Encriptación
===============================
Archivo: app/encriptacion/encriptarWindow.py

Responsabilidad:
    - Unir la UI generada (frnEncriptar) con el Navbar compartido.
    - NO contiene lógica de negocio.
"""

from PyQt6.QtWidgets import QMainWindow
# Importamos la "cara" del formulario
from encriptacion.views.frnEncriptar import Ui_MainWindow
# Importamos la "barra" compartida
from common.MenuBarComponent import MenuBarComponent

class EncriptarWindowUI(QMainWindow):
    """
    Clase que solamente construye la ventana visual.
    Une el formulario con el menú.
    """
    def __init__(self):
        super().__init__()
        
        # 1. Pintar el Formulario (Centro)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # 2. Pintar la Barra de Menú (Arriba)
        self.menuBar().setParent(None) # Borramos la vieja
        
        self.menubar_component = MenuBarComponent(self)
        menubar = self.menubar_component.setup_menubar()
        
        self.setMenuBar(menubar)
        
        # ¡Listo! Aquí no hacemos nada más. Solo pintar.