"""
Ventana de Desencriptación con MenuBar Reutilizable
==================================================

Este módulo contiene la clase DesencriptarWindow que implementa la lógica
de la ventana de desencriptación usando el MenuBarComponent reutilizable.

Autor: Marcos Jesús Ríos Durán
Fecha: 07/12/2025
Versión: 1.0.0
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from desencriptacion.frnDesencriptar import Ui_MainWindow
from app.common.MenuBarComponent import MenuBarComponent


class DesencriptarWindow(QMainWindow):
    """
    Clase que gestiona la ventana de desencriptación de mensajes.
    
    Esta clase utiliza el MenuBarComponent para mantener consistencia
    en la navegación del sistema.
    
    Attributes:
        ui (Ui_MainWindow): Interfaz de usuario generada
        menubar_component (MenuBarComponent): Componente del navbar
    """
    
    def __init__(self):
        """
        Constructor de la clase DesencriptarWindow.
        
        Inicializa la ventana, configura la UI y agrega el menubar
        reutilizable.
        """
        super().__init__()
        
        # Configurar la interfaz base
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # ====================================================================
        # AGREGAR MENUBAR REUTILIZABLE
        # ====================================================================
        # Eliminar el menubar generado automáticamente
        self.menuBar().setParent(None)
        
        # Crear y configurar el menubar component
        self.menubar_component = MenuBarComponent(self)
        menubar = self.menubar_component.setup_menubar()
        self.setMenuBar(menubar)
        
        # ====================================================================
        # CONEXIÓN DE SEÑALES LOCALES
        # ====================================================================
        self.ui.btnCargarArchivo.clicked.connect(self.cargar_archivo)
        self.ui.btnDesencriptar.clicked.connect(self.desencriptar_mensaje)
        self.ui.btnDescargar.clicked.connect(self.descargar_archivo)
        self.ui.btnRegresar.clicked.connect(self.regresar_menu)
    
    # ========================================================================
    # MÉTODOS DE LA VENTANA
    # ========================================================================
    
    def cargar_archivo(self):
        """Carga un archivo encriptado."""
        # TODO: Implementar lógica de carga
        print("Cargando archivo...")
    
    def desencriptar_mensaje(self):
        """Desencripta el mensaje cargado."""
        # TODO: Implementar lógica de desencriptación
        print("Desencriptando mensaje...")
        mensaje = self.ui.txtMensajeEncriptado.toPlainText()
        print(f"Mensaje encriptado: {mensaje}")
    
    def descargar_archivo(self):
        """Descarga el mensaje desencriptado."""
        # TODO: Implementar lógica de descarga
        print("Descargando archivo...")
    
    def regresar_menu(self):
        """Regresa al menú principal."""
        from app.homePage.menu import MenuWindow
        
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DesencriptarWindow()
    window.show()
    sys.exit(app.exec())