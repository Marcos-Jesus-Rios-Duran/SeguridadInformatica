"""
Módulo de Interfaz de Usuario - Pantalla de Menú Principal
===========================================================

Este módulo contiene la clase menu que define la interfaz gráfica
para la pantalla del menú principal del sistema de encriptación.

Autor: [Marcos Jesús Ríos Durán]
Fecha: 07/11/2025
Versión: 1.0.0

Nota: Este archivo es generado automáticamente por PyQt6 UI code generator 6.10.0
      desde el archivo 'frnMenu.ui'. No editar manualmente a menos que sea necesario.
"""

# ============================================================================
# IMPORTACIONES
# ============================================================================

from PyQt6 import QtCore, QtGui, QtWidgets


# ============================================================================
# CLASE PRINCIPAL
# ============================================================================

class menu(object):
    """
    Clase que representa la interfaz de usuario de la ventana del menú principal.
    
    Esta clase configura todos los componentes visuales del menú principal,
    incluyendo la barra de menús con opciones de encriptación, desencriptación,
    ayuda y salida del sistema.
    
    Attributes:
        centralwidget (QWidget): Widget central de la ventana principal
        menubar (QMenuBar): Barra de menú principal de la ventana
        menuEncriptar (QMenu): Menú de opciones de encriptación
        menuDesencriptar (QMenu): Menú de opciones de desencriptación
        menuAyuda (QMenu): Menú de ayuda del sistema
        menusalir (QMenu): Menú para salir de la aplicación
        statusbar (QStatusBar): Barra de estado de la ventana
        Crear_Documento (QAction): Acción para crear un nuevo documento
        ctionCargarDocumento (QAction): Acción para cargar un documento existente
    """
    
    def setupUi(self, MainWindow):
        """
        Configura todos los componentes de la interfaz de usuario del menú.
        
        Este método inicializa y posiciona todos los widgets del menú principal,
        establece sus propiedades visuales y configura las acciones disponibles
        en la barra de menús.
        
        Args:
            MainWindow (QMainWindow): Ventana principal donde se montará la UI
            
        Returns:
            None
            
        Example:
            >>> window = QtWidgets.QMainWindow()
            >>> ui = menu()
            >>> ui.setupUi(window)
        """
        # ====================================================================
        # CONFIGURACIÓN DE LA VENTANA PRINCIPAL
        # ====================================================================
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)  # Establece dimensiones: 800x600 píxeles
        
        # ====================================================================
        # WIDGET CENTRAL
        # ====================================================================
        
        # Crea el widget central que contendrá todos los demás componentes
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        # ====================================================================
        # BARRA DE MENÚ PRINCIPAL
        # ====================================================================
        
        # Configura la barra de menú
        # Posición: x=0, y=0, ancho=800, alto=21
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        
        # ====================================================================
        # MENÚS DE OPCIONES
        # ====================================================================
        
        # Menú "Encriptar" - Contiene opciones para encriptar documentos
        self.menuEncriptar = QtWidgets.QMenu(parent=self.menubar)
        self.menuEncriptar.setObjectName("menuEncriptar")
        
        # Menú "Desencriptar" - Contiene opciones para desencriptar documentos
        self.menuDesencriptar = QtWidgets.QMenu(parent=self.menubar)
        self.menuDesencriptar.setObjectName("menuDesencriptar")
        
        # Menú "Ayuda" - Contiene información de ayuda del sistema
        self.menuAyuda = QtWidgets.QMenu(parent=self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        
        # Menú "Salir" - Contiene opciones para cerrar la aplicación
        self.menusalir = QtWidgets.QMenu(parent=self.menubar)
        self.menusalir.setObjectName("menusalir")
        
        # Establece la barra de menú en la ventana principal
        MainWindow.setMenuBar(self.menubar)
        
        # ====================================================================
        # BARRA DE ESTADO
        # ====================================================================
        
        # Configura la barra de estado en la parte inferior de la ventana
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # ====================================================================
        # ACCIONES DEL MENÚ
        # ====================================================================
        
        # Acción "Crear Documento" - Permite crear un nuevo documento para encriptar
        self.Crear_Documento = QtGui.QAction(parent=MainWindow)
        self.Crear_Documento.setObjectName("Crear_Documento")
        
        # Acción "Cargar Documento" - Permite cargar un documento existente para desencriptar
        self.ctionCargarDocumento = QtGui.QAction(parent=MainWindow)
        self.ctionCargarDocumento.setObjectName("ctionCargarDocumento")
        
        # ====================================================================
        # ASIGNACIÓN DE ACCIONES A MENÚS
        # ====================================================================
        
        # Agrega la acción "Crear Documento" al menú "Encriptar"
        self.menuEncriptar.addAction(self.Crear_Documento)
        
        # Agrega la acción "Cargar Documento" al menú "Desencriptar"
        self.menuDesencriptar.addAction(self.ctionCargarDocumento)
        
        # ====================================================================
        # AGREGANDO MENÚS A LA BARRA PRINCIPAL
        # ====================================================================
        
        # Agrega el menú "Encriptar" a la barra de menú
        self.menubar.addAction(self.menuEncriptar.menuAction())
        
        # Agrega el menú "Desencriptar" a la barra de menú
        self.menubar.addAction(self.menuDesencriptar.menuAction())
        
        # Agrega el menú "Ayuda" a la barra de menú
        self.menubar.addAction(self.menuAyuda.menuAction())
        
        # Agrega el menú "Salir" a la barra de menú
        self.menubar.addAction(self.menusalir.menuAction())

        # ====================================================================
        # INICIALIZACIÓN FINAL
        # ====================================================================
        
        # Establece los textos traducibles de la interfaz
        self.retranslateUi(MainWindow)
        
        # Conecta automáticamente las señales y slots por nombre
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        Establece los textos de la interfaz de usuario del menú.
        
        Este método configura todos los textos visibles en el menú principal,
        permitiendo la internacionalización y traducción del sistema.
        
        Args:
            MainWindow (QMainWindow): Ventana principal de la aplicación
            
        Returns:
            None
            
        Example:
            >>> ui.retranslateUi(MainWindow)
        """
        # Obtiene la función de traducción
        _translate = QtCore.QCoreApplication.translate
        
        # ====================================================================
        # CONFIGURACIÓN DE TEXTOS
        # ====================================================================
        
        # Título de la ventana principal
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        # Texto del menú "Encriptar"
        self.menuEncriptar.setTitle(_translate("MainWindow", "Encriptar"))
        
        # Texto del menú "Desencriptar"
        self.menuDesencriptar.setTitle(_translate("MainWindow", "Desencriptar"))
        
        # Texto del menú "Ayuda"
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        
        # Texto del menú "Salir"
        self.menusalir.setTitle(_translate("MainWindow", "Salir"))
        
        # Texto de la acción "Crear Documento"
        self.Crear_Documento.setText(_translate("MainWindow", "Crear Documento"))
        
        # Texto de la acción "Cargar Documento"
        self.ctionCargarDocumento.setText(_translate("MainWindow", "Cargar Documento"))


# ============================================================================
# PUNTO DE ENTRADA DE LA APLICACIÓN
# ============================================================================

if __name__ == "__main__":
    """
    Punto de entrada principal cuando el módulo se ejecuta directamente.
    
    Crea la aplicación Qt, inicializa la ventana principal con la interfaz
    del menú y ejecuta el loop principal de eventos.
    """
    import sys
    
    # Crea la aplicación Qt con los argumentos de línea de comandos
    app = QtWidgets.QApplication(sys.argv)
    
    # Crea la ventana principal
    MainWindow = QtWidgets.QMainWindow()
    
    # Instancia la interfaz de usuario del menú
    ui = menu()
    
    # Configura la interfaz en la ventana principal
    ui.setupUi(MainWindow)
    
    # Muestra la ventana
    MainWindow.show()
    
    # Inicia el loop de eventos y sale con el código de retorno
    sys.exit(app.exec())