import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, 
                             QPushButton, QFrame, QHBoxLayout, QGraphicsDropShadowEffect)
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QColor

class EmailDialog(QDialog):
    def __init__(self, parent=None, archivos_memoria=None):
        super().__init__(parent)
        self.archivos_memoria = archivos_memoria if archivos_memoria else []
        
        # 1. Configuración de la Ventana (Transparente y sin bordes)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.resize(400, 520)
        
        # 2. Centrar automáticamente
        if parent:
            geo_parent = parent.geometry()
            geo_self = self.geometry()
            center_point = geo_parent.center() - geo_self.center()
            self.move(parent.mapToGlobal(QPoint(0,0)) + center_point)

        self.init_ui()

    def init_ui(self):
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(10, 10, 10, 10)

        # --- FRAME PRINCIPAL ---
        self.frame = QFrame()
        self.frame.setObjectName("MainFrame")
        self.frame.setStyleSheet("""
            QFrame#MainFrame {
                background-color: #FFFFFF;
                border-radius: 20px;
                border: 1px solid #BDC3C7;
            }
            QLabel {
                color: #2C3E50;
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
                font-weight: 500;
            }
            QLineEdit {
                background-color: #ECF0F1;
                border: 2px solid transparent;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
                color: #2C3E50;
            }
            QLineEdit:focus {
                background-color: #FFFFFF;
                border: 2px solid #3498DB;
            }
        """)
        
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(5)
        shadow.setColor(QColor(0, 0, 0, 60))
        self.frame.setGraphicsEffect(shadow)
        
        layout_principal.addWidget(self.frame)
        
        # --- CONTENIDO ---
        layout_content = QVBoxLayout(self.frame)
        layout_content.setSpacing(15)
        layout_content.setContentsMargins(25, 30, 25, 30)

        # Título
        lbl_titulo = QLabel("🔐 Enviar Datos Seguros")
        lbl_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_titulo.setStyleSheet("font-size: 22px; font-weight: bold; color: #2980B9; margin-bottom: 10px;")
        layout_content.addWidget(lbl_titulo)

        # Campos
        self.txt_remitente = QLineEdit("230733@utxicotepec.edu.mx")
        self.txt_remitente.setPlaceholderText("Tu correo institucional")
        self.txt_remitente.setReadOnly(True)
        self.txt_remitente.setStyleSheet("color: #7F8C8D; background-color: #F5F6FA;")
        layout_content.addWidget(self.crear_label("De (Remitente):"))
        layout_content.addWidget(self.txt_remitente)

        self.txt_app_pass = QLineEdit()
        self.txt_app_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.txt_app_pass.setPlaceholderText("Pega aquí tu clave de 16 letras")
        layout_content.addWidget(self.crear_label("Contraseña de Aplicación (Gmail):"))
        layout_content.addWidget(self.txt_app_pass)

        self.txt_destinatario = QLineEdit()
        self.txt_destinatario.setPlaceholderText("ejemplo@gmail.com")
        layout_content.addWidget(self.crear_label("Para (Destinatario):"))
        layout_content.addWidget(self.txt_destinatario)

        # Botones
        layout_btns = QHBoxLayout()
        layout_btns.setSpacing(15)
        layout_btns.setContentsMargins(0, 10, 0, 0)

        btn_cancel = QPushButton("Cancelar")
        btn_cancel.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_cancel.clicked.connect(self.reject)
        btn_cancel.setStyleSheet("""
            QPushButton {
                background-color: #E74C3C; color: white; border-radius: 10px; padding: 12px; font-weight: bold; font-size: 14px;
            }
            QPushButton:hover { background-color: #C0392B; }
        """)

        self.btn_enviar = QPushButton("📤 Enviar Ahora") # Lo guardamos en self para referencia si hace falta
        self.btn_enviar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_enviar.clicked.connect(self.validar_y_enviar)
        self.btn_enviar.setStyleSheet("""
            QPushButton {
                background-color: #2ECC71; color: white; border-radius: 10px; padding: 12px; font-weight: bold; font-size: 14px;
            }
            QPushButton:hover { background-color: #27AE60; }
        """)

        layout_btns.addWidget(btn_cancel)
        layout_btns.addWidget(self.btn_enviar)
        layout_content.addLayout(layout_btns)

        # ====================================================================
        # NUEVO: SOPORTE PARA TECLA ENTER
        # ====================================================================
        # Si estás en el campo de contraseña y das Enter -> Envia
        self.txt_app_pass.returnPressed.connect(self.validar_y_enviar)
        # Si estás en el campo destinatario y das Enter -> Envia
        self.txt_destinatario.returnPressed.connect(self.validar_y_enviar)

    def crear_label(self, texto):
        lbl = QLabel(texto)
        lbl.setStyleSheet("margin-bottom: 2px; margin-left: 5px; font-size: 13px; color: #555;")
        return lbl

    def validar_y_enviar(self):
        remitente = self.txt_remitente.text().strip()
        password = self.txt_app_pass.text().strip()
        destinatario = self.txt_destinatario.text().strip()

        if not all([remitente, password, destinatario]):
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Faltan Datos", "Por favor llena todos los campos.")
            return

        try:
            # Deshabilitar botón para evitar doble clic
            self.btn_enviar.setText("Enviando...")
            self.btn_enviar.setEnabled(False)
            self.repaint() # Forzar actualización visual

            self.enviar_gmail(remitente, password, destinatario)
            
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.information(self, "¡Enviado!", "✅ El correo se envió correctamente.")
            self.accept()
        except Exception as e:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.critical(self, "Error", f"❌ No se pudo enviar.\n\nError: {str(e)}")
            self.btn_enviar.setText("📤 Enviar Ahora")
            self.btn_enviar.setEnabled(True)

    def enviar_gmail(self, remitente, password, destinatario):
        msg = MIMEMultipart()
        msg['From'] = remitente
        msg['To'] = destinatario
        msg['Subject'] = "🔐 Datos Encriptados (App Seguridad)"

        cuerpo = """
        <div style="font-family: Arial, sans-serif; color: #333;">
            <h2 style="color: #2980B9;">🔐 Archivos de Seguridad</h2>
            <p>Hola,</p>
            <p>Adjunto encontrarás los archivos generados por tu aplicación de seguridad:</p>
            <ul>
                <li><b>Mensaje Encriptado</b> (.txt)</li>
                <li><b>Llave de Acceso</b> (.key)</li>
            </ul>
            <p style="font-size: 12px; color: #777;">Este es un mensaje automático.</p>
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