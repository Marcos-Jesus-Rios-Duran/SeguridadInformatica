"""
Componente Lógico del MenuBar Compartido (Sleek Cyber Style)
============================================================
Ubicación: app/common/MenuBarComponent.py

Navbar reutilizable con estilo oscuro y efectos hover modernos.
"""
from PyQt6.QtWidgets import QMessageBox
from common.frnMenuBar import Ui_MenuBar 

class MenuBarComponent:
    def __init__(self, main_window):
        self.main_window = main_window
        self.ui = Ui_MenuBar()

    def setup_menubar(self):
        self.ui.setupUi(self.main_window)
        
        # =======================================================
        # ESTILO CYBER PARA EL NAVBAR
        # =======================================================
        # Aplicamos el estilo oscuro y los efectos hover aquí mismo
        # para que se replique en todas las ventanas.
        self.ui.menubar.setStyleSheet("""
            QMenuBar {
                background-color: #1E293B; /* Fondo oscuro */
                color: #E2E8F0; /* Texto claro */
                border-bottom: 2px solid #10B981; /* Línea verde abajo */
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
            }
            QMenuBar::item {
                background-color: transparent;
                padding: 8px 15px;
                border-radius: 5px;
            }
            QMenuBar::item:selected { /* Hover Effect */
                background-color: #10B981; /* Verde Esmeralda al pasar mouse */
                color: white;
            }
            QMenuBar::item:pressed {
                background-color: #059669;
            }
            
            /* Estilo para los menús desplegables */
            QMenu {
                background-color: #0F172A; /* Fondo muy oscuro */
                color: #E2E8F0;
                border: 1px solid #334155;
            }
            QMenu::item {
                padding: 8px 25px;
            }
            QMenu::item:selected {
                background-color: #06B6D4; /* Azul Cian para items */
                color: white;
            }
        """)

        # Conexiones de lógica
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
            "Sistema de Seguridad Informática\nCreated by Antonio Ocpaco"
        )

    def cerrar_sesion(self):
        respuesta = QMessageBox.question(
            self.main_window,
            "Salir",
            "¿Deseas cerrar sesión?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if respuesta == QMessageBox.StandardButton.Yes:
            from main import LoginWindow
            self.login = LoginWindow()
            self.login.show()
            self.main_window.close()