"""
Lógica de Encriptación
======================
Controlador que maneja la encriptación y el envío por correo seguro.

Archivo: app/encriptacion/controller/encriptarLogic.py
"""

import sys
from PyQt6.QtWidgets import QApplication, QMessageBox

# 1. IMPORTAR VISTA Y COMPONENTES
from encriptacion.views.EncriptarWindow import EncriptarWindowUI
from common.FileHelper import FileHelper
from common.EmailDialog import EmailDialog 

# 2. IMPORTAR TU HERRAMIENTA DE ENCRIPTACIÓN
from encriptacion.tools.AesCipher import AesCipher

class EncriptarLogic(EncriptarWindowUI):
    def __init__(self):
        super().__init__()
        
        # Variables de estado
        self.cifrador = None 
        self.mensaje_encriptado_bytes = None
        
        # Inicializamos los botones y conexiones
        self.inicializar_logica()

    def inicializar_logica(self):
        # Conexiones de botones principales
        self.ui.btnEncriptar.clicked.connect(self.encriptar_mensaje)
        self.ui.btnDescargar.clicked.connect(self.descargar_archivos)
        self.ui.btnRegresar.clicked.connect(self.regresar_menu)
        self.ui.btnCargar.clicked.connect(self.cargar_archivo_txt)
        
        # Conexión del botón de ENVÍO
        self.ui.btnEnviar.clicked.connect(self.preparar_envio_correo)

    # ========================================================================
    # LÓGICA DE NEGOCIO
    # ========================================================================

    def cargar_archivo_txt(self):
        contenido, _ = FileHelper.abrir_archivo(self)
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

        # 1. Instanciar la herramienta (Genera una LLAVE NUEVA automáticamente)
        self.cifrador = AesCipher()
        
        # 2. Encriptar
        self.mensaje_encriptado_bytes = self.cifrador.encriptar(mensaje_plano)
        
        # Convertir a string SOLO para mostrar en pantalla
        mensaje_encriptado_str = self.mensaje_encriptado_bytes.decode('utf-8')
        
        # 3. Mostrar el resultado
        self.ui.txtMensaje.setText(mensaje_encriptado_str)
        
        QMessageBox.information(self, "Éxito", "Mensaje encriptado correctamente.\n\nPuedes descargarlo o enviarlo por correo.")

    def descargar_archivos(self):
        """
        Guarda el mensaje y la llave en el disco duro.
        """
        if not self.cifrador or not self.mensaje_encriptado_bytes:
            QMessageBox.warning(self, "Error", "Primero debes encriptar un mensaje.")
            return

        # Guardar mensaje encriptado
        contenido_encriptado = self.mensaje_encriptado_bytes.decode('utf-8')
        ruta_guardada = FileHelper.guardar_archivo_txt(self, contenido_encriptado)
        
        # Si se guardó el mensaje, guardamos la llave automáticamente
        if ruta_guardada:
            llave_bytes = self.cifrador.obtener_key()
            llave_str = llave_bytes.decode('utf-8')
            FileHelper.guardar_llave_automatica(self, ruta_guardada, llave_str)

    def preparar_envio_correo(self):
        """
        Prepara los datos en RAM y abre el modal hermoso de correo.
        NO requiere guardar los archivos en el disco previamente.
        """
        # 1. Validar que exista información encriptada
        if not self.cifrador or not self.mensaje_encriptado_bytes:
            QMessageBox.warning(self, "Atención", "No hay datos para enviar.\nPrimero escribe un mensaje y presiona 'Encriptar'.")
            return

        # 2. Empaquetar los datos "virtuales" para el correo
        # Obtenemos los bytes puros
        bytes_mensaje = self.mensaje_encriptado_bytes
        bytes_llave = self.cifrador.obtener_key()

        # Creamos la lista de adjuntos en memoria
        datos_para_enviar = [
            {
                'nombre': 'mensaje_seguro.txt',  # Nombre que verá el destinatario
                'contenido': bytes_mensaje
            },
            {
                'nombre': 'acceso_unico.key',    # Nombre que verá el destinatario
                'contenido': bytes_llave
            }
        ]

        # 3. Abrir el diálogo Modal (Tu ventana hermosa)
        # Al usar .exec(), la ventana principal espera a que termines con el correo
        dialogo = EmailDialog(parent=self, archivos_memoria=datos_para_enviar)
        dialogo.exec()

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