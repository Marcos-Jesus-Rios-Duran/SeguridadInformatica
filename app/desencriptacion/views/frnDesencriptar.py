"""
Vista de Desencriptación (Sleek Cyber Horizontal)
=================================================
Interfaz gráfica moderna para el módulo de desencriptación.
Diseño coherente con el resto del sistema "Sleek Cyber".

Autor: [Marcos Jesús Ríos Durán]
Fecha: 14/12/2025
Versión: 2.1.0 (Horizontal Cyber)
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
        
        # Fondo degradado profundo
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
        # 2. ENCABEZADO Y CARGA
        # ====================================================================
        
        # Título pequeño
        self.label_titulo = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_titulo.setGeometry(QtCore.QRect(50, 20, 300, 30))
        self.label_titulo.setText("MÓDULO DE Desencriptacion")
        self.label_titulo.setStyleSheet("""
            font-family: 'Segoe UI Black';
            font-size: 18px;
            color: #64748B;
            letter-spacing: 2px;
        """)
        
        # BOTÓN CARGAR ARCHIVO (Gigante y Principal)
        self.btnCargarArchivo = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnCargarArchivo.setGeometry(QtCore.QRect(50, 60, 800, 80))
        self.btnCargarArchivo.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        
        # Estilo llamativo para la acción principal
        self.btnCargarArchivo.setStyleSheet("""
            QPushButton {
                background-color: rgba(30, 41, 59, 0.6);
                border: 2px dashed #06B6D4; /* Borde punteado Cian */
                border-radius: 15px;
                color: #22D3EE;
                font-family: 'Segoe UI Black';
                font-size: 20px;
                letter-spacing: 1px;
            }
            QPushButton:hover {
                background-color: rgba(6, 182, 212, 0.1);
                border: 2px solid #22D3EE; /* Borde sólido al pasar mouse */
                color: white;
            }
        """)

        # ====================================================================
        # 3. TERMINAL DE VISUALIZACIÓN
        # ====================================================================
        
        # Etiqueta
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 160, 300, 20))
        self.label.setStyleSheet("color: #34D399; font-weight: bold; letter-spacing: 1px;")
        
        # Área de Texto (Terminal)
        self.txtMensajeEncriptado = QtWidgets.QTextEdit(parent=self.centralwidget)
        # Ajustamos altura: Empieza en 190 y termina dejando espacio para botones abajo
        self.txtMensajeEncriptado.setGeometry(QtCore.QRect(50, 190, 800, 380))
        self.txtMensajeEncriptado.setReadOnly(True)
        self.txtMensajeEncriptado.setStyleSheet("""
            QTextEdit {
                background-color: #0F172A;
                border: 2px solid #1E293B;
                border-radius: 15px;
                padding: 15px;
                color: #94A3B8; /* Gris al principio */
                font-family: 'Consolas', monospace;
                font-size: 14px;
            }
            QTextEdit:focus {
                border: 2px solid #06B6D4;
                background-color: #020617;
            }
        """)
        
        # Sombra
        shadow_txt = QGraphicsDropShadowEffect(self.txtMensajeEncriptado)
        shadow_txt.setBlurRadius(20)
        shadow_txt.setColor(QColor(6, 182, 212, 40))
        self.txtMensajeEncriptado.setGraphicsEffect(shadow_txt)

        # ====================================================================
        # 4. BOTONERA HORIZONTAL (ABAJO)
        # ====================================================================
        self.panel_botones = QtWidgets.QFrame(parent=self.centralwidget)
        self.panel_botones.setGeometry(QtCore.QRect(50, 600, 800, 70))
        self.panel_botones.setStyleSheet("background: transparent;")
        
        # --- ESTILOS ---
        style_btn = """
            QPushButton {
                background-color: #1E293B;
                color: white;
                border-radius: 10px;
                font-weight: bold;
                font-family: 'Segoe UI';
                font-size: 14px;
                border: 1px solid #334155;
            }
            QPushButton:hover { margin-top: -2px; }
        """
        
        # Estilo Desencriptar (Verde Principal)
        style_unlock = style_btn + """
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #10B981, stop:1 #06B6D4);
                border: none;
                font-size: 15px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #34D399, stop:1 #22D3EE);
            }
        """

        # Estilo Descargar (Cian)
        style_save = style_btn + """
            QPushButton {
                border: 2px solid #06B6D4;
                color: #22D3EE;
            }
            QPushButton:hover { background-color: rgba(6, 182, 212, 0.1); color: white; }
        """
        
        # Estilo Regresar (Simple)
        style_back = style_btn + """
            QPushButton {
                border: 1px dashed #64748B;
                color: #94A3B8;
            }
            QPushButton:hover { border-color: #EF4444; color: #EF4444; }
        """

        # --- BOTONES ---
        # 1. Desencriptar (Grande a la izquierda)
        self.btnDesencriptar = QtWidgets.QPushButton(parent=self.panel_botones)
        self.btnDesencriptar.setGeometry(QtCore.QRect(0, 0, 300, 60))
        self.btnDesencriptar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnDesencriptar.setStyleSheet(style_unlock)

        # 2. Descargar (Centro)
        self.btnDescargar = QtWidgets.QPushButton(parent=self.panel_botones)
        self.btnDescargar.setGeometry(QtCore.QRect(320, 0, 200, 60))
        self.btnDescargar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnDescargar.setStyleSheet(style_save)

        # 3. Regresar (Derecha)
        self.btnRegresar = QtWidgets.QPushButton(parent=self.panel_botones)
        self.btnRegresar.setGeometry(QtCore.QRect(600, 0, 200, 60))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Secure Nexus - Recuperación"))
        self.label.setText(_translate("MainWindow", "CONTENIDO SEGURO >"))
        self.btnCargarArchivo.setText(_translate("MainWindow", "📂  SELECCIONAR ARCHIVO CIFRADO (.txt / .enc)"))
        
        # Textos de la terminal
        self.txtMensajeEncriptado.setPlaceholderText(_translate("MainWindow", "// Esperando archivo para procesar..."))
        
        # Botones
        self.btnDesencriptar.setText(_translate("MainWindow", "🔓  DESENCRIPTAR AHORA"))
        self.btnDescargar.setText(_translate("MainWindow", "💾  GUARDAR RESULTADO"))
        self.btnRegresar.setText(_translate("MainWindow", "← VOLVER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())