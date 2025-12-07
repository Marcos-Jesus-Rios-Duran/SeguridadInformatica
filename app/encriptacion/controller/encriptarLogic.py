"""
Lógica de Encriptación
======================
Archivo: app/encriptacion/controller/encriptarLogic.py
"""

import sys
from PyQt6.QtWidgets import QApplication, QMessageBox

# 1. IMPORTAR VISTA Y COMPONENTES
from encriptacion.views.EncriptarWindow import EncriptarWindowUI
from common.FileHelper import FileHelper
# 2. IMPORTAR TU HERRAMIENTA DE ENCRIPTACIÓN
from encriptacion.tools.AesCipher import AesCipher

class EncriptarLogic(EncriptarWindowUI):
    def __init__(self):
        super().__init__()
        self.inicializar_logica()
        
        # Variable para guardar el objeto cifrador temporalmente
        self.cifrador = None 
        self.mensaje_encriptado_bytes = None

    def inicializar_logica(self):
        self.ui.btnEncriptar.clicked.connect(self.encriptar_mensaje)
        self.ui.btnDescargar.clicked.connect(self.descargar_archivos) # Ojo: cambié el nombre
        self.ui.btnEnviar.clicked.connect(self.enviar_mensaje)
        self.ui.btnRegresar.clicked.connect(self.regresar_menu)
        self.ui.btnCargar.clicked.connect(self.cargar_archivo_txt)

    # ========================================================================
    # LÓGICA DE NEGOCIO
    # ========================================================================

    def cargar_archivo_txt(self):
        contenido = FileHelper.abrir_archivo(self)
        if contenido is not None:
            self.ui.txtMensaje.setText(contenido)

    def encriptar_mensaje(self):
        """
        Toma el texto, crea una llave nueva y lo encripta.
        """
        mensaje_plano = self.ui.txtMensaje.toPlainText()
        
        if not mensaje_plano:
            QMessageBox.warning(self, "Advertencia", "El campo de texto está vacío.")
            return

        # 1. Instanciar la herramienta (Esto genera una LLAVE NUEVA automáticamente)
        self.cifrador = AesCipher()
        
        # 2. Encriptar
        # El resultado son bytes, así que para mostrarlo en pantalla lo convertimos a string
        self.mensaje_encriptado_bytes = self.cifrador.encriptar(mensaje_plano)
        mensaje_encriptado_str = self.mensaje_encriptado_bytes.decode('utf-8')
        
        # 3. Mostrar el resultado en la pantalla (visual solamente)
        self.ui.txtMensaje.setText(mensaje_encriptado_str)
        
        QMessageBox.information(self, "Éxito", "Mensaje encriptado correctamente.\n\n¡NO OLVIDES DESCARGAR LA LLAVE!")

    def descargar_archivos(self):
        """
        Guarda DOS archivos:
        1. El mensaje encriptado (.txt o .enc)
        2. La llave secreta (.key)
        """
        if not self.cifrador or not self.mensaje_encriptado_bytes:
            QMessageBox.warning(self, "Error", "Primero debes encriptar un mensaje.")
            return

        # --- PASO 1: GUARDAR MENSAJE ENCRIPTADO ---
        contenido_encriptado = self.mensaje_encriptado_bytes.decode('utf-8')
        ruta_guardada= FileHelper.guardar_archivo_txt(self,contenido_encriptado)
        if ruta_guardada:
            llave_bytes= self.cifrador.obtener_key()
            llave_str = llave_bytes.decode('utf-8')
            FileHelper.guardar_llave_automatica(self,ruta_guardada,llave_str)

    def enviar_mensaje(self):
        print("Lógica: Preparando envío de correo/mensaje...")

    def regresar_menu(self):
        from homePage.menu import MenuWindow
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EncriptarLogic()
    window.show()
    sys.exit(app.exec())