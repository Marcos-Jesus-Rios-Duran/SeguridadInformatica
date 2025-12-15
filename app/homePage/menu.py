"""
Ventana del Menú Principal - Backend (Sleek Cyber Duo)
======================================================

Diseño "Centro de Comando" simplificado a dos opciones principales.
Eliminado el botón de email para mayor coherencia lógica.

Autor: [Marcos Jesús Ríos Durán]
Fecha: 14/12/2025
Versión: 2.1.0 (Cyber Duo)
"""

import sys 
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                             QGraphicsDropShadowEffect, QWidget)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QColor, QCursor

# Importamos el Navbar reutilizable
from common.MenuBarComponent import MenuBarComponent

class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # ====================================================================
        # 1. CONFIGURACIÓN GENERAL
        # ====================================================================
        self.setWindowTitle("Centro de Comando - Secure Nexus")
        self.resize(900, 700)
        
        # Fondo degradado profundo
        self.setStyleSheet("""
            QMainWindow {
                background: qradialgradient(
                    cx:0.5, cy:0.5, radius: 1.0,
                    fx:0.5, fy:0.5,
                    stop:0 #0F172A,
                    stop:1 #020617
                );
            }
        """)
        
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        
        # ====================================================================
        # 2. NAVBAR REUTILIZABLE
        # ====================================================================
        self.menubar_component = MenuBarComponent(self)
        menubar = self.menubar_component.setup_menubar()
        
        # Estilo coherente con el componente
        menubar.setStyleSheet("""
            QMenuBar {
                background-color: #1E293B;
                color: #E2E8F0;
                border-bottom: 2px solid #10B981;
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
            }
            QMenuBar::item {
                background-color: transparent;
                padding: 8px 15px;
            }
            QMenuBar::item:selected {
                background-color: #10B981;
                color: white;
            }
        """)
        self.setMenuBar(menubar)
        
        # ====================================================================
        # 3. DASHBOARD
        # ====================================================================
        self.setup_cyber_dashboard()

    def setup_cyber_dashboard(self):
        # TÍTULO PRINCIPAL
        self.lbl_titulo = QLabel(self.centralwidget)
        self.lbl_titulo.setGeometry(0, 50, 900, 50)
        self.lbl_titulo.setText("CENTRO DE OPERACIONES")
        self.lbl_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_titulo.setStyleSheet("""
            font-family: 'Segoe UI Black', sans-serif;
            font-size: 34px;
            font-weight: 800;
            color: #F0FDF4;
            letter-spacing: 4px;
        """)

        self.lbl_sub = QLabel(self.centralwidget)
        self.lbl_sub.setGeometry(0, 100, 900, 30)
        self.lbl_sub.setText("Seleccione un protocolo de seguridad")
        self.lbl_sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_sub.setStyleSheet("color: #34D399; font-size: 15px; font-weight: bold;")

        # ====================================================================
        # TARJETAS DUO (2 COLUMNAS)
        # ====================================================================
        # Ancho ventana: 900
        # Margen izquierdo: 100
        # Espacio central: 60
        # Ancho botón: 320
        # X1 = 100
        # X2 = 100 + 320 + 60 = 480
        
        # --- CARD 1: ENCRIPTAR (Izquierda) ---
        self.btn_encriptar = QPushButton(self.centralwidget)
        self.btn_encriptar.setGeometry(100, 170, 320, 380) # Más anchos
        self.btn_encriptar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_encriptar.setText("🔒\n\nENCRIPTAR\nDATOS\n\n[ Proteger Archivo ]")
        self.btn_encriptar.clicked.connect(self.ir_a_encriptar)
        
        self.btn_encriptar.setStyleSheet("""
            QPushButton {
                background-color: rgba(30, 41, 59, 0.6);
                border: 2px solid #10B981; /* Borde Esmeralda */
                border-radius: 25px;
                color: #ECFDF5;
                font-family: 'Segoe UI Black';
                font-size: 20px;
                padding: 20px;
            }
            QPushButton:hover {
                background-color: rgba(16, 185, 129, 0.15);
                border: 3px solid #34D399; /* Borde más grueso al hover */
                color: #34D399;
                margin-top: -10px; /* Elevación */
            }
        """)
        self.add_shadow(self.btn_encriptar, "#10B981")

        # --- CARD 2: DESENCRIPTAR (Derecha) ---
        self.btn_desencriptar = QPushButton(self.centralwidget)
        self.btn_desencriptar.setGeometry(480, 170, 320, 380) # Más anchos
        self.btn_desencriptar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_desencriptar.setText("🔓\n\nDESENCRIPTAR\nACCESO\n\n[ Leer Archivo ]")
        self.btn_desencriptar.clicked.connect(self.ir_a_desencriptar)
        
        self.btn_desencriptar.setStyleSheet("""
            QPushButton {
                background-color: rgba(30, 41, 59, 0.6);
                border: 2px solid #06B6D4; /* Borde Cian */
                border-radius: 25px;
                color: #ECFDF5;
                font-family: 'Segoe UI Black';
                font-size: 20px;
                padding: 20px;
            }
            QPushButton:hover {
                background-color: rgba(6, 182, 212, 0.15);
                border: 3px solid #22D3EE;
                color: #22D3EE;
                margin-top: -10px;
            }
        """)
        self.add_shadow(self.btn_desencriptar, "#06B6D4")

        # PIE DE PÁGINA
        self.lbl_footer = QLabel(self.centralwidget)
        self.lbl_footer.setGeometry(0, 650, 900, 30)
        self.lbl_footer.setText("SISTEMA SEGURO v2.1 - ACCESO AUTORIZADO")
        self.lbl_footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_footer.setStyleSheet("color: #475569; font-size: 11px; font-family: 'Consolas';")

    def add_shadow(self, widget, color_hex):
        """Agrega resplandor"""
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(40)
        shadow.setColor(QColor(color_hex))
        shadow.setOffset(0, 0)
        widget.setGraphicsEffect(shadow)

    # ========================================================================
    # NAVEGACIÓN
    # ========================================================================

    def ir_a_encriptar(self):
        from encriptacion.controller.encriptarLogic import EncriptarLogic
        self.window = EncriptarLogic()
        self.window.show()
        self.close()

    def ir_a_desencriptar(self):
        from desencriptacion.controller.desencriptarLogic import DesencriptarLogic
        self.window = DesencriptarLogic()
        self.window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuWindow()
    window.show()
    sys.exit(app.exec())