"""
Módulo Principal del Sistema de Encriptación
============================================

Este es el punto de entrada principal de la aplicación. Contiene la clase
LoginWindow que gestiona la autenticación de usuarios y la lógica de inicio
de sesión del sistema.

Autor: Marcos Jesús Ríos Durán
Fecha: 08/12/2025
Versión: 1.2.0 (Botón Automático)

Dependencias:
    - PyQt6.QtWidgets: Componentes de interfaz gráfica
    - login.Ui_MainWindow: Interfaz de usuario generada para login
"""

# ============================================================================
# IMPORTACIONES
# ============================================================================

import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QMessageBox, 
                             QLineEdit, QPushButton, QHBoxLayout)
from PyQt6.QtCore import Qt
from login import Ui_MainWindow


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
        # BOTÓN "OJITO" AUTOMÁTICO (Integrado en el Input)
        # ====================================================================
        
        # 1. Crear el botón como hijo del campo de contraseña (self.ui.lvlpassword)
        self.btn_toggle_password = QPushButton(self.ui.lvlpassword)
        self.btn_toggle_password.setText("👁")
        self.btn_toggle_password.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_toggle_password.setFixedWidth(30) # Ancho fijo
        
        # Estilo para que parezca un icono flotante limpio
        self.btn_toggle_password.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                font-size: 16px;
                color: #94A3B8; /* Gris suave por defecto */
                padding-bottom: 2px;
            }
            QPushButton:hover {
                color: #22D3EE; /* Cian Neón al pasar el mouse */
            }
        """)
        
        # 2. Layout Horizontal DENTRO del Input
        # Esto es lo que lo acomoda a la derecha automáticamente
        layout_ojo = QHBoxLayout(self.ui.lvlpassword)
        layout_ojo.setContentsMargins(0, 0, 5, 0) # Margen derecho de 5px
        layout_ojo.addStretch() # Empuja el botón hacia el final
        layout_ojo.addWidget(self.btn_toggle_password)
        
        # 3. Margen de Texto del Input
        # Vital para que lo que escribas no se tape con el botón
        self.ui.lvlpassword.setTextMargins(0, 0, 35, 0) 
        
        # Conexión del evento clic
        self.btn_toggle_password.clicked.connect(self.toggle_password)
        self.password_visible = False
        
        # ====================================================================
        # CONEXIÓN DE SEÑALES Y SLOTS
        # ====================================================================
        self.ui.lvlacept.clicked.connect(self.aceptar_login)
        # Soporte para tecla Enter al escribir la contraseña
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
        
        # Validación de credenciales
        if (usuario == "admin") and password == "manzana":
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
        Abre la ventana del menú principal (Lazy Loading).
        """
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
            self.btn_toggle_password.setText("👁‍🗨") # O puedes usar otro icono para 'ojo cerrado'
            self.password_visible = True


# ============================================================================
# PUNTO DE ENTRADA DE LA APLICACIÓN
# ============================================================================

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())