"""
Módulo de Interfaz de Usuario - Pantalla de Login (Sleek Cyber Edition - Hover Fix)
===================================================================================

Diseño "Cyberpunk Elegante" para Antonio.
Ajustes de UX:
- Hover SALIR -> Rojo (Alerta)
- Hover AUTORIZAR -> Azul (Acción)

Autor: [Marcos Jesús Ríos Durán]
Fecha: 14/12/2025
Versión: 5.1.0 (Sleek Cyber Hover)
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
        MainWindow.resize(700, 600) 
        
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
        # 2. TARJETA CENTRAL
        # ====================================================================
        self.card_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.card_frame.setGeometry(QtCore.QRect(100, 50, 500, 500))
        self.card_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(30, 41, 59, 0.90);
                border-radius: 25px;
                border: 1px solid #10B981;
            }
        """)
        
        shadow = QGraphicsDropShadowEffect(self.card_frame)
        shadow.setBlurRadius(50)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(16, 185, 129, 70))
        self.card_frame.setGraphicsEffect(shadow)

        # ====================================================================
        # 3. ENCABEZADO
        # ====================================================================
        
        # LOGO
        self.logo_bg = QtWidgets.QLabel(parent=self.card_frame)
        self.logo_bg.setGeometry(QtCore.QRect(190, 40, 120, 120))
        self.logo_bg.setText("🛡️")
        self.logo_bg.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.logo_bg.setStyleSheet("""
            QLabel {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #0F172A, stop:1 #10B981);
                color: #ECFDF5;
                border-radius: 60px;
                font-size: 65px;
                border: 2px solid #34D399;
            }
        """)

        # TÍTULO
        self.lbl_titulo = QtWidgets.QLabel(parent=self.card_frame)
        self.lbl_titulo.setGeometry(QtCore.QRect(50, 180, 400, 40))
        self.lbl_titulo.setText("ACCESO AL SISTEMA")
        self.lbl_titulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_titulo.setStyleSheet("""
            font-family: 'Segoe UI Black', 'Roboto', sans-serif;
            font-size: 28px;
            font-weight: 800;
            color: #F0FDF4;
            letter-spacing: 3px;
        """)

        # ====================================================================
        # 4. INPUTS
        # ====================================================================
        style_input = """
            QLineEdit {
                background-color: #1E293B;
                border: 2px solid #334155;
                border-radius: 12px;
                padding: 0 20px;
                font-family: 'Segoe UI', sans-serif;
                font-size: 15px;
                color: #E2E8F0;
            }
            QLineEdit:focus {
                border: 2px solid #34D399;
                background-color: #0F172A;
            }
            QLineEdit::placeholder { color: #64748B; font-style: italic; }
        """

        # USUARIO
        self.label_user = QtWidgets.QLabel(parent=self.card_frame)
        self.label_user.setGeometry(QtCore.QRect(50, 240, 400, 20))
        self.label_user.setText("IDENTIFICADOR")
        self.label_user.setStyleSheet("color: #34D399; font-size: 12px; font-weight: bold; letter-spacing: 1px;")

        self.lvluser = QtWidgets.QLineEdit(parent=self.card_frame)
        self.lvluser.setGeometry(QtCore.QRect(50, 265, 400, 50))
        self.lvluser.setPlaceholderText("Ingrese su ID de usuario")
        self.lvluser.setStyleSheet(style_input)

        # CONTRASEÑA
        self.label_pass = QtWidgets.QLabel(parent=self.card_frame)
        self.label_pass.setGeometry(QtCore.QRect(50, 335, 400, 20))
        self.label_pass.setText("CLAVE DE SEGURIDAD")
        self.label_pass.setStyleSheet("color: #34D399; font-size: 12px; font-weight: bold; letter-spacing: 1px;")

        self.lvlpassword = QtWidgets.QLineEdit(parent=self.card_frame)
        self.lvlpassword.setGeometry(QtCore.QRect(50, 360, 400, 50))
        self.lvlpassword.setPlaceholderText("••••••••••••")
        self.lvlpassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lvlpassword.setStyleSheet(style_input)

        # ====================================================================
        # 5. BOTONES (Con Hover Mejorado)
        # ====================================================================
        
        # Botón AUTORIZAR (Verde -> Azul al pasar mouse)
        self.lvlacept = QtWidgets.QPushButton(parent=self.card_frame)
        self.lvlacept.setGeometry(QtCore.QRect(260, 440, 190, 50)) 
        self.lvlacept.setText("AUTORIZAR ACCESO")
        self.lvlacept.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.lvlacept.setStyleSheet("""
            QPushButton {
                /* Estado Normal: Gradiente Verde */
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #10B981, stop:1 #06B6D4);
                color: white;
                border: none;
                border-radius: 12px;
                font-weight: 800;
                font-family: 'Segoe UI Black';
                font-size: 14px;
                letter-spacing: 1px;
            }
            QPushButton:hover {
                /* HOVER AZUL: Gradiente de Azul a Cian */
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #2563EB, stop:1 #06B6D4);
                border: 2px solid #3B82F6; /* Borde azul brillante */
            }
            QPushButton:pressed { background-color: #1E40AF; }
        """)

        # Botón SALIR (Gris -> Rojo al pasar mouse)
        self.lvlcancel = QtWidgets.QPushButton(parent=self.card_frame)
        self.lvlcancel.setGeometry(QtCore.QRect(50, 440, 190, 50))
        self.lvlcancel.setText("SALIR")
        self.lvlcancel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.lvlcancel.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #94A3B8;
                border: 2px solid #334155;
                border-radius: 12px;
                font-weight: bold;
                font-family: 'Segoe UI';
                font-size: 14px;
            }
            QPushButton:hover {
                /* HOVER ROJO: Texto rojo, borde rojo y fondo rojizo */
                color: #EF4444; 
                border: 2px solid #EF4444;
                background-color: rgba(239, 68, 68, 0.1);
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Secure Access - Antonio"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())