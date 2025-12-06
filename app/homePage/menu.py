"""
Ventana del Menú Principal - Backend
====================================

Este módulo contiene la clase MenuWindow que implementa la lógica del menú
principal con diseño de bienvenida elegante usando el MenuBarComponent.

Autor: Marcos Jesús Ríos Durán
Fecha: 07/12/2025
Versión: 1.0.0

Dependencias:
    - PyQt6.QtWidgets: Componentes de interfaz gráfica
    - PyQt6.QtCore: Funcionalidades core de Qt
    - app.common.MenuBarComponent: Navbar reutilizable
"""

# ============================================================================
# IMPORTACIONES
# ============================================================================

import sys 
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QFrame, QWidget
from PyQt6.QtCore import Qt
from common.MenuBarComponent import MenuBarComponent


# ============================================================================
# CLASE PRINCIPAL
# ============================================================================

class MenuWindow(QMainWindow):
    """
    Clase que gestiona la ventana del menú principal con diseño de bienvenida.
    
    Esta clase utiliza:
        - MenuBarComponent: Para el navbar compartido
        - Diseño personalizado: Frame con tarjetas de bienvenida
    
    Attributes:
        centralwidget (QWidget): Widget central de la ventana
        menubar_component (MenuBarComponent): Componente del navbar
        frame_principal (QFrame): Frame contenedor del diseño
        label_icono (QLabel): Label con el icono principal 🔐
        label_titulo (QLabel): Label para el título
        label_subtitulo (QLabel): Label para el subtítulo
        linea_separadora (QFrame): Línea decorativa
        card_encriptar (QLabel): Tarjeta informativa de encriptación
        card_desencriptar (QLabel): Tarjeta informativa de desencriptación
        card_seguridad (QLabel): Tarjeta informativa de seguridad
    """
    
    def __init__(self):
        """
        Constructor de la clase MenuWindow.
        
        Inicializa la ventana del menú principal, configura el menubar
        reutilizable y crea el diseño de bienvenida elegante en azul.
        """
        # ====================================================================
        # INICIALIZACIÓN DE LA CLASE PADRE
        # ====================================================================
        
        super().__init__()
        
        # ====================================================================
        # CONFIGURACIÓN DE LA VENTANA
        # ====================================================================
        
        # Título de la ventana
        self.setWindowTitle("Menú Principal - Sistema de Encriptación")
        
        # Tamaño de la ventana
        self.resize(800, 600)
        
        # ====================================================================
        # CREAR WIDGET CENTRAL
        # ====================================================================
        
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        
        # Fondo degradado azul elegante
        self.centralwidget.setStyleSheet("""
            QWidget#centralwidget {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #E8F4F8,
                    stop:1 #D4E7F1
                );
            }
        """)
        
        # ====================================================================
        # AGREGAR MENUBAR REUTILIZABLE
        # ====================================================================
        
        # Crear y configurar el menubar component (navbar compartido)
        self.menubar_component = MenuBarComponent(self)
        menubar = self.menubar_component.setup_menubar()
        self.setMenuBar(menubar)
        
        # ====================================================================
        # CONFIGURAR DISEÑO DE BIENVENIDA
        # ====================================================================
        
        self.setup_welcome_design()
    
    def setup_welcome_design(self):
        """
        Configura el diseño de bienvenida con estilo elegante azul.
        
        Crea todos los elementos visuales del mensaje de bienvenida:
            - Frame principal blanco con bordes redondeados
            - Icono grande de seguridad (🔐)
            - Título principal del sistema
            - Subtítulo descriptivo
            - Línea separadora decorativa
            - Tres tarjetas informativas con iconos
        
        Paleta de colores azul elegante (inspirada en trajes formales):
            - #1E3A8A: Azul marino oscuro
            - #2563EB: Azul medio
            - #3B82F6: Azul brillante
            - #60A5FA: Azul claro
            - #BFDBFE, #DBEAFE: Azules pastel suaves
        """
        # ====================================================================
        # FRAME PRINCIPAL CON ESTILO
        # ====================================================================
        
        self.frame_principal = QFrame(self.centralwidget)
        self.frame_principal.setGeometry(100, 80, 600, 450)
        self.frame_principal.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 20px;
                border: 2px solid #3B82F6;
            }
        """)
        
        # ====================================================================
        # ICONO PRINCIPAL
        # ====================================================================
        
        self.label_icono = QLabel(self.frame_principal)
        self.label_icono.setGeometry(0, 30, 600, 120)
        self.label_icono.setText("🔐")
        self.label_icono.setStyleSheet("""
            QLabel {
                font-size: 100px;
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #1E3A8A,
                    stop:0.5 #3B82F6,
                    stop:1 #60A5FA
                );
                border-radius: 15px;
                padding: 10px;
            }
        """)
        self.label_icono.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # ====================================================================
        # TÍTULO PRINCIPAL
        # ====================================================================
        
        self.label_titulo = QLabel(self.frame_principal)
        self.label_titulo.setGeometry(50, 160, 500, 50)
        self.label_titulo.setText("Sistema de Encriptación")
        self.label_titulo.setStyleSheet("""
            QLabel {
                font-size: 28px;
                font-weight: bold;
                color: #1E3A8A;
                font-family: 'Segoe UI', 'Arial', sans-serif;
                letter-spacing: 1px;
            }
        """)
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # ====================================================================
        # SUBTÍTULO
        # ====================================================================
        
        self.label_subtitulo = QLabel(self.frame_principal)
        self.label_subtitulo.setGeometry(50, 210, 500, 30)
        self.label_subtitulo.setText("¡Bienvenido! Protege tu información de manera segura")
        self.label_subtitulo.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #2563EB;
                font-family: 'Segoe UI', 'Arial', sans-serif;
                font-style: italic;
            }
        """)
        self.label_subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # ====================================================================
        # LÍNEA SEPARADORA DECORATIVA
        # ====================================================================
        
        self.linea_separadora = QFrame(self.frame_principal)
        self.linea_separadora.setGeometry(150, 255, 300, 2)
        self.linea_separadora.setStyleSheet("""
            QFrame {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 transparent,
                    stop:0.5 #3B82F6,
                    stop:1 transparent
                );
                border: none;
            }
        """)
        
        # ====================================================================
        # TARJETAS INFORMATIVAS
        # ====================================================================
        
        # Tarjeta 1: Encriptar
        self.card_encriptar = QLabel(self.frame_principal)
        self.card_encriptar.setGeometry(80, 280, 150, 140)
        self.card_encriptar.setText(
            "🔒\n\n"
            "Encriptar\n\n"
            "Protege tus\n"
            "documentos"
        )
        self.card_encriptar.setStyleSheet("""
            QLabel {
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 #DBEAFE,
                    stop:1 #BFDBFE
                );
                border: 2px solid #3B82F6;
                border-radius: 15px;
                padding: 15px;
                font-size: 13px;
                font-weight: bold;
                color: #1E3A8A;
                font-family: 'Segoe UI', 'Arial', sans-serif;
            }
        """)
        self.card_encriptar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Tarjeta 2: Desencriptar
        self.card_desencriptar = QLabel(self.frame_principal)
        self.card_desencriptar.setGeometry(240, 280, 150, 140)
        self.card_desencriptar.setText(
            "🔓\n\n"
            "Desencriptar\n\n"
            "Accede a tus\n"
            "archivos"
        )
        self.card_desencriptar.setStyleSheet("""
            QLabel {
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 #DBEAFE,
                    stop:1 #BFDBFE
                );
                border: 2px solid #3B82F6;
                border-radius: 15px;
                padding: 15px;
                font-size: 13px;
                font-weight: bold;
                color: #1E3A8A;
                font-family: 'Segoe UI', 'Arial', sans-serif;
            }
        """)
        self.card_desencriptar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Tarjeta 3: Seguridad
        self.card_seguridad = QLabel(self.frame_principal)
        self.card_seguridad.setGeometry(400, 280, 150, 140)
        self.card_seguridad.setText(
            "🛡️\n\n"
            "Seguridad\n\n"
            "Máxima\n"
            "protección"
        )
        self.card_seguridad.setStyleSheet("""
            QLabel {
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 #DBEAFE,
                    stop:1 #BFDBFE
                );
                border: 2px solid #3B82F6;
                border-radius: 15px;
                padding: 15px;
                font-size: 13px;
                font-weight: bold;
                color: #1E3A8A;
                font-family: 'Segoe UI', 'Arial', sans-serif;
            }
        """)
        self.card_seguridad.setAlignment(Qt.AlignmentFlag.AlignCenter)


# ============================================================================
# PUNTO DE ENTRADA DE LA APLICACIÓN
# ============================================================================

if __name__ == "__main__":
    """
    Punto de entrada cuando el módulo se ejecuta directamente.
    Útil para pruebas del menú sin pasar por el login.
    """
    app = QApplication(sys.argv)
    window = MenuWindow()
    window.show()
    sys.exit(app.exec())