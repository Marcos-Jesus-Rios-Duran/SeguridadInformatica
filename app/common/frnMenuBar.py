# common/frnMenuBar.py
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MenuBar(object):
    def setupUi(self, MainWindow):
        # 1. Crear la Barra de Menú
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        # 2. Crear los Menús (Las pestañas de arriba)
        self.menuEncriptar = QtWidgets.QMenu(parent=self.menubar)
        self.menuEncriptar.setTitle("Encriptar")
        
        self.menuDesencriptar = QtWidgets.QMenu(parent=self.menubar)
        self.menuDesencriptar.setTitle("Desencriptar")
        
        self.menuAyuda = QtWidgets.QMenu(parent=self.menubar)
        self.menuAyuda.setTitle("Ayuda")
        
        self.menuSalir = QtWidgets.QMenu(parent=self.menubar)
        self.menuSalir.setTitle("Salir")

        # 3. Crear las Acciones (Las opciones dentro de los menús)
        # Acción para ir a Encriptar
        self.actionIrEncriptar = QtGui.QAction(parent=MainWindow)
        self.actionIrEncriptar.setText("Crear Documento")
        self.actionIrEncriptar.setStatusTip("Ir a la pantalla de encriptación")

        # Acción para ir a Desencriptar
        self.actionIrDesencriptar = QtGui.QAction(parent=MainWindow)
        self.actionIrDesencriptar.setText("Cargar Documento")
        self.actionIrDesencriptar.setStatusTip("Ir a la pantalla de desencriptación")

        # Acción de Ayuda
        self.actionAcercaDe = QtGui.QAction(parent=MainWindow)
        self.actionAcercaDe.setText("Acerca de")

        # Acción de Salir
        self.actionCerrarSesion = QtGui.QAction(parent=MainWindow)
        self.actionCerrarSesion.setText("Cerrar Sesión")

        # 4. Asignar Acciones a los Menús
        self.menuEncriptar.addAction(self.actionIrEncriptar)
        self.menuDesencriptar.addAction(self.actionIrDesencriptar)
        self.menuAyuda.addAction(self.actionAcercaDe)
        self.menuSalir.addAction(self.actionCerrarSesion)

        # 5. Agregar los menús a la barra
        self.menubar.addAction(self.menuEncriptar.menuAction())
        self.menubar.addAction(self.menuDesencriptar.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menubar.addAction(self.menuSalir.menuAction())