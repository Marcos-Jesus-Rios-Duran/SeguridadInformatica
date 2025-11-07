import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QPushButton
from login import Ui_MainWindow
from menuBackEnd import MenuWindow  # Importar la ventana del menú

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Ocultar contraseña con asteriscos
        self.ui.lvlpassword.setEchoMode(QLineEdit.EchoMode.Password)
        
        # Botón para mostrar/ocultar contraseña
        self.btn_toggle_password = QPushButton(self.ui.centralwidget)
        self.btn_toggle_password.setGeometry(420, 138, 25, 25)
        self.btn_toggle_password.setText("👁")
        self.btn_toggle_password.clicked.connect(self.toggle_password)
        self.password_visible = False
        
        # Conectar botones
        self.ui.lvlacept.clicked.connect(self.aceptar_login)
        self.ui.lvlcancel.clicked.connect(self.close)
    
    def validar_campos(self):
        usuario = self.ui.lvluser.text()
        password = self.ui.lvlpassword.text()
        
        if not usuario:
            QMessageBox.warning(self, "Error", "Por favor ingrese un usuario")
            return False
        
        if not password:
            QMessageBox.warning(self, "Error", "Por favor ingrese una contraseña")
            return False
        
        return True
    
    def aceptar_login(self):
        # Validación de campos vacios
        if self.validar_campos():
            # Obtenemos los valores ingresados
            usuario = self.ui.lvluser.text()
            password = self.ui.lvlpassword.text()
            
            # Validamos usuario y contraseña
            if (usuario == "admin" or usuario == "Marcos") and password == "mrco":
                QMessageBox.information(self, "Éxito", f"¡Bienvenido {usuario}!")
                # Abrir ventana de menú
                self.abrir_menu()
            else:
                QMessageBox.critical(self, "Error", "Usuario o contraseña incorrectos")
    
    def abrir_menu(self):
        # Crear y mostrar la ventana del menú
        self.menu_window = MenuWindow()
        self.menu_window.show()
        # Cerrar la ventana de login
        self.close()
    
    def toggle_password(self):
        if self.password_visible:
            self.ui.lvlpassword.setEchoMode(QLineEdit.EchoMode.Password)
            self.btn_toggle_password.setText("👁")
            self.password_visible = False
        else:
            self.ui.lvlpassword.setEchoMode(QLineEdit.EchoMode.Normal)
            self.btn_toggle_password.setText("👁‍🗨")
            self.password_visible = True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())