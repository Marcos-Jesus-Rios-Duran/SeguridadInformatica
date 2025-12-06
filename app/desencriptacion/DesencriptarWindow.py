"""
Vista Compuesta de Desencriptación
==================================
Archivo: app/desencriptacion/desencriptarWindow.py

Responsabilidad:
    - Unir la UI generada (frnDesencriptar) con el Navbar compartido.
    - NO contiene lógica de negocio, solo configuración visual.
"""

from PyQt6.QtWidgets import QMainWindow
# 1. Importamos la "cara" (formulario generado)
from desencriptacion.frnDesencriptar import Ui_MainWindow
# 2. Importamos la "barra" (menú compartido)
from common.MenuBarComponent import MenuBarComponent

class DesencriptarWindow(QMainWindow):
    """
    Clase que solamente construye la ventana visual completa.
    Fusiona el formulario de desencriptación con el menú superior.
    """
    def __init__(self):
        super().__init__()
        
        # ----------------------------------------------------------------
        # PASO 1: PINTAR EL FORMULARIO (ABAJO)
        # ----------------------------------------------------------------
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # ----------------------------------------------------------------
        # PASO 2: PINTAR EL NAVBAR (ARRIBA)
        # ----------------------------------------------------------------
        # Borramos la barra vacía que trae por defecto
        self.menuBar().setParent(None) 
        
        # Instanciamos el componente del menú
        self.menubar_component = MenuBarComponent(self)
        
        # Lo construimos y lo asignamos
        menubar = self.menubar_component.setup_menubar()
        self.setMenuBar(menubar)