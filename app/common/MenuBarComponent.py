"""
Componente Lógico del MenuBar Compartido
========================================
Ubicación: app/common/MenuBarComponent.py
"""
from PyQt6.QtWidgets import QMessageBox
from common.frnMenuBar import Ui_MenuBar 

class MenuBarComponent:
    def __init__(self, main_window):
        self.main_window = main_window
        self.ui = Ui_MenuBar()

    def setup_menubar(self):
        self.ui.setupUi(self.main_window)
        
        # Conexiones
        self.ui.actionIrEncriptar.triggered.connect(self.ir_a_encriptar)
        self.ui.actionIrDesencriptar.triggered.connect(self.ir_a_desencriptar)
        self.ui.actionAcercaDe.triggered.connect(self.mostrar_ayuda)
        self.ui.actionCerrarSesion.triggered.connect(self.cerrar_sesion)

        return self.ui.menubar

    # =======================================================
    # LÓGICA DE NAVEGACIÓN
    # =======================================================
    
    def ir_a_encriptar(self):
        from encriptacion.controller.encriptarLogic import EncriptarLogic
        if isinstance(self.main_window, EncriptarLogic):
            return

        self.ventana = EncriptarLogic()
        self.ventana.show()
        self.main_window.close()

    def ir_a_desencriptar(self):
        from desencriptacion.controller.desencriptarLogic import DesencriptarLogic
        
        if isinstance(self.main_window, DesencriptarLogic):
            return

        self.ventana = DesencriptarLogic()
        self.ventana.show()
        self.main_window.close()

    def mostrar_ayuda(self):
        QMessageBox.information(
            self.main_window,
            "Acerca de",
            "Sistema de Seguridad Informática v1.0\nCreated by Marcos Ríos"
        )

    def cerrar_sesion(self):
        respuesta = QMessageBox.question(
            self.main_window,
            "Salir",
            "¿Deseas cerrar sesión?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if respuesta == QMessageBox.StandardButton.Yes:
            # CORREGIDO: Importamos directo desde main (sin app.)
            from main import LoginWindow
            self.login = LoginWindow()
            self.login.show()
            self.main_window.close()