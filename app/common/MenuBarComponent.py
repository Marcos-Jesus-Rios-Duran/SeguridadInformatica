"""
Componente de Barra de Menú Reutilizable
=========================================

Este módulo contiene la clase MenuBarComponent que implementa un navbar
reutilizable para todas las ventanas del sistema de encriptación.

Autor: Marcos Jesús Ríos Durán
Fecha: 07/12/2025
Versión: 1.0.0
"""

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox


class MenuBarComponent:
    """
    Componente reutilizable de barra de menú (navbar) para el sistema.
    
    Esta clase proporciona un menubar consistente que puede ser agregado
    a cualquier ventana del sistema, manteniendo la misma estructura y
    funcionalidad en todas las pantallas.
    
    Attributes:
        parent_window (QMainWindow): Ventana padre que contiene el menubar
    """
    
    def __init__(self, parent_window):
        """
        Inicializa el componente de menubar.
        
        Args:
            parent_window (QMainWindow): Ventana donde se montará el menubar
        """
        self.parent_window = parent_window
        self.menubar = None
        
    def setup_menubar(self):
        """
        Configura y retorna el menubar completo.
        
        Crea la estructura completa del menubar con todos sus menús
        y acciones, listo para ser agregado a cualquier ventana.
        
        Returns:
            QMenuBar: Barra de menú configurada
        """
        # Crear la barra de menú
        self.menubar = QtWidgets.QMenuBar(parent=self.parent_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        
        # ====================================================================
        # MENÚ ENCRIPTAR
        # ====================================================================
        self.menuEncriptar = QtWidgets.QMenu(parent=self.menubar)
        self.menuEncriptar.setObjectName("menuEncriptar")
        self.menuEncriptar.setTitle("Encriptar")
        
        self.actionCrearDocumento = QtGui.QAction(parent=self.parent_window)
        self.actionCrearDocumento.setObjectName("actionCrearDocumento")
        self.actionCrearDocumento.setText("Crear Documento")
        self.actionCrearDocumento.triggered.connect(self.abrir_encriptar)
        
        self.menuEncriptar.addAction(self.actionCrearDocumento)
        
        # ====================================================================
        # MENÚ DESENCRIPTAR
        # ====================================================================
        self.menuDesencriptar = QtWidgets.QMenu(parent=self.menubar)
        self.menuDesencriptar.setObjectName("menuDesencriptar")
        self.menuDesencriptar.setTitle("Desencriptar")
        
        self.actionCargarDocumento = QtGui.QAction(parent=self.parent_window)
        self.actionCargarDocumento.setObjectName("actionCargarDocumento")
        self.actionCargarDocumento.setText("Cargar Documento")
        self.actionCargarDocumento.triggered.connect(self.abrir_desencriptar)
        
        self.menuDesencriptar.addAction(self.actionCargarDocumento)
        
        # ====================================================================
        # MENÚ AYUDA
        # ====================================================================
        self.menuAyuda = QtWidgets.QMenu(parent=self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuAyuda.setTitle("Ayuda")
        
        self.actionAcercaDe = QtGui.QAction(parent=self.parent_window)
        self.actionAcercaDe.setObjectName("actionAcercaDe")
        self.actionAcercaDe.setText("Acerca de")
        self.actionAcercaDe.triggered.connect(self.mostrar_ayuda)
        
        self.menuAyuda.addAction(self.actionAcercaDe)
        
        # ====================================================================
        # MENÚ SALIR
        # ====================================================================
        self.menuSalir = QtWidgets.QMenu(parent=self.menubar)
        self.menuSalir.setObjectName("menuSalir")
        self.menuSalir.setTitle("Salir")
        
        self.actionCerrarSesion = QtGui.QAction(parent=self.parent_window)
        self.actionCerrarSesion.setObjectName("actionCerrarSesion")
        self.actionCerrarSesion.setText("Cerrar Sesión")
        self.actionCerrarSesion.triggered.connect(self.cerrar_sesion)
        
        self.menuSalir.addAction(self.actionCerrarSesion)
        
        # ====================================================================
        # AGREGAR MENÚS A LA BARRA
        # ====================================================================
        self.menubar.addAction(self.menuEncriptar.menuAction())
        self.menubar.addAction(self.menuDesencriptar.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menubar.addAction(self.menuSalir.menuAction())
        
        return self.menubar
    
    # ========================================================================
    # MÉTODOS DE NAVEGACIÓN
    # ========================================================================
    
    def abrir_encriptar(self):
        """Abre la ventana de encriptación."""
        from encriptacion.encriptarLogic import EncriptarWindow
        
        # Cerrar ventana actual si no es la ventana de encriptación
        if not isinstance(self.parent_window, EncriptarWindow):
            self.ventana_encriptar = EncriptarWindow()
            self.ventana_encriptar.show()
            self.parent_window.close()
    
    def abrir_desencriptar(self):
        """Abre la ventana de desencriptación."""
        from desencriptacion.desencriptarLogic import DesencriptarWindow
        
        # Cerrar ventana actual si no es la ventana de desencriptación
        if not isinstance(self.parent_window, DesencriptarWindow):
            self.ventana_desencriptar = DesencriptarWindow()
            self.ventana_desencriptar.show()
            self.parent_window.close()
    
    def mostrar_ayuda(self):
        """Muestra información del sistema."""
        QMessageBox.information(
            self.parent_window,
            "Acerca de",
            "Sistema de Encriptación v1.0.0\n\n"
            "Autor: Marcos Jesús Ríos Durán\n"
            "Fecha: 07/11/2025\n\n"
            "Sistema de encriptación y desencriptación de mensajes."
        )
    
    def cerrar_sesion(self):
        """Cierra la sesión y regresa al login."""
        respuesta = QMessageBox.question(
            self.parent_window,
            "Cerrar Sesión",
            "¿Estás seguro que deseas cerrar la aplicación?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if respuesta == QMessageBox.StandardButton.Yes:
            from main import LoginWindow
            
            self.login_window = LoginWindow()
            self.login_window.show()
            self.parent_window.close()