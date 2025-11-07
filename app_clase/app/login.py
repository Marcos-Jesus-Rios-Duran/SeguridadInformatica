"""
Módulo de Interfaz de Usuario - Pantalla de Login
==================================================

Este módulo contiene la clase Ui_MainWindow que define la interfaz gráfica
para la pantalla de inicio de sesión del sistema.

Autor: [Marcos Jesús Ríos Durán]
Fecha: 07/11/2025
Versión: 1.0.0

Nota: Este archivo es generado automáticamente por PyQt6 UI code generator 6.10.0
      desde el archivo 'login.ui'. No editar manualmente a menos que sea necesario.
"""

# ============================================================================
# IMPORTACIONES
# ============================================================================

from PyQt6 import QtCore, QtGui, QtWidgets


# ============================================================================
# CLASE PRINCIPAL
# ============================================================================

class Ui_MainWindow(object):
    """
    Clase que representa la interfaz de usuario de la ventana de Login.
    
    Esta clase configura todos los componentes visuales de la pantalla de
    inicio de sesión, incluyendo campos de texto para usuario y contraseña,
    botones de acción y elementos decorativos.
    
    Attributes:
        centralwidget (QWidget): Widget central de la ventana principal
        lvluser (QLineEdit): Campo de texto para ingresar el nombre de usuario
        lvlpassword (QLineEdit): Campo de texto para ingresar la contraseña
        lvlacept (QPushButton): Botón para aceptar y validar el login
        lvlcancel (QPushButton): Botón para cancelar el proceso de login
        label (QLabel): Etiqueta con imagen decorativa del sistema
        label_4 (QLabel): Etiqueta de texto "Contraseña"
        label_5 (QLabel): Etiqueta de texto "Usuario"
        menubar (QMenuBar): Barra de menú de la ventana
        statusbar (QStatusBar): Barra de estado de la ventana
    """
    
    def setupUi(self, MainWindow):
        """
        Configura todos los componentes de la interfaz de usuario.
        
        Este método inicializa y posiciona todos los widgets de la ventana,
        establece sus propiedades visuales y configura las conexiones de señales.
        
        Args:
            MainWindow (QMainWindow): Ventana principal donde se montará la UI
            
        Returns:
            None
        """
        # ====================================================================
        # CONFIGURACIÓN DE LA VENTANA PRINCIPAL
        # ====================================================================
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(451, 335)  # Establece dimensiones: 451x335 píxeles
        
        # ====================================================================
        # WIDGET CENTRAL
        # ====================================================================
        
        # Crea el widget central que contendrá todos los demás componentes
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # ====================================================================
        # CAMPOS DE ENTRADA (QLineEdit)
        # ====================================================================
        
        # Campo de texto para el nombre de usuario
        # Posición: x=220, y=130, ancho=231, alto=41
        self.lvluser = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lvluser.setGeometry(QtCore.QRect(220, 60, 231, 41))
        self.lvluser.setObjectName("lvluser")
        
        # Campo de texto para la contraseña
        # Posición: x=220, y=60, ancho=231, alto=41
        self.lvlpassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lvlpassword.setGeometry(QtCore.QRect(220, 130, 231, 41))
        self.lvlpassword.setObjectName("lvlpassword")
        
        # ====================================================================
        # BOTONES DE ACCIÓN (QPushButton)
        # ====================================================================
        
        # Botón "Cancelar" con icono
        # Posición: x=90, y=220, ancho=111, alto=41
        self.lvlcancel = QtWidgets.QPushButton(parent=self.centralwidget)
        self.lvlcancel.setGeometry(QtCore.QRect(90, 220, 111, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagen1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.lvlcancel.setIcon(icon)  # Asigna icono desde "Imagen1.png"
        self.lvlcancel.setObjectName("lvlcancel")
        
        # Botón "Aceptar" con icono
        # Posición: x=260, y=220, ancho=111, alto=41
        self.lvlacept = QtWidgets.QPushButton(parent=self.centralwidget)
        self.lvlacept.setGeometry(QtCore.QRect(260, 220, 111, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Imagen2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.lvlacept.setIcon(icon1)  # Asigna icono desde "Imagen2.png"
        self.lvlacept.setIconSize(QtCore.QSize(18, 18))  # Tamaño del icono: 18x18 px
        self.lvlacept.setObjectName("lvlacept")
        
        # ====================================================================
        # ETIQUETAS DE TEXTO (QLabel)
        # ====================================================================
        
        # Etiqueta "Contraseña"
        # Posición: x=150, y=140, ancho=71, alto=31
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 140, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")  # Fuente: Agency FB
        font.setPointSize(14)  # Tamaño: 14 puntos
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        # Etiqueta "Usuario"
        # Posición: x=160, y=60, ancho=51, alto=31
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 60, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")  # Fuente: Agency FB
        font.setPointSize(14)  # Tamaño: 14 puntos
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        # ====================================================================
        # IMAGEN DECORATIVA
        # ====================================================================
        
        # Etiqueta con imagen del logo/avatar del sistema
        # Posición: x=20, y=50, ancho=121, alto=151
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 121, 151))
        self.label.setText("")  # Sin texto
        self.label.setPixmap(QtGui.QPixmap("Imagen3.png"))  # Carga imagen desde "Imagen3.png"
        self.label.setScaledContents(True)  # Escala la imagen al tamaño del label
        self.label.setObjectName("label")
        
        # ====================================================================
        # CONFIGURACIÓN DE COMPONENTES DE LA VENTANA
        # ====================================================================
        
        # Establece el widget central en la ventana principal
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Configura la barra de menú
        # Posición: x=0, y=0, ancho=451, alto=21
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 451, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        # Configura la barra de estado
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # ====================================================================
        # INICIALIZACIÓN FINAL
        # ====================================================================
        
        # Establece los textos traducibles de la interfaz
        self.retranslateUi(MainWindow)
        
        # Conecta automáticamente las señales y slots por nombre
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        Establece los textos de la interfaz de usuario.
        
        Este método configura todos los textos visibles en la interfaz,
        permitiendo la internacionalización y traducción del sistema.
        
        Args:
            MainWindow (QMainWindow): Ventana principal de la aplicación
            
        Returns:
            None
        """
        # Obtiene la función de traducción
        _translate = QtCore.QCoreApplication.translate
        
        # Configura los textos de cada componente
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))  # Título de la ventana
        self.lvlcancel.setText(_translate("MainWindow", "Cancelar"))  # Texto del botón cancelar
        self.label_4.setText(_translate("MainWindow", "Contraseña"))  # Texto etiqueta contraseña
        self.lvlacept.setText(_translate("MainWindow", "Aceptar"))  # Texto del botón aceptar
        self.label_5.setText(_translate("MainWindow", "Usuario"))  # Texto etiqueta usuario


# ============================================================================
# PUNTO DE ENTRADA DE LA APLICACIÓN
# ============================================================================

if __name__ == "__main__":
    """
    Punto de entrada principal cuando el módulo se ejecuta directamente.
    
    Crea la aplicación Qt, inicializa la ventana principal con la interfaz
    de login y ejecuta el loop principal de eventos.
    """
    import sys
    
    # Crea la aplicación Qt con los argumentos de línea de comandos
    app = QtWidgets.QApplication(sys.argv)
    
    # Crea la ventana principal
    MainWindow = QtWidgets.QMainWindow()
    
    # Instancia la interfaz de usuario
    ui = Ui_MainWindow()
    
    # Configura la interfaz en la ventana principal
    ui.setupUi(MainWindow)
    
    # Muestra la ventana
    MainWindow.show()
    
    # Inicia el loop de eventos y sale con el código de retorno
    sys.exit(app.exec())