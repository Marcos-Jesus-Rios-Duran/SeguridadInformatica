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
    - homePage.menuLogic.MenuWindow: Ventana del menú principal

"""

# ============================================================================
# IMPORTACIONES
# ============================================================================

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QPushButton
from login import Ui_MainWindow
from homePage.menu import MenuWindow


# ============================================================================
# CLASE PRINCIPAL - LOGIN WINDOW
# ============================================================================

class LoginWindow(QMainWindow):
    """
    Clase que gestiona la lógica de negocio de la ventana de inicio de sesión.
    
    Esta clase hereda de QMainWindow y proporciona toda la funcionalidad
    necesaria para el proceso de autenticación, incluyendo validación de
    credenciales, gestión de visibilidad de contraseña y navegación al
    sistema principal.
    
    Attributes:
        ui (Ui_MainWindow): Instancia de la interfaz de usuario del login
        btn_toggle_password (QPushButton): Botón para mostrar/ocultar contraseña
        password_visible (bool): Estado de visibilidad de la contraseña
        menu_window (MenuWindow): Referencia a la ventana del menú principal
        
    Credenciales válidas:
        - Usuario: "admin" o "Marcos"
        - Contraseña: "mrco"
    """
    
    def __init__(self):
        """
        Constructor de la clase LoginWindow.
        
        Inicializa la ventana de login, configura la interfaz de usuario,
        establece el modo de ocultación de contraseña, crea el botón de
        visibilidad y conecta todas las señales con sus respectivos slots.
        
        Proceso de inicialización:
            1. Inicializa la clase padre QMainWindow
            2. Configura la interfaz de usuario desde login.py
            3. Establece el modo Password para el campo de contraseña
            4. Crea y configura el botón de toggle de visibilidad
            5. Conecta señales de botones con sus manejadores
        """
        # ====================================================================
        # INICIALIZACIÓN DE LA CLASE PADRE
        # ====================================================================
        
        # Inicializa la clase padre QMainWindow
        super().__init__()
        
        # ====================================================================
        # CONFIGURACIÓN DE LA INTERFAZ DE USUARIO
        # ====================================================================
        
        # Crea e inicializa la interfaz de usuario del login
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # ====================================================================
        # CONFIGURACIÓN DEL CAMPO DE CONTRASEÑA
        # ====================================================================
        
        # Ocultar contraseña con asteriscos por defecto
        # EchoMode.Password muestra asteriscos en lugar del texto real
        self.ui.lvlpassword.setEchoMode(QLineEdit.EchoMode.Password)
        
        # ====================================================================
        # BOTÓN PARA MOSTRAR/OCULTAR CONTRASEÑA
        # ====================================================================
        
        # Crear botón de toggle para visibilidad de contraseña
        # Posición: x=420, y=138, ancho=25, alto=25
        self.btn_toggle_password = QPushButton(self.ui.centralwidget)
        self.btn_toggle_password.setGeometry(420, 138, 25, 25)
        self.btn_toggle_password.setText("👁")  # Icono de ojo
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
        
        # Conectar el botón con su función
        self.btn_toggle_password.clicked.connect(self.toggle_password)
        
        # Estado inicial de visibilidad (oculta)
        self.password_visible = False
        
        # ====================================================================
        # CONEXIÓN DE SEÑALES Y SLOTS
        # ====================================================================
        
        # Conectar botón "Aceptar" con la validación de login
        self.ui.lvlacept.clicked.connect(self.aceptar_login)
        # Conectamos el "Enter" de la contraseña a la misma función de aceptar
        self.ui.lvlpassword.returnPressed.connect(self.aceptar_login)
        
        # Conectar botón "Cancelar" con el cierre de la aplicación
        self.ui.lvlcancel.clicked.connect(self.close)
    
    # ========================================================================
    # MÉTODOS DE VALIDACIÓN
    # ========================================================================
    
    def validar_campos(self):
        """
        Valida que los campos de usuario y contraseña no estén vacíos.
        
        Este método verifica que ambos campos requeridos contengan información
        antes de proceder con la autenticación. Muestra mensajes de advertencia
        al usuario en caso de encontrar campos vacíos.
            
        Returns:
            bool: True si ambos campos contienen datos, False en caso contrario
            
        Efectos secundarios:
            - Muestra QMessageBox de advertencia si algún campo está vacío
        """
        # Obtiene el texto ingresado en el campo de usuario (elimina espacios)
        usuario = self.ui.lvluser.text().strip()
        
        # Obtiene el texto ingresado en el campo de contraseña
        password = self.ui.lvlpassword.text()
        
        # ====================================================================
        # VALIDACIÓN: AMBOS CAMPOS VACÍOS
        # ====================================================================
        
        if not usuario and not password:
            QMessageBox.warning(
                self, 
                "Error", 
                "Por favor complete todos los campos"
            )
            return False
        
        # ====================================================================
        # VALIDACIÓN: CAMPO DE USUARIO VACÍO
        # ====================================================================
        
        if not usuario:
            QMessageBox.warning(
                self, 
                "Error", 
                "Por favor ingrese un usuario"
            )
            return False
        
        # ====================================================================
        # VALIDACIÓN: CAMPO DE CONTRASEÑA VACÍO
        # ====================================================================
        
        if not password:
            QMessageBox.warning(
                self, 
                "Error", 
                "Por favor ingrese una contraseña"
            )
            return False
        
        # ====================================================================
        # VALIDACIÓN EXITOSA
        # ====================================================================
        
        # Retorna True si ambos campos son válidos
        return True
    
    # ========================================================================
    # MÉTODOS DE AUTENTICACIÓN
    # ========================================================================
    
    def aceptar_login(self):
        """
        Procesa el intento de inicio de sesión del usuario.
        
        Este método coordina el proceso completo de autenticación:
        1. Valida que los campos no estén vacíos
        2. Obtiene las credenciales ingresadas
        3. Verifica las credenciales contra los valores permitidos
        4. Muestra mensajes de éxito o error según corresponda
        5. Abre la ventana del menú principal si las credenciales son correctas
        
        Credenciales válidas:
            - Usuarios permitidos: "admin" o "Marcos"
            - Contraseña requerida: "mrco"
        """
        # ====================================================================
        # PASO 1: VALIDACIÓN DE CAMPOS
        # ====================================================================
        
        # Verificar que los campos no estén vacíos
        if not self.validar_campos():
            return  # Detener el proceso si la validación falla
        
        # ====================================================================
        # PASO 2: OBTENCIÓN DE CREDENCIALES
        # ====================================================================
        
        # Obtiene el nombre de usuario ingresado (sin espacios)
        usuario = self.ui.lvluser.text().strip()
        
        # Obtiene la contraseña ingresada
        password = self.ui.lvlpassword.text()
        
        # ====================================================================
        # PASO 3: VERIFICACIÓN DE CREDENCIALES
        # ====================================================================
        
        # Valida usuario y contraseña contra los valores permitidos
        if (usuario == "admin" or usuario == "Marcos") and password == "mrco":
            # ================================================================
            # AUTENTICACIÓN EXITOSA
            # ================================================================
            
            # Mostrar mensaje de bienvenida
            QMessageBox.information(
                self, 
                "Éxito", 
                f"¡Bienvenido {usuario}!\n\nAcceso concedido al sistema."
            )
            
            # Abrir ventana de menú principal
            self.abrir_menu()
        else:
            # ================================================================
            # AUTENTICACIÓN FALLIDA
            # ================================================================
            
            # Mostrar mensaje de error
            QMessageBox.critical(
                self, 
                "Error de Autenticación", 
                "Usuario o contraseña incorrectos.\n\nPor favor, intente nuevamente."
            )
            
            # Opcional: Limpiar el campo de contraseña por seguridad
            self.ui.lvlpassword.clear()
            self.ui.lvlpassword.setFocus()
    
    # ========================================================================
    # MÉTODOS DE NAVEGACIÓN
    # ========================================================================
    
    def abrir_menu(self):
        """
        Abre la ventana del menú principal y cierra la ventana de login.
        
        Este método gestiona la transición desde la pantalla de autenticación
        hacia el menú principal del sistema una vez que el usuario ha sido
        autenticado exitosamente.
            
        Efectos secundarios:
            - Crea una nueva instancia de MenuWindow
            - Muestra la ventana del menú principal
            - Cierra la ventana de login actual
        """
        # Crear y almacenar referencia a la ventana del menú
        self.menu_window = MenuWindow()
        
        # Mostrar la ventana del menú principal
        self.menu_window.show()
        
        # Cerrar la ventana de login
        self.close()
    
    # ========================================================================
    # MÉTODOS DE INTERACCIÓN
    # ========================================================================
    
    def toggle_password(self):
        """
        Alterna la visibilidad del campo de contraseña.
        
        Este método cambia el modo de visualización del campo de contraseña
        entre texto oculto (asteriscos) y texto visible, actualizando también
        el icono del botón para reflejar el estado actual.
        
        Estados:
            - Oculta (False): Muestra asteriscos, icono "👁"
            - Visible (True): Muestra texto plano, icono "👁‍🗨"
            
        Efectos secundarios:
            - Cambia el modo de eco del campo de contraseña
            - Actualiza el texto del botón de toggle
            - Modifica el estado de la variable password_visible
        """
        # Verifica el estado actual de visibilidad
        if self.password_visible:
            # ================================================================
            # OCULTAR CONTRASEÑA
            # ================================================================
            
            # Establece modo de contraseña (muestra asteriscos)
            self.ui.lvlpassword.setEchoMode(QLineEdit.EchoMode.Password)
            
            # Cambia el icono a ojo cerrado
            self.btn_toggle_password.setText("👁")
            
            # Actualiza el estado a no visible
            self.password_visible = False
        else:
            # ================================================================
            # MOSTRAR CONTRASEÑA
            # ================================================================
            
            # Establece modo normal (muestra texto plano)
            self.ui.lvlpassword.setEchoMode(QLineEdit.EchoMode.Normal)
            
            # Cambia el icono a ojo abierto
            self.btn_toggle_password.setText("👁‍🗨")
            
            # Actualiza el estado a visible
            self.password_visible = True


# ============================================================================
# PUNTO DE ENTRADA DE LA APLICACIÓN
# ============================================================================

if __name__ == "__main__":
    """
    Punto de entrada principal de la aplicación.
    Returns:
        int: Código de salida de la aplicación (0 = éxito, otro = error)
        
    Example:
        $ python main.py
    """
    # Crea la aplicación Qt con los argumentos de línea de comandos
    app = QApplication(sys.argv)
    
    # Crea e instancia la ventana de login
    window = LoginWindow()
    
    # Muestra la ventana
    window.show()
    
    # Inicia el loop de eventos y sale con el código de retorno
    sys.exit(app.exec())