"""
Ventana de Encriptación con MenuBar Reutilizable
================================================

Este módulo contiene la clase EncriptarWindow que implementa la lógica
de la ventana de encriptación usando el MenuBarComponent reutilizable.

Autor: Marcos Jesús Ríos Durán
Fecha: 07/12/2025
Versión: 1.0.0
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from encriptacion.frnEncriptar import Ui_MainWindow
from app.common.MenuBarComponent import MenuBarComponent

class EncriptarWindow(QMainWindow):
    """
    Clase que gestiona la ventana de encriptación de mensajes.
    
    Esta clase utiliza el MenuBarComponent para mantener consistencia
    en la navegación del sistema.
    
    Attributes:
        ui (Ui_MainWindow): Interfaz de usuario generada
        menubar_component (MenuBarComponent): Componente del navbar
    """
    
    def __init__(self):
        """
        Constructor de la clase EncriptarWindow.
        
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
        self.ui.btnEncriptar.clicked.connect(self.encriptar_mensaje)
        self.ui.btnDescargar.clicked.connect(self.descargar_archivo)
        self.ui.btnEnviar.clicked.connect(self.enviar_mensaje)
        self.ui.btnRegresar.clicked.connect(self.regresar_menu)
    
    # ========================================================================
    # MÉTODOS DE LA VENTANA
    # ========================================================================
    
    def encriptar_mensaje(self):
        """Encripta el mensaje ingresado."""
        # TODO: Implementar lógica de encriptación
        print("Encriptando mensaje...")
        mensaje = self.ui.txtMensaje.toPlainText()
        print(f"Mensaje: {mensaje}")
    
    def descargar_archivo(self):
        """Descarga el mensaje encriptado."""
        # TODO: Implementar lógica de descarga
        print("Descargando archivo...")
    
    def enviar_mensaje(self):
        """Envía el mensaje encriptado."""
        # TODO: Implementar lógica de envío
        print("Enviando mensaje...")
    
    def regresar_menu(self):
        """Regresa al menú principal."""
        from app.homePage.menu import MenuWindow
        
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EncriptarWindow()
    window.show()
    sys.exit(app.exec())