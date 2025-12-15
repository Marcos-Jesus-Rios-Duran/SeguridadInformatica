"""
Módulo de Interfaz de Usuario - Pantalla de Login (Cyber Spaced Edition)
========================================================================

Diseño "Dark Cyber" con espaciado mejorado y distribución limpia.
Ajustado para dar mayor legibilidad y "aire" a los elementos.

Autor: [Marcos Jesús Ríos Durán]
Fecha: 08/12/2025
Versión: 3.1.0 (Cyber Spaced)
"""

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor, QFont

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # ====================================================================
        # 1. CONFIGURACIÓN GENERAL
        # ====================================================================
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 650) # Ventana un poco más grande
        
        # Fondo degradado Radial Cyber
        MainWindow.setStyleSheet("""
            QMainWindow {
                background: qradialgradient(
                    cx:0.5, cy:0.5, radius: 0.8,
                    fx:0.5, fy:0.5,
                    stop:0 #1E293B,
                    stop:1 #0F172A
                );
            }
        """)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ====================================================================
        # 2. TARJETA CENTRAL (Más alta y espaciosa)
        # ====================================================================
        self.card_frame = QtWidgets.QFrame(parent=self.centralwidget)
        # Centramos la tarjeta: (520-400)/2 = 60 en X
        self.card_frame.setGeometry(QtCore.QRect(60, 40, 400, 560)) 
        self.card_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(30, 41, 59, 0.95);
                border-radius: 25px;
                border: 2px solid #06B6D4;
            }
        """)
        
        # Sombra Neón
        shadow = QGraphicsDropShadowEffect(self.card_frame)
        shadow.setBlurRadius(40)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(6, 182, 212, 60))
        self.card_frame.setGraphicsEffect(shadow)

        # ====================================================================
        # 3. ENCABEZADO (Logo y Títulos)
        # ====================================================================
        
        # LOGO
        self.logo_bg = QtWidgets.QLabel(parent=self.card_frame)
        self.logo_bg.setGeometry(QtCore.QRect(135, 40, 130, 130))
        self.logo_bg.setText("🛡️")
        self.logo_bg.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.logo_bg.setStyleSheet("""
            QLabel {
                background-color: #0F172A;
                color: #22D3EE;
                border-radius: 65px;
                font-size: 70px;
                border: 3px solid #22D3EE;
            }
        """)

        # TÍTULO (Bajamos un poco para separar del logo)
        self.lbl_titulo = QtWidgets.QLabel(parent=self.card_frame)
        self.lbl_titulo.setGeometry(QtCore.QRect(50, 190, 300, 35))
        self.lbl_titulo.setText("ACCESO SEGURO")
        self.lbl_titulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_titulo.setStyleSheet("""
            font-family: 'Segoe UI Black', sans-serif;
            font-size: 26px;
            font-weight: bold;
            color: #F1F5F9;
            letter-spacing: 1px;
        """)
        
        # SUBTÍTULO
        self.lbl_subtitulo = QtWidgets.QLabel(parent=self.card_frame)
        self.lbl_subtitulo.setGeometry(QtCore.QRect(50, 225, 300, 20))
        self.lbl_subtitulo.setText("Terminal de Ciberseguridad v1.1")
        self.lbl_subtitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_subtitulo.setStyleSheet("color: #06B6D4; font-size: 12px; font-weight: bold;")

        # ====================================================================
        # 4. INPUTS (Con más aire entre ellos)
        # ====================================================================
        style_input = """
            QLineEdit {
                background-color: #334155;
                border: 2px solid #475569;
                border-radius: 12px;
                padding: 0 15px;
                font-family: 'Segoe UI';
                font-size: 14px;
                color: #E2E8F0;
            }
            QLineEdit:focus {
                border: 2px solid #22D3EE;
                background-color: #1E293B;
            }
        """

        # --- USUARIO ---
        # Etiqueta (Y=270)
        self.label_user = QtWidgets.QLabel(parent=self.card_frame)
        self.label_user.setGeometry(QtCore.QRect(50, 270, 300, 20))
        self.label_user.setText("IDENTIFICADOR DE USUARIO")
        self.label_user.setStyleSheet("color: #94A3B8; font-size: 11px; font-weight: bold; letter-spacing: 0.8px;")

        # Input (Y=295)
        self.lvluser = QtWidgets.QLineEdit(parent=self.card_frame)
        self.lvluser.setGeometry(QtCore.QRect(50, 295, 300, 45))
        self.lvluser.setPlaceholderText("Usuario...")
        self.lvluser.setStyleSheet(style_input)


        # --- CONTRASEÑA ---
        # Aumentamos el espacio aquí (De 295+45=340, saltamos a 365)
        # Etiqueta (Y=365)
        self.label_pass = QtWidgets.QLabel(parent=self.card_frame)
        self.label_pass.setGeometry(QtCore.QRect(50, 365, 300, 20))
        self.label_pass.setText("CLAVE DE ACCESO")
        self.label_pass.setStyleSheet("color: #94A3B8; font-size: 11px; font-weight: bold; letter-spacing: 0.8px;")

        # Input (Y=390) - ¡OJO AQUÍ PARA TU BOTÓN DEL OJITO!
        self.lvlpassword = QtWidgets.QLineEdit(parent=self.card_frame)
        self.lvlpassword.setGeometry(QtCore.QRect(50, 390, 300, 45))
        self.lvlpassword.setPlaceholderText("••••••••••••")
        self.lvlpassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lvlpassword.setStyleSheet(style_input)

        # ====================================================================
        # 5. BOTONES (Abajo con buen margen)
        # ====================================================================
        
        # Botón INGRESAR (Y=480)
        self.lvlacept = QtWidgets.QPushButton(parent=self.card_frame)
        self.lvlacept.setGeometry(QtCore.QRect(210, 480, 140, 50)) # Un poco más altos (50px)
        self.lvlacept.setText("AUTORIZAR ⚡")
        self.lvlacept.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.lvlacept.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #06B6D4, stop:1 #3B82F6);
                color: white;
                border: none;
                border-radius: 12px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #22D3EE, stop:1 #60A5FA);
            }
            QPushButton:pressed { background-color: #0E7490; }
        """)

        # Botón SALIR (Y=480)
        self.lvlcancel = QtWidgets.QPushButton(parent=self.card_frame)
        self.lvlcancel.setGeometry(QtCore.QRect(50, 480, 140, 50))
        self.lvlcancel.setText("CANCELAR ✕")
        self.lvlcancel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.lvlcancel.setStyleSheet("""
            QPushButton {
                background-color: #1E293B;
                color: #94A3B8;
                border: 2px solid #334155;
                border-radius: 12px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                color: #EF4444; border: 2px solid #EF4444; background-color: #331E1E;
            }
        """)

        # ====================================================================
        # COMPATIBILIDAD
        # ====================================================================
        self.label_4 = self.label_pass
        self.label_5 = self.label_user
        self.label = self.logo_bg

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Security System - Access"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())