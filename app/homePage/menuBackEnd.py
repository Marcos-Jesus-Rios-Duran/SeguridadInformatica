"""
Ventana del Menú Principal
========================================================

Este módulo contiene la clase MenuWindow que implementa la lógica de negocio
para la ventana del menú principal del sistema, gestionando las opciones de
encriptación, desencriptación y navegación del sistema.

Autor: Marcos Jesús Ríos Durán
Fecha: 07/11/2025
Versión: 1.0.0

Dependencias:
    - PyQt6.QtWidgets: Componentes de interfaz gráfica
    - homePage.frnMenu.menu: Interfaz de usuario generada del menú
    - encriptacion.encriptarLogic: Ventana de encriptación
    - desencriptacion.desencriptarLogic: Ventana de desencriptación
"""

# ============================================================================
# IMPORTACIONES
# ============================================================================

import sys 
from homePage.frnMenu import menu as MenuUI
from encriptacion.encriptarLogic import EncriptarWindow
from desencriptacion.desencriptarLogic import DesencriptarWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox


# ============================================================================
# CLASE PRINCIPAL
# ============================================================================

class MenuWindow(QMainWindow):
    """
    Clase que gestiona la lógica de negocio de la ventana del menú principal.
    
    Esta clase hereda de QMainWindow y proporciona toda la funcionalidad
    del menú principal del sistema, incluyendo gestión de opciones de
    encriptación, desencriptación, ayuda y salida del sistema.
    
    Attributes:
        ui (MenuUI): Instancia de la interfaz de usuario del menú
        ventana_encriptar (EncriptarWindow): Referencia a la ventana de encriptación
        ventana_desencriptar (DesencriptarWindow): Referencia a la ventana de desencriptación
    
    Note:
        Esta ventana se abre después de un inicio de sesión exitoso.
    """
    
    def __init__(self):
        """
        Constructor de la clase MenuWindow.
        
        Inicializa la ventana del menú principal, configura la interfaz de
        usuario y conecta las señales de los elementos del menú con sus
        respectivos manejadores de eventos.
        
        Este método se ejecuta automáticamente al crear una instancia de
        MenuWindow y es responsable de:
            - Inicializar la clase padre QMainWindow
            - Crear la interfaz de usuario del menú
            - Configurar la UI en la ventana actual
            - Conectar señales con slots
            - Configurar eventos de los menús
            
        See Also:
            setupUi(): Método que configura la interfaz gráfica
        """
        # ====================================================================
        # INICIALIZACIÓN DE LA CLASE PADRE
        # ====================================================================
        
        super().__init__()
        
        # ====================================================================
        # CONFIGURACIÓN DE LA INTERFAZ DE USUARIO
        # ====================================================================
        
        self.ui = MenuUI()
        self.ui.setupUi(self)
        
        # ====================================================================
        # INICIALIZACIÓN DE REFERENCIAS A VENTANAS
        # ====================================================================
        
        self.ventana_encriptar = None
        self.ventana_desencriptar = None
        
        # ====================================================================
        # CONEXIÓN DE SEÑALES Y SLOTS
        # ====================================================================
        
        self.ui.Crear_Documento.triggered.connect(self.abrir_encriptar)
        self.ui.ctionCargarDocumento.triggered.connect(self.abrir_desencriptar)
        self.ui.actionAcercaDe.triggered.connect(self.mostrar_ayuda)
        self.ui.actionCerrarSesion.triggered.connect(self.salir_aplicacion)
       
       
    # ========================================================================
    # MÉTODOS DE GESTIÓN DE VENTANAS
    # ========================================================================
    
    def abrir_encriptar(self):
        """
        Abre la ventana de encriptación de mensajes.
        
        Crea una nueva instancia de la ventana de encriptación y la muestra
        al usuario. Esta ventana permite crear y encriptar documentos.
        
        Returns:
            None
            
        Example:
            >>> self.abrir_encriptar()
            
        See Also:
            EncriptarWindow: Clase que implementa la ventana de encriptación
        """
        self.ventana_encriptar = EncriptarWindow()
        self.ventana_encriptar.show()
    
    def abrir_desencriptar(self):
        """
        Abre la ventana de desencriptación de mensajes.
        
        Crea una nueva instancia de la ventana de desencriptación y la muestra
        al usuario. Esta ventana permite cargar y desencriptar documentos.
        
        Returns:
            None
            
        Example:
            >>> self.abrir_desencriptar()
            
        See Also:
            DesencriptarWindow: Clase que implementa la ventana de desencriptación
        """
        self.ventana_desencriptar = DesencriptarWindow()
        self.ventana_desencriptar.show()
    
    def mostrar_ayuda(self):
        """
        Muestra información acerca del sistema.
        
        Despliega un cuadro de diálogo con información sobre la versión
        del sistema, el autor y la fecha de creación.
        
        Returns:
            None
            
        Example:
            >>> self.mostrar_ayuda()
        """
        QMessageBox.information(
            self,
            "Acerca de",
            "Sistema de Encriptación v1.0.0\n\n"
            "Autor: Marcos Jesús Ríos Durán\n"
            "Fecha: 07/11/2025\n\n"
            "Sistema de encriptación y desencriptación de mensajes."
        )
    
    def salir_aplicacion(self):
        """
        Cierra la aplicación de forma segura.
        
        Muestra un cuadro de diálogo de confirmación antes de cerrar la
        aplicación. Si el usuario confirma, cierra la ventana actual.
        
        Returns:
            None
            
        Example:
            >>> self.salir_aplicacion()
        """
        respuesta = QMessageBox.question(
            self,
            "Cerrar Sesión",
            "¿Estás seguro que deseas cerrar la aplicación?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if respuesta == QMessageBox.StandardButton.Yes:
             # Importar LoginWindow aquí para evitar importación circular
             from main import LoginWindow
        
            # Crear nueva ventana de login
             self.login_window = LoginWindow()
             self.login_window.show()
        
             self.close()


# ============================================================================
# PUNTO DE ENTRADA DE LA APLICACIÓN
# ============================================================================

if __name__ == "__main__":
    """
    Punto de entrada principal cuando el módulo se ejecuta directamente.
    
    Crea la aplicación Qt, inicializa la ventana del menú y ejecuta el
    loop principal de eventos del sistema.
    
    Note:
        Normalmente este módulo es llamado desde LoginWindow después de
        una autenticación exitosa, no se ejecuta directamente.
    """
    app = QApplication(sys.argv)
    window = MenuWindow()
    window.show()
    sys.exit(app.exec())