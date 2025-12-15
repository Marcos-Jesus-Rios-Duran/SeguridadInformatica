"""
Vista de Encriptación (Sleek Cyber Horizontal)
==============================================
Botones organizados horizontalmente en la parte inferior.
Incluye el botón "Cargar" integrado en el diseño.

Autor: [Marcos Jesús Ríos Durán]
Fecha: 14/12/2025
Versión: 2.1.0 (Horizontal)
"""

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # ====================================================================
        # 1. CONFIGURACIÓN GENERAL
        # ====================================================================
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        
        # Fondo degradado
        MainWindow.setStyleSheet("""
            QMainWindow {
                background: qradialgradient(
                    cx:0.5, cy:0.5, radius: 1.0,
                    fx:0.5, fy:0.5,
                    stop:0 #0F172A,
                    stop:1 #020617
                );
            }
        """)
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ====================================================================
        # 2. ENCABEZADO
        # ====================================================================
        self.label_titulo = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_titulo.setGeometry(QtCore.QRect(50, 30, 400, 40))
        self.label_titulo.setText("MÓDULO DE ENCRIPTACIÓN")
        self.label_titulo.setStyleSheet("""
            font-family: 'Segoe UI Black';
            font-size: 24px;
            font-weight: 800;
            color: #F0FDF4;
            letter-spacing: 2px;
        """)

        # ====================================================================
        # 3. TERMINAL (ÁREA DE TEXTO)
        # ====================================================================
        # Etiqueta
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 80, 300, 20))
        self.label.setStyleSheet("color: #34D399; font-weight: bold; letter-spacing: 1px;")
        
        # Área de Texto (Ahora ocupa casi todo el ancho, dejando espacio abajo para botones)
        self.txtMensaje = QtWidgets.QTextEdit(parent=self.centralwidget)
        # Ajustamos altura: Empieza en 110 y termina en 550 (440px de alto)
        self.txtMensaje.setGeometry(QtCore.QRect(50, 110, 800, 440))
        self.txtMensaje.setStyleSheet("""
            QTextEdit {
                background-color: #0F172A;
                border: 2px solid #1E293B;
                border-radius: 15px;
                padding: 15px;
                color: #22D3EE;
                font-family: 'Consolas', monospace;
                font-size: 14px;
            }
            QTextEdit:focus {
                border: 2px solid #34D399;
                background-color: #020617;
            }
        """)
        
        shadow_txt = QGraphicsDropShadowEffect(self.txtMensaje)
        shadow_txt.setBlurRadius(20)
        shadow_txt.setColor(QColor(34, 211, 238, 40))
        self.txtMensaje.setGraphicsEffect(shadow_txt)

        # ====================================================================
        # 4. BOTONERA HORIZONTAL (ABAJO)
        # ====================================================================
        # Creamos un contenedor horizontal invisible en Y=580
        self.panel_botones = QtWidgets.QFrame(parent=self.centralwidget)
        self.panel_botones.setGeometry(QtCore.QRect(50, 580, 800, 80))
        self.panel_botones.setStyleSheet("background: transparent;")
        
        # --- ESTILOS ---
        style_btn = """
            QPushButton {
                background-color: #1E293B;
                color: white;
                border-radius: 10px;
                font-weight: bold;
                font-family: 'Segoe UI';
                font-size: 13px;
                border: 1px solid #334155;
            }
            QPushButton:hover {
                margin-top: -2px; /* Pequeño salto */
            }
        """
        
        # Estilo Principal (Verde)
        style_primary = style_btn + """
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #10B981, stop:1 #06B6D4);
                border: none;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #34D399, stop:1 #22D3EE);
            }
        """

        # Estilo Acción (Cian)
        style_action = style_btn + """
            QPushButton {
                border: 2px solid #06B6D4;
                color: #22D3EE;
            }
            QPushButton:hover { background-color: rgba(6, 182, 212, 0.1); color: white; }
        """

        # Estilo Email (Índigo)
        style_email = style_btn + """
            QPushButton {
                border: 2px solid #6366F1;
                color: #818CF8;
            }
            QPushButton:hover { background-color: rgba(99, 102, 241, 0.1); color: white; }
        """
        
        # Estilo Regresar (Rojo sutil)
        style_back = style_btn + """
            QPushButton {
                border: 1px dashed #64748B;
                color: #94A3B8;
            }
            QPushButton:hover { border-color: #EF4444; color: #EF4444; }
        """

        # --- BOTONES (Calculando anchos para 800px total) ---
        # Total ancho disponible: 800. 5 Botones.
        # Ancho aprox por botón: 150px. Espacio entre ellos: 10px.
        
        # 1. Cargar TXT
        self.btnCargar = QtWidgets.QPushButton(parent=self.panel_botones)
        self.btnCargar.setGeometry(QtCore.QRect(0, 10, 140, 50))
        self.btnCargar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnCargar.setStyleSheet(style_action)

        # 2. Encriptar (Más grande y llamativo)
        self.btnEncriptar = QtWidgets.QPushButton(parent=self.panel_botones)
        self.btnEncriptar.setGeometry(QtCore.QRect(150, 0, 200, 60)) # Un poco más alto
        self.btnEncriptar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnEncriptar.setStyleSheet(style_primary)
        
        # 3. Descargar
        self.btnDescargar = QtWidgets.QPushButton(parent=self.panel_botones)
        self.btnDescargar.setGeometry(QtCore.QRect(360, 10, 140, 50))
        self.btnDescargar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnDescargar.setStyleSheet(style_action)

        # 4. Enviar Email
        self.btnEnviar = QtWidgets.QPushButton(parent=self.panel_botones)
        self.btnEnviar.setGeometry(QtCore.QRect(510, 10, 140, 50))
        self.btnEnviar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnEnviar.setStyleSheet(style_email)

        # 5. Regresar (Al final)
        self.btnRegresar = QtWidgets.QPushButton(parent=self.panel_botones)
        self.btnRegresar.setGeometry(QtCore.QRect(660, 10, 140, 50))
        self.btnRegresar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnRegresar.setStyleSheet(style_back)

        # ====================================================================
        # INICIALIZACIÓN
        # ====================================================================
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secure Nexus - Encriptación"))
        self.label.setText(_translate("MainWindow", "INPUT DE DATOS >"))
        self.txtMensaje.setPlaceholderText(_translate("MainWindow", "// Terminal lista. Escriba o cargue un archivo..."))
        
        # Textos
        self.btnCargar.setText(_translate("MainWindow", "📂 Cargar"))
        self.btnEncriptar.setText(_translate("MainWindow", "🔒 ENCRIPTAR"))
        self.btnDescargar.setText(_translate("MainWindow", "💾 Guardar"))
        self.btnEnviar.setText(_translate("MainWindow", "📧 Enviar"))
        self.btnRegresar.setText(_translate("MainWindow", "← Volver"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())