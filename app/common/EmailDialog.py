"""
Diálogo de Envío de Correo (Sleek Cyber Edition - Centrado Perfecto)
====================================================================
Interfaz moderna y oscura para el envío de credenciales.
Se posiciona automáticamente en el centro de la ventana principal.

Autor: [Marcos Jesús Ríos Durán]
Fecha: 14/12/2025
Versión: 2.1.0 (Cyber Center)
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, 
                             QPushButton, QFrame, QHBoxLayout, QGraphicsDropShadowEffect)
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QColor, QCursor

class EmailDialog(QDialog):
    def __init__(self, parent=None, archivos_memoria=None):
        super().__init__(parent)
        self.archivos_memoria = archivos_memoria if archivos_memoria else []
        
        # 1. Configuración de la Ventana
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.resize(450, 580)
        
        # Inicializamos la interfaz
        self.init_ui()

        # 2. CENTRADO PERFECTO SOBRE LA APP
        # Lo ejecutamos aquí para asegurar que la ventana ya tiene tamaño
        if parent:
            self.centrar_en_ventana_padre(parent)

    def centrar_en_ventana_padre(self, parent):
        """Calcula el centro geométrico respecto a la ventana principal"""
        # Obtenemos la geometría (posición y tamaño) de la ventana padre
        parent_geo = parent.frameGeometry()
        self_geo = self.frameGeometry()
        
        # Calculamos el centro
        center_point = parent_geo.center()
        
        # Movemos el centro de nuestra geometría al centro del padre
        self_geo.moveCenter(center_point)
        
        # Movemos la ventana a esa posición calculada
        self.move(self_geo.topLeft())

    def init_ui(self):
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(10, 10, 10, 10)

        # --- FRAME PRINCIPAL (TARJETA CYBER) ---
        self.frame = QFrame()
        self.frame.setObjectName("MainFrame")
        self.frame.setStyleSheet("""
            QFrame#MainFrame {
                background-color: rgba(15, 23, 42, 0.98); /* Fondo casi negro opaco */
                border-radius: 20px;
                border: 2px solid #10B981; /* Borde Verde Neón */
            }
            QLabel {
                color: #E2E8F0; /* Texto claro */
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
                font-weight: bold;
            }
            QLineEdit {
                background-color: #1E293B; /* Fondo input oscuro */
                border: 2px solid #334155;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
                color: #22D3EE; /* Texto Cian estilo terminal */
                font-family: 'Consolas', monospace;
            }
            QLineEdit:focus {
                background-color: #0F172A;
                border: 2px solid #10B981; /* Foco Verde */
            }
            QLineEdit::placeholder { color: #64748B; }
        """)
        
        # Sombra Neón
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(16, 185, 129, 60)) # Resplandor verde
        self.frame.setGraphicsEffect(shadow)
        
        layout_principal.addWidget(self.frame)
        
        # --- CONTENIDO ---
        layout_content = QVBoxLayout(self.frame)
        layout_content.setSpacing(15)
        layout_content.setContentsMargins(30, 30, 30, 30)

        # Título
        lbl_titulo = QLabel("📡 TRANSMISIÓN SEGURA")
        lbl_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_titulo.setStyleSheet("""
            font-family: 'Segoe UI Black';
            font-size: 20px; 
            color: #F0FDF4; 
            letter-spacing: 1px;
            margin-bottom: 10px;
        """)
        layout_content.addWidget(lbl_titulo)

        # 1. Remitente (Editable)
        self.txt_remitente = QLineEdit()
        self.txt_remitente.setPlaceholderText("Tu correo (Gmail)...")
        layout_content.addWidget(self.crear_label("DE (Tu Correo Gmail):"))
        layout_content.addWidget(self.txt_remitente)

        # 2. Contraseña de Aplicación
        self.txt_app_pass = QLineEdit()
        self.txt_app_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.txt_app_pass.setPlaceholderText("•••• •••• •••• ••••")
        layout_content.addWidget(self.crear_label("CLAVE DE APLICACIÓN:"))
        layout_content.addWidget(self.txt_app_pass)

        # 3. Destinatario
        self.txt_destinatario = QLineEdit()
        self.txt_destinatario.setPlaceholderText("destinatario@ejemplo.com")
        layout_content.addWidget(self.crear_label("PARA (Destinatario):"))
        layout_content.addWidget(self.txt_destinatario)

        # Botones
        layout_btns = QHBoxLayout()
        layout_btns.setSpacing(15)
        layout_btns.setContentsMargins(0, 15, 0, 0)

        # Botón Cancelar (Estilo Alerta)
        btn_cancel = QPushButton("ABORTAR")
        btn_cancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn_cancel.clicked.connect(self.reject)
        btn_cancel.setStyleSheet("""
            QPushButton {
                background-color: transparent; 
                color: #94A3B8; 
                border: 2px solid #334155;
                border-radius: 10px; 
                padding: 12px; 
                font-weight: bold; 
                font-family: 'Segoe UI';
            }
            QPushButton:hover { 
                color: #EF4444; 
                border-color: #EF4444; 
                background-color: rgba(239, 68, 68, 0.1);
            }
        """)

        # Botón Enviar (Estilo Acción Verde)
        self.btn_enviar = QPushButton("ENVIAR DATOS 🚀")
        self.btn_enviar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_enviar.clicked.connect(self.validar_y_enviar)
        self.btn_enviar.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #10B981, stop:1 #06B6D4);
                color: white; 
                border: none;
                border-radius: 10px; 
                padding: 12px; 
                font-weight: bold; 
                font-family: 'Segoe UI Black';
            }
            QPushButton:hover { 
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #34D399, stop:1 #22D3EE);
            }
        """)

        layout_btns.addWidget(btn_cancel)
        layout_btns.addWidget(self.btn_enviar)
        layout_content.addLayout(layout_btns)

        # Soporte para Enter
        self.txt_app_pass.returnPressed.connect(self.validar_y_enviar)
        self.txt_destinatario.returnPressed.connect(self.validar_y_enviar)

    def crear_label(self, texto):
        lbl = QLabel(texto)
        lbl.setStyleSheet("color: #34D399; font-size: 11px; margin-bottom: 2px; margin-left: 2px;")
        return lbl

    def validar_y_enviar(self):
        remitente = self.txt_remitente.text().strip()
        password = self.txt_app_pass.text().strip()
        destinatario = self.txt_destinatario.text().strip()

        if not all([remitente, password, destinatario]):
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Datos Incompletos", "⚠️ Faltan campos requeridos para la transmisión.")
            return

        try:
            # UI Feedback
            self.btn_enviar.setText("TRANSMITIENDO...")
            self.btn_enviar.setEnabled(False)
            self.repaint()

            self.enviar_gmail(remitente, password, destinatario)
            
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.information(self, "Éxito", "✅ Paquete de datos enviado correctamente.")
            self.accept()
        except Exception as e:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.critical(self, "Fallo de Envío", f"❌ Error en la transmisión:\n\n{str(e)}")
            self.btn_enviar.setText("REINTENTAR ENVÍO 🚀")
            self.btn_enviar.setEnabled(True)

    def enviar_gmail(self, remitente, password, destinatario):
        msg = MIMEMultipart()
        msg['From'] = remitente
        msg['To'] = destinatario
        msg['Subject'] = "🔐 Secure Nexus: Datos Encriptados"

        cuerpo = """
        <div style="font-family: 'Courier New', monospace; color: #333; background-color: #f4f4f4; padding: 20px;">
            <h2 style="color: #06B6D4;">[ SECURE NEXUS REPORT ]</h2>
            <p><strong>Estado:</strong> Transmisión Exitosa</p>
            <p>Se adjuntan las credenciales y archivos generados por el sistema.</p>
            <hr>
            <ul>
                <li>📄 <b>Mensaje Seguro</b> (.txt)</li>
                <li>🔑 <b>Llave Maestra</b> (.key)</li>
            </ul>
            <p style="font-size: 10px; color: #777;">Generado automáticamente por Secure Nexus v2.0</p>
        </div>
        """
        msg.attach(MIMEText(cuerpo, 'html'))

        for archivo in self.archivos_memoria:
            nombre = archivo['nombre']
            contenido_bytes = archivo['contenido']
            part = MIMEApplication(contenido_bytes, Name=nombre)
            part['Content-Disposition'] = f'attachment; filename="{nombre}"'
            msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remitente, password)
        server.send_message(msg)
        server.quit()