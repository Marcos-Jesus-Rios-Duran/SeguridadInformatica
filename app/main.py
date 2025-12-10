"""
Módulo Principal del Sistema de Encriptación
============================================

Este es el punto de entrada principal de la aplicación. Contiene la clase
LoginWindow que gestiona la autenticación de usuarios y la lógica de inicio
de sesión del sistema.

Autor: Marcos Jesús Ríos Durán
Fecha: 07/12/2025
Versión: 1.0.0

Dependencias:
    - PyQt6.QtWidgets: Componentes de interfaz gráfica
    - login.Ui_MainWindow: Interfaz de usuario generada para login
    - homePage.menuLogic.MenuWindow: Ventana del menú principal (Carga Perezosa)
"""

# ============================================================================
# IMPORTACIONES
# ============================================================================

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QPushButton
from login import Ui_MainWindow

# --- CAMBIO IMPORTANTE: ---
# Quitamos el import de MenuWindow de aquí arriba para que el programa arranque rápido.
# Antes estaba: from homePage.menu import MenuWindow 
# --------------------------


# ============================================================================
# CLASE PRINCIPAL - LOGIN WINDOW
# ============================================================================

class LoginWindow(QMainWindow):
    """
    Clase que gestiona la lógica de negocio de la ventana de inicio de sesión.
    """
    
    def __init__(self):
        super().__init__()
        
        # ====================================================================
        # CONFIGURACIÓN DE LA INTERFAZ DE USUARIO
        # ====================================================================
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Configuración del campo de contraseña
        self.ui.lvlpassword.setEchoMode(QLineEdit.EchoMode.Password)
        
        # ====================================================================
        # BOTÓN PARA MOSTRAR/OCULTAR CONTRASEÑA
        # ====================================================================
        self.btn_toggle_password = QPushButton(self.ui.centralwidget)
        self.btn_toggle_password.setGeometry(420, 138, 25, 25)
        self.btn_toggle_password.setText("👁")
        self.btn_toggle_password.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 0.05);
                border-radius: 3px;
            }
        """)
        
        self.btn_toggle_password.clicked.connect(self.toggle_password)
        self.password_visible = False
        
        # ====================================================================
        # CONEXIÓN DE SEÑALES Y SLOTS
        # ====================================================================
        self.ui.lvlacept.clicked.connect(self.aceptar_login)
        # Soporte para tecla Enter
        self.ui.lvlpassword.returnPressed.connect(self.aceptar_login)
        self.ui.lvlcancel.clicked.connect(self.close)
    
    # ========================================================================
    # MÉTODOS DE VALIDACIÓN
    # ========================================================================
    
    def validar_campos(self):
        usuario = self.ui.lvluser.text().strip()
        password = self.ui.lvlpassword.text()
        
        if not usuario and not password:
            QMessageBox.warning(self, "Error", "Por favor complete todos los campos")
            return False
        
        if not usuario:
            QMessageBox.warning(self, "Error", "Por favor ingrese un usuario")
            return False
        
        if not password:
            QMessageBox.warning(self, "Error", "Por favor ingrese una contraseña")
            return False
            
        return True
    
    # ========================================================================
    # MÉTODOS DE AUTENTICACIÓN
    # ========================================================================
    
    def aceptar_login(self):
        if not self.validar_campos():
            return
        
        usuario = self.ui.lvluser.text().strip()
        password = self.ui.lvlpassword.text()
        
        if (usuario == "admin" or usuario == "Marcos") and password == "mrco":
            QMessageBox.information(
                self, 
                "Éxito", 
                f"¡Bienvenido {usuario}!\n\nAcceso concedido al sistema."
            )
            self.abrir_menu()
        else:
            QMessageBox.critical(
                self, 
                "Error de Autenticación", 
                "Usuario o contraseña incorrectos.\n\nPor favor, intente nuevamente."
            )
            self.ui.lvlpassword.clear()
            self.ui.lvlpassword.setFocus()
    
    # ========================================================================
    # MÉTODOS DE NAVEGACIÓN
    # ========================================================================
    
    def abrir_menu(self):
        """
        Abre la ventana del menú principal.
        IMPLEMENTACIÓN DE LAZY LOADING
        """
        # ====================================================================
        # LAZY LOADING (CARGA PEREZOSA)
        # ====================================================================
        from homePage.menu import MenuWindow
        
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.close()
    
    # ========================================================================
    # MÉTODOS DE INTERACCIÓN
    # ========================================================================
    
    def toggle_password(self):
        if self.password_visible:
            self.ui.lvlpassword.setEchoMode(QLineEdit.EchoMode.Password)
            self.btn_toggle_password.setText("👁")
            self.password_visible = False
        else:
            self.ui.lvlpassword.setEchoMode(QLineEdit.EchoMode.Normal)
            self.btn_toggle_password.setText("👁‍🗨")
            self.password_visible = True


# ============================================================================
# PUNTO DE ENTRADA DE LA APLICACIÓN
# ============================================================================

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())